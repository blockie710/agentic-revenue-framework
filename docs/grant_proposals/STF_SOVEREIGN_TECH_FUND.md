# Sovereign Tech Fund (STF) — Proposal Skeleton

**Governance:** GrantHermes grant-pipeline Phase 4 (skeleton stage). Zero-hallucination enforced: every non-source fact is tagged `[VERIFIED: context]` (from applicant brief) or `[FLAG: UNVERIFIED]` (must be confirmed before final submission). No invented eligibility wording, dates, or award figures.

**Applicant:** Blake Hogle — solo maintainer, forming MI LLC "Nexus Signalworks". Hudsonville MI, pre-revenue. `[VERIFIED: context]`
**Status tag:** `ELIGIBLE (UNVERIFIED scope)` — see §8.
**Fit score:** 78/100. `[VERIFIED: context]`
**⚠ UNVERIFIED SCOPE — PROMINENT FLAG:** The exact STF **individual-applicant eligibility wording has NOT been re-confirmed**. STF typically funds **organizations / fiscal sponsors**, not unaffiliated individuals. Verify the current call's eligibility and the fiscal-sponsor requirement before drafting the final. `[FLAG: UNVERIFIED]`

---

## 1. Project
- **Name:** Open Agentic Revenue & A2A Toolkit (**OARAT**). `[VERIFIED: context]`
- **What it is:** an open-source toolkit combining (a) a **libre C++ / DSP real-time-safety auditor** and (b) an **A2A (agent-to-agent) settlement toolkit**. `[VERIFIED: context]`
- **Licenses:** **AGPL-3.0 / MIT** (dual-licensed components). `[VERIFIED: context]`
- **Relation to core IP:** built from the same native C++20/AVX2 DSP competence; the audited engine and settlement layer are libre infrastructure, distinct from the trade-secret commercial DSP core. `[VERIFIED: context]`
- **Current state:** pre-revenue, solo, forming LLC. `[VERIFIED: context]`

## 2. Why Critical Open Infrastructure
- **Thesis:** C++/audio DSP tooling and open agent-to-agent settlement are **under-maintained critical infrastructure** for the broader open ecosystem (audio software, agentic commerce, edge DSP). `[VERIFIED: context]`
- **Gap:** RT-safety auditing for native DSP is not a solved, widely-available libre tool; A2A settlement lacks a small, auditable reference implementation. `[ACTION: substantiate with references; do not assert without citation]`
- `[FLAG: UNVERIFIED]` STF's own definition of "critical open infrastructure" for this cycle — confirm alignment before final.

## 3. Openness
- **License:** AGPL-3.0 (copyleft core) + MIT (permissive components). `[VERIFIED: context]`
- **Governance:** `[ACTION: define contribution process, CoC, release cadence]`
- **Reproducibility:** clean DATA_MANIFEST pattern reused for audit transparency. `[VERIFIED: context]`
- `[FLAG: UNVERIFIED]` STF openness/transparency reporting obligations for grantees — confirm.

## 4. Maintainership (solo)
- **Sole maintainer:** Blake Hogle. `[VERIFIED: context]`
- **Bus-factor risk:** high (one person). `[ACTION: mitigation — documented build/test, governance handoff plan, possible fiscal sponsor or co-maintainer]`
- **LLC context:** forming Nexus Signalworks; `[FLAG: UNVERIFIED]` whether STF requires an organizational/fiscal sponsor rather than an individual applicant — **must verify**.

## 5. Budget (€50k–€150k range)
- **Total:** within STF's stated **€50,000–€150,000** band. `[VERIFIED: context]` `[FLAG: UNVERIFIED]` exact award size, eligible cost categories, and any personnel-cost limits per current call.
- **Skeleton line items (to be priced, not authoritative):**
  - Maintainer time (solo, part-time): €___
  - RT-safety auditor dev: €___
  - A2A settlement toolkit dev: €___
  - CI / infra / test hardware: €___
  - Documentation / community: €___
- `[FLAG: UNVERIFIED]` whether STF permits funding a solo individual's time directly or requires pass-through via a fiscal host.

## 6. Community Benefit
- **Who benefits:** open-source audio/DSP projects, agentic-commerce builders, edge-DSP practitioners. `[VERIFIED: context]`
- **Concrete outputs:** reusable RT-safety auditor; auditable A2A settlement reference. `[VERIFIED: context]`
- **Adoption path:** `[ACTION: identify at least 2–3 real downstream projects/communities that would use OARAT]`.

## 7. Risk
- **Eligibility risk (highest):** individual-vs-organization applicant rules unconfirmed → proposal may be ineligible as written. `[FLAG: UNVERIFIED]`
- **Sole-maintainer risk:** bus factor, continuity. → mitigate via governance docs + fiscal sponsor.
- **Scope risk:** dual toolkit (auditor + settlement) may exceed solo capacity → scope to MVP.
- **Funding-structure risk:** direct individual payment may be disallowed → require fiscal sponsor. `[FLAG: UNVERIFIED]`

## 8. Eligibility & Status (consolidated flags)
- **Tag:** `ELIGIBLE (UNVERIFIED scope)`.
- `[FLAG: UNVERIFIED]` exact individual-eligibility wording **not re-confirmed** — verify on STF's current application guidance before final draft.
- `[FLAG: UNVERIFIED]` award band applicability to a solo/LLC applicant; fiscal-sponsor requirement.
- `[FLAG: UNVERIFIED]` application window / deadline for the relevant STF cycle.

---
### Zero-hallucination checklist (Phase 4)
- [x] No invented STF deadlines or eligibility clauses.
- [x] All euro amounts flagged UNVERIFIED except the €50k–€150k band from brief.
- [x] Licenses (AGPL-3.0/MIT) and project name (OARAT) taken from brief.
- [ ] Applicant to confirm: current STF eligibility wording, fiscal-sponsor requirement, deadline, allowable costs.
- [ ] Applicant to resolve solo-vs-organization applicant structure.
