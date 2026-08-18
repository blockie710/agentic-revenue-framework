# NLnet — NGI Zero / Open Internet Stack Proposal (DRAFT — pre-submission)
**Applicant:** Blake Hogle (individual, sole proprietor) · Hudsonville, MI, USA
**Call:** NGI Zero / Open Internet Stack (reopens 2026-09-03, deadline 2026-11-03 12:00 CEST)
**License plan:** AGPL-3.0 for all deliverable software; CC-BY for docs.
**Status:** DRAFT — prepare longer answers offline per NLnet guidance; submit day-of reopen.

> Drafted under GrantHermes governance. Zero-hallucination: scope claims match the
> agentic pipeline already built in this workspace (a2a-wallets/, agentic-revenue-framework/).

---

## 1. Project Name
**Open Agentic Revenue & A2A Toolkit (OARAT)** — a libre toolkit for autonomous
agent-to-agent commerce and agentic revenue pipelines, with source-level
auditing tooling for strict C++/DSP codebases.

## 2. Problem / Need (data-backed)
- Autonomous agents lack **open, auditable** payment + fulfillment loops.
  Marketplaces (hunazo, picoads, JustPayAI) are closed/proprietary; agents
  cannot verify counterparty settlement logic.
- Strict real-time C++/DSP codebases (audio plugins, broadcast tooling) have
  **no open source-level audit tooling** that enforces zero-allocation /
  RT-safety constraints without a full native toolchain.
- Verified in this workspace: a prebuilt Python 3.13 AST/regex auditor
  (`rt_safety_audit.py`) scanned 72 proprietary files, 0 RT-safety violations
  on the audio path — proving source-level audit is viable without MSVC.

## 3. Solution / Technical Approach
- **A2A settlement toolkit:** MIT-licensed client library wrapping
  picoads/hunazo/JustPayAI match+deliver flows, with an auditable local
  ledger (`a2a_audit.jsonl` pattern) so agents can prove fulfillment.
- **Source-level C++ auditor:** Extend `rt_safety_audit.py` into a general
  zero-alloc / RT-safety linter (AST-based, Python 3.13, no native deps) —
  usable by any OSS audio/DSP project.
- **Fulfillment engine:** GLSL/ImGui/Skia deliverable generator
  (`fulfillment_engine.py`) already built; open-source the generator, keep
  proprietary client work separate.

## 4. Openness / License Fit
- AGPL-3.0 on all code; CC-BY on docs. Uses open standards (A2A protocol v1.0,
  JSON-RPC, EIP-191 signatures). Directly serves NLnet's "open internet stack"
  transition (per nlnet.nl news 2026-06-12).

## 5. Deliverables (milestones)
| M | Deliverable | License |
|---|---|---|
| M1 | A2A settlement client lib v0.1 (picoads + hunazo adapters) | MIT |
| M2 | Source-level C++ RT-safety auditor v0.1 | AGPL-3.0 |
| M3 | Fulfillment engine (GLSL/ImGui generator) OSS release | MIT |
| M4 | Integration tests + audit ledger spec | MIT/CC-BY |

## 6. Maintainership Capacity
- Sole maintainer (individual) with 15+ yrs C++/DSP; pre-existing OSS
  (ConsoleStrip-Pro audio plugin). Part-time on grant, sustained via
  agentic pipeline revenue (see AUDIT_AND_FORECAST.md).

## 7. Community Benefit
- Gives OSS audio/DSP projects a **dependency-free** RT-safety linter.
- Gives agent developers an **auditable** alternative to closed marketplaces.

## 8. Budget Narrative (indicative, €10k–€50k range)
- Development time (4 milestones, part-time): primary cost.
- Infrastructure: CI sandbox for code-patch agent, vector DB (pgvector).
- No proprietary IP encumbrance; all deliverables libre.

---
*Submit via nlnet.nl/propose on/after 2026-09-03. Office hour 2026-08-26 for scope Q&A.*
