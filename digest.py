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

# Calculate the start and end dates for the past month
end_date = datetime.datetime.utcnow()
start_date = end_date - datetime.timedelta(days=30)

# GitHub API headers
headers = {
    "Accept": "application/vnd.github.v3+json"
}

# Function to fetch PRs and issues within the last month
def fetch_github_activity(repo):
    activity = {"opened": [], "closed": [], "merged": []}

    # Fetch PRs
    prs_url = f"{github_api_base}{repo}/pulls?state=all&per_page=100"
    response = requests.get(prs_url, headers=headers)
    if response.status_code == 200:
        prs = response.json()
        for pr in prs:
            created_at = datetime.datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            closed_at = pr["closed_at"]
            merged_at = pr["merged_at"]
            pr_link = pr["html_url"]
            pr_number = pr["number"]
            pr_title = pr["title"]

            if created_at >= start_date:
                activity["opened"].append(f"[#{pr_number} - {pr_title}]({pr_link})")

            if closed_at and datetime.datetime.strptime(closed_at, "%Y-%m-%dT%H:%M:%SZ") >= start_date:
                activity["closed"].append(f"[#{pr_number} - {pr_title}]({pr_link})")

            if merged_at and datetime.datetime.strptime(merged_at, "%Y-%m-%dT%H:%M:%SZ") >= start_date:
                activity["merged"].append(f"[#{pr_number} - {pr_title}]({pr_link})")

    # Fetch Issues
    issues_url = f"{github_api_base}{repo}/issues?state=all&per_page=100"
    response = requests.get(issues_url, headers=headers)
    if response.status_code == 200:
        issues = response.json()
        for issue in issues:
            if "pull_request" not in issue:  # Ignore PRs listed under issues
                created_at = datetime.datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                closed_at = issue["closed_at"]
                issue_link = issue["html_url"]
                issue_number = issue["number"]
                issue_title = issue["title"]

                if created_at >= start_date:
                    activity["opened"].append(f"[#{issue_number} - {issue_title}]({issue_link})")

                if closed_at and datetime.datetime.strptime(closed_at, "%Y-%m-%dT%H:%M:%SZ") >= start_date:
                    activity["closed"].append(f"[#{issue_number} - {issue_title}]({issue_link})")

    return activity

# Fetch activity for each repo
repo_activities = {repo: fetch_github_activity(repo) for repo in repos}

# Create digest text
digest_content = "# Monthly Digest: GitHub Activity\n\n"
digest_content += f"Period: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}\n\n"

for repo, activity in repo_activities.items():
    repo_link = f"https://github.com/{repo}"
    digest_content += f"## [{repo}]({repo_link})\n\n"

    if activity["opened"]:
        digest_content += "**Opened Issues & PRs:**\n" + "\n".join(activity["opened"]) + "\n\n"
    if activity["closed"]:
        digest_content += "**Closed Issues & PRs:**\n" + "\n".join(activity["closed"]) + "\n\n"
    if activity["merged"]:
        digest_content += "**Merged PRs:**\n" + "\n".join(activity["merged"]) + "\n\n"

    if not any(activity.values()):
        digest_content += "_No significant activity in this period._\n\n"

# Generate file name with month and year (e.g., github_digest_February_2025.md)
filename = f"github_digest_{end_date.strftime('%B_%Y')}.md"
with open(filename, "w") as file:
    file.write(digest_content)

print("Monthly digest saved to github_digest.md")
