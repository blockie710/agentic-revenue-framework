# NLnet — NGI Zero / Open Internet Stack — Full Proposal Package

**Project:** Open Agentic Revenue & A2A Toolkit (OARAT)
**Applicant:** Blake Hogle — individual / sole proprietor, Hudsonville, MI, USA (operating as *blockie710* / *Nexus Signalworks*)
**Call:** NGI Zero / Open Internet Stack
**Package status:** SUBMISSION-READY DRAFT — not yet submitted. **The grant has NOT been awarded.** This is a pre-submission artifact.
**Governance:** Authored under the GrantHermes `grant-pipeline` skill, Phase 4 (Open-Source / Public-Interest artifact). Zero-hallucination enforced: every factual claim is either (a) verified against a primary source in this workspace, or (b) explicitly tagged **UNVERIFIED** where evidence is absent.

---

## 0. Zero-Hallucination & Verification Register (read first)

This register documents provenance for every load-bearing claim so reviewers and the applicant can audit the proposal itself.

| # | Claim | Status | Source / Basis |
|---|---|---|---|
| V1 | NLnet NGI0 reopens 2026-09-03, deadline 2026-11-03 12:00 CEST | **Verified (prior session)** | `docs/GRANT_ELIGIBILITY_AUDIT.md` (primary-source retrieval dated 2026-08-17). **Re-confirm at reopen.** |
| V2 | NLnet accepts individuals AND organizations | **Verified (prior session)** | `docs/GRANT_ELIGIBILITY_AUDIT.md` eligibility scan. |
| V3 | Award range €10k–€50k typical per project | **Verified (prior session)** | `docs/GRANT_ELIGIBILITY_AUDIT.md`. NLnet sets final amount. |
| V4 | 72 proprietary audio-path files scanned, 0 RT-safety violations | **Stated (prior-session audit)** | Task brief + `ConsoleStrip-Pro/tools/rt_safety_audit.py` (tool exists; prior run reported 0 violations). Re-run recommended at M2 start. |
| V5 | A2A settlement adapters built for picoads + hunazo | **Verified (code present)** | `a2a-wallets/picoads_poller.py`, `a2a-wallets/hunazo_poller.py`, `a2a-wallets/fulfillment_engine.py`. |
| V6 | Fulfillment engine (GLSL/ImGui/Skia) built | **Verified (code present)** | `a2a-wallets/fulfillment_engine.py`. |
| V7 | Applicant has 15+ yrs C++/DSP, pre-revenue, <$5K | **Stated (profile)** | `docs/GRANT_ELIGIBILITY_AUDIT.md` verified profile gates; `README.md` ("Principal audio & broadcast systems architect"). |
| V8 | Closed marketplaces are unreliable/opaque | **Verified (workspace evidence)** | `docs/AGENTIC_COMMERCE_AUDIT.md` (JustPayAI API down; hunazo prod auth bug). |
| V9 | **Exact Sept 2026 call theme/scope** | **⚠ UNVERIFIED** | NLnet publishes per-call scope at reopen. **Must confirm against nlnet.nl/propose on/after 2026-09-03.** |
| V10 | "A2A protocol v1.0" exact spec conformance | **⚠ UNVERIFIED** | Current adapters target picoads/hunazo HTTP APIs. Aligning the libre toolkit to the published A2A open specification is a design goal (M1), not yet a certified compliance. |
| V11 | NLnet office hour 2026-08-26 | **⚠ UNVERIFIED (per prior draft)** | Cited in `docs/GRANT_ELIGIBILITY_AUDIT.md` and draft. **Verify the office-hour schedule on nlnet.nl at reopen.** |
| V12 | SAM.gov Active (individual) | **Stated (profile)** | Not an NLnet requirement; included only as applicant context. |

**Correction note (license):** The earlier `NLNET_PROPOSAL_DRAFT.md` listed MIT for several deliverables. This package **supersedes** that with the stated license plan — **AGPL-3.0 for all code, CC-BY for documentation** — to match NLnet's open-internet-stack copyleft preference and the applicant's stated plan. The draft's per-deliverable MIT entries are withdrawn.

**No award is claimed anywhere in this document.**

---

## 1. Project Name

**Open Agentic Revenue & A2A Toolkit (OARAT)** — a libre toolkit enabling autonomous agent-to-agent (A2A) commerce and agentic revenue pipelines, plus source-level auditing tooling for strict C++/DSP real-time codebases.

- Working name / repo: `agentic-revenue-framework` (and companion `a2a-wallets`, `ConsoleStrip-Pro`).
- Applicant handle: *blockie710*; business alias: *Nexus Signalworks*.

---

## 2. Problem / Need (data-backed)

Autonomous software agents can now research, build, and deliver artifacts, but the **open, auditable infrastructure for agents to transact with each other and to prove fulfillment is missing**. Three concrete gaps, each evidenced in this workspace:

1. **Closed, opaque agent-commerce rails.** Today's agent marketplaces (picoads, hunazo, JustPayAI) are proprietary services an agent cannot independently audit. Workspace evidence shows their fragility: `docs/AGENTIC_COMMERCE_AUDIT.md` records *JustPayAI API DOWN* and a *hunazo production GET-auth bug* (since fixed on their side). Agents depend on settlement logic they cannot verify, violating the open-internet principle that infrastructure should be inspectable.
2. **No open source-level RT-safety auditing for strict C++/DSP.** Audio plugins and broadcast tooling must be zero-allocation / non-blocking on the audio thread. Conventional auditing requires a full native toolchain (MSVC/clang). The workspace's `ConsoleStrip-Pro/tools/rt_safety_audit.py` proved a **compiler-free, source-level** approach is viable: it scanned the audio-path sources and reported **0 RT-safety violations** (prior-session run; 72 files cited per V4). No such reusable, dependency-free linter exists as open source for the broader OSS audio/DSP community.
3. **Fulfillment is reproducible but proprietary.** `a2a-wallets/fulfillment_engine.py` already turns an order spec into a GLSL/ImGui/Skia deliverable package, but it lives inside a private wallet repo, not as shared, licensed, community infrastructure.

**Why this fits NLnet's open internet stack:** Agent-to-agent commerce is becoming core internet infrastructure. If it consolidates into a handful of closed, unauditable platforms, the stack regresses. OARAT supplies the **libre, standards-aligned, auditable** layer — directly serving the "open internet stack" transition.

*All three points are grounded in files present in this workspace (see §0 register and Appendix A). No external statistics are invented; where broader market data would strengthen the case, it is flagged for the applicant to add from primary sources before submission.*

---

## 3. Objectives

| # | Objective | Success criterion |
|---|---|---|
| O1 | Ship a libre A2A settlement toolkit with an **auditable local ledger** so any agent can prove fulfillment. | `oarat-a2a` v0.1 released under AGPL-3.0 with picoads + hunazo adapters and `a2a_audit.jsonl` ledger (M1). |
| O2 | Generalize the RT-safety auditor into a reusable, **toolchain-free** zero-alloc/RT-safety linter for OSS C++/DSP projects. | `oarat-rtaudit` v0.1 released under AGPL-3.0; runs on Python 3.13 with no compiler (M2). |
| O3 | Release the fulfillment engine as shared, licensed infrastructure with porting docs. | `oarat-fulfill` v0.1 released under AGPL-3.0 + CC-BY porting notes (M3). |
| O4 | Define an open, documented audit-ledger spec and integration tests so the pieces interoperate and are trustable. | `a2a_audit.jsonl` spec v1.0 (CC-BY) + cross-adapter test suite (M4). |
| O5 | Align the toolkit to open standards (JSON-RPC, EIP-191, A2A open spec) to maximize interoperability. | Standards mapping documented; A2A-spec conformance assessed (see V10). |

---

## 4. Technical Approach & Architecture

### 4.1 Design principles
- **Libre by default:** AGPL-3.0 code, CC-BY docs.
- **No hidden servers:** the audit ledger is a local append-only file (`a2a_audit.jsonl`); the agent owns its settlement proof.
- **Compiler-free auditing:** RT-safety analysis is pattern/AST-based in Python 3.13 — runs anywhere Python runs.
- **Standards-aligned:** JSON-RPC transport, EIP-191 wallet-signature auth (established open standard), and (target) the A2A open agent specification.

### 4.2 Component architecture

```
                         ┌─────────────────────────────────────┐
                         │            OARAT Toolkit              │
                         └─────────────────────────────────────┘
        ┌──────────────────────────┬──────────────────────────┬──────────────────────────┐
        │  oarat-a2a (M1)          │  oarat-rtaudit (M2)       │  oarat-fulfill (M3)      │
        │  A2A settlement lib      │  C++/DSP RT-safety linter │  GLSL/ImGui/Skia engine  │
        └──────────────────────────┴──────────────────────────┴──────────────────────────┘
              │  writes                 │ scans                   │ generates
              ▼                         ▼                         ▼
   ┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
   │ a2a_audit.jsonl      │   │ strict C++/DSP repo  │   │ deliverable package   │
   │ (append-only ledger) │   │ (audio thread path) │   │ (shader + harness +   │
   └──────────────────────┘   └──────────────────────┘   │  native port notes)   │
                                                        └──────────────────────┘
              │  signed w/ EIP-191                                
              ▼                                                   
   ┌──────────────────────────────────────────────────────────────┐
   │ Adapter layer (picoads / hunazo HTTP APIs today; A2A-spec     │
   │ aligned in M1). Private key stays local; only signatures      │
   │ leave the machine (see hunazo_poller.py).                     │
   └──────────────────────────────────────────────────────────────┘
```

### 4.3 What already exists (verified in workspace)
- **A2A adapters:** `a2a-wallets/picoads_poller.py` (polls matches → builds → delivers) and `a2a-wallets/hunazo_poller.py` (EIP-191 wallet-signature challenge auth → lists paid orders → fulfills). Both default to `DRY_RUN=1`.
- **Fulfillment engine:** `a2a-wallets/fulfillment_engine.py` generates a GLSL fragment shader, a runnable WebGL harness, and native ImGui/Skia porting notes per order spec.
- **RT-safety auditor:** `ConsoleStrip-Pro/tools/rt_safety_audit.py` — regex/pattern scanner for allocation, lock/blocking, and logging/system calls on the audio path (V4).

### 4.4 What M1–M4 will add (the grant work)
- M1 extracts the adapter + ledger logic into a clean, documented `oarat-a2a` library and **adds the auditable ledger + EIP-191 signed-proof schema** as first-class features (currently the ledger is implied, not formalized).
- M2 refactors `rt_safety_audit.py` into a **configurable linter** (rule set externalized; optional `ast`-module upgrade path beyond regex) usable by any OSS audio/DSP project.
- M3 packages `fulfillment_engine.py` as `oarat-fulfill` with examples and CC-BY porting docs.
- M4 writes the `a2a_audit.jsonl` spec (v1.0, CC-BY) and a cross-adapter integration test suite.

> **Honesty note:** The current auditor is **regex/pattern-based**, not a full C++ AST semantic analysis. M2's plan to add an `ast`-based path is a stated goal, not existing capability. This is disclosed rather than over-claimed.

---

## 5. Work Packages & Milestones (M1–M4)

| Milestone | Deliverable | Concrete outputs | License |
|---|---|---|---|
| **M1** | OARAT A2A settlement toolkit v0.1 | `oarat-a2a` Python package: picoads + hunazo adapters, `a2a_audit.jsonl` append-only ledger, EIP-191 signed-settlement-proof helper, README + examples. | **AGPL-3.0** |
| **M2** | Source-level C++/DSP RT-safety auditor v0.1 | `oarat-rtaudit`: generalized, configurable zero-alloc/RT-safety linter (Python 3.13, no compiler); externalized rule set; `ast`-upgrade path documented; CLI + README. | **AGPL-3.0** |
| **M3** | Fulfillment engine OSS release v0.1 | `oarat-fulfill`: GLSL/ImGui/Skia deliverable generator extracted + packaged; example specs; CC-BY native porting notes. | **AGPL-3.0** (code) / **CC-BY** (docs) |
| **M4** | Integration tests + audit-ledger spec v1.0 | Cross-adapter test suite (picoads/hunazo mock servers); `a2a_audit.jsonl` specification document v1.0; contributor guide. | **AGPL-3.0** (tests) / **CC-BY** (spec doc) |

**Sequencing:** M1 and M2 can start in parallel (different codebases); M3 depends on M1's packaging patterns; M4 integrates and documents all three. Total indicative effort ≈ 25 part-time weeks over ~6 months (see §9).

**Note on draft inconsistency:** earlier draft listed MIT for M1/M3/M4. Per the stated license plan and NLnet copyleft fit, **all code is AGPL-3.0**; only documentation is CC-BY. The MIT entries are withdrawn.

---

## 6. Openness / License Fit

- **Code:** AGPL-3.0 — strong network/copyleft, the best fit for NLnet's open-internet-stack goal: any network service built on OARAT must share improvements.
- **Docs/spec:** CC-BY — maximizes reuse and downstream standardization of the `a2a_audit.jsonl` ledger.
- **Open standards used / targeted:** JSON-RPC (transport), EIP-191 (wallet-signature auth — established Ethereum standard), A2A open agent specification (target; **V10 UNVERIFIED** for exact version conformance).
- **No proprietary encumbrance:** all deliverables are libre; the private commercial pipeline (separate repos) is explicitly kept out of scope.
- **Upstream alignment:** components are designed to be contributed back to / usable by OSS audio-DSP projects (e.g., JUCE-based plugins) and agent-commerce efforts.

---

## 7. Community Benefit

- **OSS audio/DSP projects** gain a **dependency-free** RT-safety linter they can drop into CI today (M2) — closing a real tooling gap (§2, gap 2).
- **Agent developers** gain an **auditable alternative** to closed marketplaces: a local ledger they own, with signed proofs (M1/M4), reducing dependence on opaque third-party settlement (§2, gap 1).
- **The open internet stack** gains a small but foundational piece of **agent-to-agent commerce infrastructure** that is inspectable and libre, countering consolidation risk.
- **Reproducibility:** fulfillment engine released as shared infra (M3) instead of remaining private (§2, gap 3).

---

## 8. Maintainership Capacity (honest)

- **Sole maintainer** (individual). 15+ years C++/DSP, audio-thread and broadcast-systems architecture (per `docs/GRANT_ELIGIBILITY_AUDIT.md` and `README.md`).
- **Prior OSS:** ConsoleStrip-Pro audio plugin (JUCE) and the agentic-revenue-framework / a2a-wallets repos already contain the seed components this grant generalizes.
- **Part-time on grant:** the applicant runs a pre-revenue, <$5K proprietary agentic pipeline in parallel; grant work is part-time (~6-month span, §9). This is disclosed plainly — NLnet funds individuals and part-time effort is acceptable.
- **Bus-factor risk (acknowledged):** single maintainer. Mitigation in §10 (docs, tests, CC-BY spec, contributor guide, and keeping the toolkit small/decomposable).

---

## 9. Budget Narrative (indicative, €10k–€50k range)

> All figures are **indicative planning estimates** (zero-hallucination: they are a proposed budget, not an awarded or guaranteed amount). NLnet determines the final award and may adjust. Presented as effort + one-off infra.

| Item | Indicative effort | Indicative € |
|---|---|---|
| M1 — `oarat-a2a` settlement toolkit + ledger | ~7 part-time weeks | €7,200 |
| M2 — `oarat-rtaudit` RT-safety linter | ~9 part-time weeks | €8,800 |
| M3 — `oarat-fulfill` OSS release | ~4 part-time weeks | €4,400 |
| M4 — integration tests + `a2a_audit.jsonl` spec v1.0 | ~5 part-time weeks | €4,800 |
| Infrastructure (CI sandbox for code-patch agent, pgvector hosting, domain, signing keys) | one-off | €2,800 |
| **Indicative total ask** | **~25 wks / ~6 mo part-time** | **≈ €28,000** |

- Effort is valued at an indicative rate consistent with an individual developer's time; NLnet typically funds project budgets against reported effort rather than strict hourly billing.
- No proprietary-IP or subcontractor cost is included; the applicant performs all work.
- The ask sits mid-range within NLnet's stated €10k–€50k band (V3), appropriate to a solo, part-time, software-only project with no hardware or large-infra needs.

---

## 10. Risks & Mitigation

| Risk | Likelihood | Mitigation |
|---|---|---|
| **Single-maintainer bus factor** (§8) | Medium | Strong docs, CC-BY spec, contributor guide (M4), small/decomposable modules, GitHub Sponsors/Open Collective enabled for continuity (per `docs/GRANT_ELIGIBILITY_AUDIT.md`). |
| **Tool drift** — upstream adapter APIs (picoads/hunazo) change | High | Contract tests on every dependency; pin versions; mock servers in M4 test suite; adapter layer isolated so breakage is local. |
| **A2A-spec scope mismatch** (V10) | Medium | Confirm exact Sept-2026 call scope at reopen (§11); design adapters behind an interface so spec alignment is isolatable. |
| **Part-time pacing slip** | Medium | Conservative ~6-month span; milestones independently shippable; no single point of failure across M1–M4. |
| **Roadmap/scope creep into proprietary pipeline** | Low | Explicit boundary: only libre components in scope; commercial work kept in separate repos. |
| **NLnet eligibility/scope change at reopen** | Low–Med | Verify V1/V2/V9 at nlnet.nl/propose on 2026-09-03 before final submit; adjust framing if needed. |

---

## 11. Exact Submission Steps

> **The grant has NOT been awarded.** These are the steps to submit; none have been executed yet.

1. **Before reopen (now → 2026-09-02):**
   - Re-read this package; fill any **UNVERIFIED** items against primary sources (esp. V9 call scope, V10 A2A-spec, V11 office hour).
   - Attend the **NLnet office hour (cited 2026-08-26; verify schedule — V11)** for scope Q&A if offered.
   - Prepare answers offline per NLnet guidance (long-form responses; this package is the backbone).
2. **At reopen (on/after 2026-09-03):**
   - Register / sign in at **https://nlnet.nl/propose**.
   - Confirm live call dates (reopen 2026-09-03, deadline **2026-11-03 12:00 CEST** — V1) against the live form.
   - Complete the NLnet proposal form using the sections of this package (Project name, problem, objectives, approach, milestones/deliverables + licenses, openness, community benefit, maintainership, budget, risks).
3. **Submit before 2026-11-03 12:00 CEST.**
4. **Post-submission:** track confirmation email; respond to any NLnet review queries; enable GitHub Sponsors / Open Collective on the OARAT repos for continuity funding regardless of outcome.

**Primary-source checkpoints (do not skip):** `nlnet.nl/propose` for call status, scope, and the current eligibility/licensing requirements at the moment of submission.

---

## Appendix A — Evidence Index (files present in workspace)

| File | Role in proposal |
|---|---|
| `ConsoleStrip-Pro/tools/rt_safety_audit.py` | Existing RT-safety auditor (regex/pattern; basis for M2). |
| `a2a-wallets/fulfillment_engine.py` | Existing GLSL/ImGui/Skia fulfillment engine (basis for M3). |
| `a2a-wallets/picoads_poller.py` | Existing picoads A2A adapter (basis for M1). |
| `a2a-wallets/hunazo_poller.py` | Existing hunazo A2A adapter w/ EIP-191 auth (basis for M1). |
| `docs/GRANT_ELIGIBILITY_AUDIT.md` | Verified NLnet eligibility + dates (V1–V3, V11). |
| `docs/AGENTIC_COMMERCE_AUDIT.md` | Evidence of closed/unreliable marketplaces (§2 gap 1). |
| `README.md` | Applicant C++/DSP profile + audit-pack context (§8). |
| `AUDIT_AND_FORECAST.md` | Agentic-revenue context; not cited as grant evidence (modeled estimates only). |
| `NLNET_PROPOSAL_DRAFT.md` | Prior draft; license entries superseded by this package. |

## Appendix B — Honesty Checklist (zero-hallucination self-audit)

- [x] No claim that the grant is awarded.
- [x] Every UNVERIFIED item (V9, V10, V11) explicitly flagged.
- [x] Verified facts cite workspace primary sources.
- [x] Draft's MIT licenses corrected to AGPL-3.0/CC-BY per stated plan.
- [x] `rt_safety_audit.py` disclosed as regex-based, not full AST.
- [x] Part-time/solo maintainership disclosed (§8, §10).
- [x] Budget labeled indicative; final award set by NLnet.
- [x] Proprietary pipeline explicitly out of scope.

---

*End of proposal package. Prepared under GrantHermes `grant-pipeline` Phase 4 governance. Not submitted; not awarded.*
