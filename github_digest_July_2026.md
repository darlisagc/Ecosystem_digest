# Monthly Digest: Ecosystem Tooling - GitHub Activities

Period: 2026-07-01 to 2026-07-31

## 🔹 [cardano-foundation/cardano-ibc-incubator](https://github.com/cardano-foundation/cardano-ibc-incubator)

**Issues opened:**
- [#552 - [👷 Task]: Prevent probabilistic light client deadlock when bridge evidence exceeds transaction limits](https://github.com/cardano-foundation/cardano-ibc-incubator/issues/552)

**PRs merged & closed:**
- [#553 - fix(dapp): disable swap and query routes](https://github.com/cardano-foundation/cardano-ibc-incubator/pull/553)
- [#551 - Enhance Cardano to Injective Testnet walkthrough and fix runtime issues](https://github.com/cardano-foundation/cardano-ibc-incubator/pull/551)
- [#549 - fix: reproduce validator voting power bypass](https://github.com/cardano-foundation/cardano-ibc-incubator/pull/549)
- [#548 - docs: refresh trust model and runtime guidance](https://github.com/cardano-foundation/cardano-ibc-incubator/pull/548)
- [#547 - fix: cardano first seen voucher recv budget](https://github.com/cardano-foundation/cardano-ibc-incubator/pull/547)
- [#546 - chore: bump Cardano probabilistic light client modules](https://github.com/cardano-foundation/cardano-ibc-incubator/pull/546)
- [#545 - fix: verify Cardano block bodies from raw CBOR](https://github.com/cardano-foundation/cardano-ibc-incubator/pull/545)

**Issues closed:**
- [#544 - TBD: intermittent v8 light client issue](https://github.com/cardano-foundation/cardano-ibc-incubator/issues/544)

## 🔹 [cardano-foundation/cardano-rosetta-java](https://github.com/cardano-foundation/cardano-rosetta-java)

**Issues opened:**
- [#771 - 3.`/account/balance` and `/account/coins` - CIP-113 support](https://github.com/cardano-foundation/cardano-rosetta-java/issues/771)
- [#770 - add 'resolve_smart_wallet_addr' in the /network/options response](https://github.com/cardano-foundation/cardano-rosetta-java/issues/770)
- [#769 - 2. `/call` — `resolve_smart_wallet_addr` Method - CIP-113](https://github.com/cardano-foundation/cardano-rosetta-java/issues/769)
- [#768 - 1: `/construction/derive` — CIP-113 Smart Wallet Address Derivation](https://github.com/cardano-foundation/cardano-rosetta-java/issues/768)
- [#763 - INDEXER_DB_* environment variables from 2.1.1 are missing from env-vars.md reference](https://github.com/cardano-foundation/cardano-rosetta-java/issues/763)

**PRs merged & closed:**
- [#773 - Revert sync-status gating/caching/scheduler (#758, #761, #767)](https://github.com/cardano-foundation/cardano-rosetta-java/pull/773)
- [#767 - feat(sync) status refresh scheduler](https://github.com/cardano-foundation/cardano-rosetta-java/pull/767)
- [#765 - chore: bump yaci-store to 2.0.2.1](https://github.com/cardano-foundation/cardano-rosetta-java/pull/765)
- [#762 - fix: drop empty account identifier from operations](https://github.com/cardano-foundation/cardano-rosetta-java/pull/762)
- [#761 - feat: add 5s cache for sync status verification](https://github.com/cardano-foundation/cardano-rosetta-java/pull/761)
- [#755 - chore: prepare 2.3.0](https://github.com/cardano-foundation/cardano-rosetta-java/pull/755)

**Issues closed:**
- [#736 - Spike: replace 'apply indexes' with a native solution](https://github.com/cardano-foundation/cardano-rosetta-java/issues/736)

## 🔹 [bloxbean/cardano-client-lib](https://github.com/bloxbean/cardano-client-lib)

**Issues opened:**
- [#637 - Add an immutable, strict and total Ed25519 verification API](https://github.com/bloxbean/cardano-client-lib/issues/637)
- [#636 - QuickTx: complete v1alpha1 transaction JSON Schema for all portable TxIntent types](https://github.com/bloxbean/cardano-client-lib/issues/636)

**PRs merged & closed:**
- [#639 - TxFlowStream v2: streaming transaction submission on FlowEngine (ADR 0004) + txflow refinement iteration](https://github.com/bloxbean/cardano-client-lib/pull/639)
- [#638 - fix(jmt): complete production readiness hardening](https://github.com/bloxbean/cardano-client-lib/pull/638)
- [#635 - feat(txflow): implement portable contract and runtime](https://github.com/bloxbean/cardano-client-lib/pull/635)
- [#634 - feat: add QuickTx policy and script reference resolution](https://github.com/bloxbean/cardano-client-lib/pull/634)
- [#631 - feat: add TxFlow flow-level execution context](https://github.com/bloxbean/cardano-client-lib/pull/631)

**Issues closed:**
- [#633 - CostModelUtil: zero-padded numeric cost-model keys ("000".."165") are not sorted, breaking script-integrity hash for some callers](https://github.com/bloxbean/cardano-client-lib/issues/633)

## 🔹 [bloxbean/yaci-devkit](https://github.com/bloxbean/yaci-devkit)

**Issues opened:**
- [#185 - yaci-store omits PlutusV2 cost model from /api/v1/epochs/parameters (yaci-cli 0.12.0-beta5)](https://github.com/bloxbean/yaci-devkit/issues/185)
- [#184 - PV11 cost-model governance bootstrap fails with "Plutus cost models update failed: null" (yaci-cli 0.12.0-beta5, -b1)](https://github.com/bloxbean/yaci-devkit/issues/184)
- [#183 - BLS12-381 Plutus scripts fail with native Yaci Store on Scalus evaluator (missing blst JNI config)](https://github.com/bloxbean/yaci-devkit/issues/183)
- [#182 -  crashes when starting node](https://github.com/bloxbean/yaci-devkit/issues/182)
- [#181 - `yaci-cli` crashes on launch if `initialAddresses` at any index is changed at all](https://github.com/bloxbean/yaci-devkit/issues/181)
- [#180 - `yaci-cli` fails to find its own config if run from anywhere but the same directory](https://github.com/bloxbean/yaci-devkit/issues/180)
- [#179 - `yaci.cli.home` is not respected for (at least) downloads](https://github.com/bloxbean/yaci-devkit/issues/179)

**Issues closed:**
- [#182 -  crashes when starting node](https://github.com/bloxbean/yaci-devkit/issues/182)

## 🔹 [bloxbean/yaci](https://github.com/bloxbean/yaci)

**Issues opened:**
- [#174 - Bug: GovStateQuery fails to decode governance state when committee is absent after NoConfidence ratification](https://github.com/bloxbean/yaci/issues/174)
- [#170 - ADR 0010: Leios (Musashi) serialization & BlockChainDataListener integration design](https://github.com/bloxbean/yaci/issues/170)
- [#166 - Implement Leios network mini-protocols (LeiosNotify/LeiosFetch) for Musashi testnet — transport-only](https://github.com/bloxbean/yaci/issues/166)

**PRs merged & closed:**
- [#176 - Add full transaction CBOR reconstruction via raw segment splicing (returnFullTxCbor) [next]](https://github.com/bloxbean/yaci/pull/176)
- [#175 - feat(helper): app-chain sync (103) on the shared peer connection](https://github.com/bloxbean/yaci/pull/175)
- [#173 - feat(appmsg): app-layer transport — envelope v2, chain negotiation, app-chain-sync (protocol 103)](https://github.com/bloxbean/yaci/pull/173)
- [#172 - feat(txsubmission): allow listeners to filter tx body requests](https://github.com/bloxbean/yaci/pull/172)
- [#169 - Add full transaction CBOR reconstruction via raw segment splicing (returnFullTxCbor)](https://github.com/bloxbean/yaci/pull/169)
- [#165 - feat: Add relay transport hooks for connection governance and peer sharing](https://github.com/bloxbean/yaci/pull/165)

## 🔹 [bloxbean/yaci-store](https://github.com/bloxbean/yaci-store)

**Issues opened:**
- [#1048 - DRep vote from before re-registration is incorrectly counted in voting tally](https://github.com/bloxbean/yaci-store/issues/1048)
- [#1047 - Snapshot Feature](https://github.com/bloxbean/yaci-store/issues/1047)
- [#1045 - Scalus: BLS12-381 builtins fail in GraalVM native image — missing JNI/resource config for blst](https://github.com/bloxbean/yaci-store/issues/1045)
- [#1044 - Blockfrost block addresses endpoint scans address_utxo due to block/block_hash index mismatch](https://github.com/bloxbean/yaci-store/issues/1044)
- [#1042 - [Blockfrost] Retest merged extension modules across networks](https://github.com/bloxbean/yaci-store/issues/1042)
- [#1041 - Blockfrost /blocks/latest performs full table scan due to DESC NULLS LAST ordering](https://github.com/bloxbean/yaci-store/issues/1041)
- [#1033 - Add tx_index (and cert_index where relevant) to tables lacking exact intra-block ordering](https://github.com/bloxbean/yaci-store/issues/1033)
- [#1030 - [Governance] Compute non-voting SPO default delegation per proposal](https://github.com/bloxbean/yaci-store/issues/1030)
- [#1029 - Java Plugin - Add docs](https://github.com/bloxbean/yaci-store/issues/1029)
- [#1028 - [Governance] Make ParameterChange validation phase-aware and simplify group handling](https://github.com/bloxbean/yaci-store/issues/1028)
- [#1023 - [Governance] Bootstrap phase: SECURITY parameter changes should still require SPO approval](https://github.com/bloxbean/yaci-store/issues/1023)
- [#1022 - [Governance] Committee member expiry boundary should be inclusive](https://github.com/bloxbean/yaci-store/issues/1022)
- [#1018 - Expose network identity (protocol magic) via the API](https://github.com/bloxbean/yaci-store/issues/1018)
- [#1017 - [Governance] SPO AlwaysNoConfidence non-voters counted as No/Yes instead of Abstain in bootstrap phase](https://github.com/bloxbean/yaci-store/issues/1017)
- [#1016 - Yaci Store 2.0.3 Planning Tracker](https://github.com/bloxbean/yaci-store/issues/1016)
- [#1013 - Committee accepted-ratio comparison rounds before threshold comparison, can diverge from cardano-ledger](https://github.com/bloxbean/yaci-store/issues/1013)
- [#1009 - Java Plugins](https://github.com/bloxbean/yaci-store/issues/1009)
- [#1004 - Yaci-indexer stops stalling, requiring restarts to recover](https://github.com/bloxbean/yaci-store/issues/1004)

**PRs merged & closed:**
- [#1039 - [Merge to 2.0.x] fix: make parameter change validation phase-aware](https://github.com/bloxbean/yaci-store/pull/1039)
- [#1038 - [Merge to 2.0.x] test(governance): preserve HFI tally behavior across phases](https://github.com/bloxbean/yaci-store/pull/1038)
- [#1037 - [Merge to 2.0.x] Fix: require SPO approval for bootstrap SECURITY param changes](https://github.com/bloxbean/yaci-store/pull/1037)
- [#1036 - [Merge to 2.0.x] Fix committee member expiry boundary](https://github.com/bloxbean/yaci-store/pull/1036)
- [#1035 - [Merge to 2.0.x] Fix SPO tally bootstrap default delegation](https://github.com/bloxbean/yaci-store/pull/1035)
- [#1032 - fix: make parameter change validation phase-aware](https://github.com/bloxbean/yaci-store/pull/1032)
- [#1031 - test(governance): preserve HFI tally behavior across phases](https://github.com/bloxbean/yaci-store/pull/1031)
- [#1027 - [Merge to main] feat: expose network identity and sync status](https://github.com/bloxbean/yaci-store/pull/1027)
- [#1026 - [Backport] fix(governance): compare committee ratios exactly](https://github.com/bloxbean/yaci-store/pull/1026)
- [#1025 - Fix: require SPO approval for bootstrap SECURITY param changes](https://github.com/bloxbean/yaci-store/pull/1025)
- [#1024 - Fix committee member expiry boundary](https://github.com/bloxbean/yaci-store/pull/1024)
- [#1021 - feat: expose network identity and sync status](https://github.com/bloxbean/yaci-store/pull/1021)
- [#1020 - [Governance rule] Fix SPO tally bootstrap default delegation](https://github.com/bloxbean/yaci-store/pull/1020)
- [#1014 - fix(governance): compare committee ratios exactly](https://github.com/bloxbean/yaci-store/pull/1014)
- [#1012 - docs(home): replace CBI Backend Service card with Nexus in Trusted By](https://github.com/bloxbean/yaci-store/pull/1012)
- [#1011 - Java plugins](https://github.com/bloxbean/yaci-store/pull/1011)
- [#1010 - docs: add Nexus (A.D. Labs) to showcase page and Trusted By section](https://github.com/bloxbean/yaci-store/pull/1010)
- [#1008 - [backport] fix: reset auto-restart counter on a sliding window ](https://github.com/bloxbean/yaci-store/pull/1008)
- [#1007 - [Backport to main] Backport JVM DNS TTL defaults for Yaci 0.4.4 to main](https://github.com/bloxbean/yaci-store/pull/1007)
- [#1006 - [Backport to 2.0.x] Backport devkit custom network fixes to release/2.0.x](https://github.com/bloxbean/yaci-store/pull/1006)
- [#1005 - [Backport to main] Backport devkit custom network fixes to main](https://github.com/bloxbean/yaci-store/pull/1005)
- [#1003 - [Backport] fix: reset auto-restart counter on a sliding window ](https://github.com/bloxbean/yaci-store/pull/1003)
- [#1001 - Test: add governance proposal status devnet ITs](https://github.com/bloxbean/yaci-store/pull/1001)
- [#1000 - [Backport] Backport assets-ext  extension to release/2.0.x](https://github.com/bloxbean/yaci-store/pull/1000)
- [#999 - docs: simplify scope tutorial queries](https://github.com/bloxbean/yaci-store/pull/999)
- [#998 - fix: reset auto-restart counter on a sliding window ](https://github.com/bloxbean/yaci-store/pull/998)

**Issues closed:**
- [#1028 - [Governance] Make ParameterChange validation phase-aware and simplify group handling](https://github.com/bloxbean/yaci-store/issues/1028)
- [#1023 - [Governance] Bootstrap phase: SECURITY parameter changes should still require SPO approval](https://github.com/bloxbean/yaci-store/issues/1023)
- [#1022 - [Governance] Committee member expiry boundary should be inclusive](https://github.com/bloxbean/yaci-store/issues/1022)
- [#996 - Indexer permanently stops retrying after `maxAttempts` and needs a manual restart](https://github.com/bloxbean/yaci-store/issues/996)
- [#975 - [2.1.0-pre]  Test Blockfrost Extension Modules](https://github.com/bloxbean/yaci-store/issues/975)


---

Let's keep building! 🚀
