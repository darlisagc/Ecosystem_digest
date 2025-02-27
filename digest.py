import requests
import datetime

# List of repositories to track
repos = [
    "bloxbean/cardano-client-lib",
    "bloxbean/yaci",
    "bloxbean/yaci-store",
    "bloxbean/yaci-devkit"
]

# GitHub API base URL
github_api_base = "https://api.github.com/repos/"

# Calculate the start and end dates for the past 30 days
end_date = datetime.datetime.utcnow()
start_date = end_date - datetime.timedelta(days=30)

# GitHub API headers
headers = {
    "Accept": "application/vnd.github.v3+json"
}

# Function to fetch GitHub activity within the last 30 days
def fetch_github_activity(repo):
    # Categories:
    # - issues_opened: issues created within the period
    # - issues_closed: issues closed within the period
    # - pr_merged: pull requests that are merged (and therefore closed) within the period
    activity = {"issues_opened": [], "issues_closed": [], "pr_merged": []}

    # Fetch PRs and include only those that are merged
    prs_url = f"{github_api_base}{repo}/pulls?state=all&per_page=100"
    response = requests.get(prs_url, headers=headers)
    if response.status_code == 200:
        prs = response.json()
        for pr in prs:
            merged_at = pr.get("merged_at")
            if merged_at:
                merged_date = datetime.datetime.strptime(merged_at, "%Y-%m-%dT%H:%M:%SZ")
                if merged_date >= start_date:
                    pr_link = pr["html_url"]
                    pr_number = pr["number"]
                    pr_title = pr["title"]
                    activity["pr_merged"].append(f"- [#{pr_number} - {pr_title}]({pr_link})")

    # Fetch issues (excluding PRs)
    issues_url = f"{github_api_base}{repo}/issues?state=all&per_page=100"
    response = requests.get(issues_url, headers=headers)
    if response.status_code == 200:
        issues = response.json()
        for issue in issues:
            # Skip items that are actually PRs
            if "pull_request" in issue:
                continue

            created_at = datetime.datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            closed_at = issue.get("closed_at")
            issue_link = issue["html_url"]
            issue_number = issue["number"]
            issue_title = issue["title"]

            if created_at >= start_date:
                activity["issues_opened"].append(f"- [#{issue_number} - {issue_title}]({issue_link})")

            if closed_at and datetime.datetime.strptime(closed_at, "%Y-%m-%dT%H:%M:%SZ") >= start_date:
                activity["issues_closed"].append(f"- [#{issue_number} - {issue_title}]({issue_link})")

    return activity

# Fetch activity for each repository
repo_activities = {repo: fetch_github_activity(repo) for repo in repos}

# Create digest text
digest_content = "# Monthly Digest: GitHub Activity\n\n"
digest_content += f"Period: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}\n\n"

for repo, activity in repo_activities.items():
    repo_link = f"https://github.com/{repo}"
    digest_content += f"## [{repo}]({repo_link})\n\n"

    if activity["issues_opened"]:
        digest_content += "**Issues opened:**\n" + "\n".join(activity["issues_opened"]) + "\n\n"
    if activity["pr_merged"]:
        digest_content += "**PRs merged & closed:**\n" + "\n".join(activity["pr_merged"]) + "\n\n"
    if activity["issues_closed"]:
        digest_content += "**Issues closed:**\n" + "\n".join(activity["issues_closed"]) + "\n\n"

    if not (activity["issues_opened"] or activity["pr_merged"] or activity["issues_closed"]):
        digest_content += "_No significant activity in this period._\n\n"

# Generate file name with month and year (e.g., github_digest_February_2025.md)
filename = f"github_digest_{end_date.strftime('%B_%Y')}.md"
with open(filename, "w") as file:
    file.write(digest_content)

print(f"Monthly digest saved to {filename}")
