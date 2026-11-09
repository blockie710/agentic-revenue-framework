# DoD SBIR/STTR — Signal Classification Proposal Skeleton

**Governance:** GrantHermes grant-pipeline Phase 4 (skeleton stage). Zero-hallucination enforced: every non-source fact below is tagged `[VERIFIED: context]` (provided by applicant brief) or `[FLAG: UNVERIFIED]` (must be confirmed before final submission). No invented deadlines, amounts, topic numbers, or citations.

**Applicant:** Blake Hogle — forming MI LLC **"Nexus Signalworks"** (target formation 2026-09-03) + EIN + SAM UEI. Solo, Hudsonville MI, pre-revenue. `[VERIFIED: context]`
**Status tag:** `CONDITIONAL` — submission blocked until MI LLC + EIN + SAM UEI exist.
**Fit score:** 80/100. `[VERIFIED: context]`

---

## 0. PRE-SUBMISSION ADVISORY (read first)
- **Pick ONE topic and match before writing.** The brief lists two candidate topics. Do NOT write a merged proposal. Choose either:
  - (A) **Army AI/ML Open Topic** `[VERIFIED: context]`
  - (B) **DARPA "Signal Classification & Anomaly Detection in Contested Spectral Environments"** — topic open **Aug 26 2026** `[VERIFIED: context]`
- `[FLAG: UNVERIFIED]` exact per-topic award amounts and the **DARPA close date** are NOT confirmed in the brief. Confirm on SAM.gov / Grants.gov / the specific BAA before finalizing.
- SBIR Phase I: **~$140K–$275K / 6–12 mo**, **no cost-share**. `[VERIFIED: context]` (per-topic figures still `[FLAG: UNVERIFIED]`).
- Company must be U.S.-owned, small, and registered in SAM with a UEI before submission. The LLC is **not yet formed** — this is the gating dependency. `[VERIFIED: context]`

---

## 1. Executive Summary
- **One-paragraph problem statement:** contested/denied spectral environments degrade classification accuracy of conventional cloud-bound or general-purpose DSP stacks.
- **Proposed solution:** a native, **zero-allocation C++20 AVX2 DSP engine** plus an AI-assisted preset layer, **real-time-safe**, **on-device/edge**, **no cloud dependency** (security/ISR advantage). Anti-Electron native ImGui/Skia front-end. `[VERIFIED: context]`
- **Core IP posture:** hand-tuned native DSP is the protected asset (trade-secret); AI is an acceleration feature only; **clean DATA_MANIFEST** supports reproducibility/audit. `[VERIFIED: context]`
- **Ask:** Phase I placeholder (see §5). **Dual-use** path: defense + commercial edge-DSP.
- **Why now:** topic opens Aug 26 2026 (DARPA candidate). `[VERIFIED: context]`

## 2. Technical Approach (map to topic gap)
- **Topic selected:** (A) Army AI/ML Open Topic / (B) DARPA contested-spectral `[ACTION: choose one]`
- **Topic gap statement:** `[ACTION: insert 2–3 sentences drawn directly from the chosen BAA/topic language]`
- **Technical mapping:**
  - Native zero-alloc C++20 AVX2 DSP → deterministic, low-jitter per-frame classification suitable for **low-power/edge** platforms. `[VERIFIED: context]`
  - **No-cloud-dependency** → on-device inference eliminates exfiltration/link-dependency risk = **security angle**. `[VERIFIED: context]`
  - AI-assisted preset layer → accelerates operator tuning without replacing the DSP core. `[VERIFIED: context]`
  - Real-time-safe scheduling + ImGui/Skia thin UI → field-deployable, no Electron attack surface. `[VERIFIED: context]`
- **Innovation claim:** (text) — must be defensible and non-speculative.
- `[FLAG: UNVERIFIED]` specific evaluation metrics / MOS / false-alarm targets must come from the topic's stated objectives.

## 3. Phase I Plan + Milestones
- **Duration:** 6–12 months (per-topic). `[VERIFIED: context]` `[FLAG: UNVERIFIED]` exact month count.
- **Milestones (skeleton — fill with real deliverables):**
  - M1 (Mo __): LLC/EIN/UEI secured; build pipeline stood up.
  - M2 (Mo __): zero-alloc DSP kernel baseline + RT-safety harness.
  - M3 (Mo __): on-device classification demo (edge target __).
  - M4 (Mo __): AI preset layer integrated; DATA_MANIFEST validated.
  - M5 (Mo __): interim report + go/no-go for Phase II.
- **Deliverables:** `[ACTION: map to topic's Phase I deliverable list]`

## 4. Commercialization (dual-use)
- **Defense pull:** on-device signal classification under contested-spectrum / comms-denied conditions. `[VERIFIED: context]`
- **Commercial push:** edge DSP for audio/RF/industrial monitoring; licensing of native engine; anti-Electron tooling. `[VERIFIED: context]`
- **IP strategy:** DSP core as trade-secret; clean DATA_MANIFEST enables audit/licensing. `[VERIFIED: context]`
- **Revenue path:** `[ACTION: insert realistic plan; pre-revenue today]`

## 5. Budget (PLACEHOLDER — UNVERIFIED)
- **Phase I total: ~$275K placeholder.** `[FLAG: UNVERIFIED]` — exact amount depends on chosen topic; confirm per-topic ceiling on the BAA.
- **Suggested skeleton line items (to be priced, not authoritative):**
  - Personnel (PI, solo +可能的 subcontract/consultant): $___
  - DSP engine development: $___
  - AI preset layer + DATA_MANIFEST tooling: $___
  - Edge hardware / test assets: $___
  - Overhead / indirect: $___
- **No cost-share required.** `[VERIFIED: context]`
- `[FLAG: UNVERIFIED]` indirect rate, allowable costs per FAR/DFARS — confirm with an SBIR accountant.

## 6. Team
- **PI / Sole proprietor:** Blake Hogle — native C++20/AVX2 DSP, real-time signal processing, on-device AI inference. `[VERIFIED: context]`
- **Gaps:** `[ACTION: list — e.g., no dedicated QA, no military sponsor yet, solo bandwidth]` → mitigation: consultant / STTR partner if topic permits.
- `[FLAG: UNVERIFIED]` whether an STTR (requires research institution partner) is required for the chosen topic — verify; SBIR does not.

## 7. Risk
- **Gating risk (highest):** LLC + EIN + SAM UEI not yet established → submission impossible until resolved. `[VERIFIED: context]`
- **Sole-founder bandwidth** vs. Phase I scope → mitigate via scoped MVP + consultant.
- **Topic mismatch** if proposal not rewritten to ONE topic → mitigate per §0 advisory.
- **Technical:** RT-safety proofs on target edge silicon `[ACTION: validate early]`.
- `[FLAG: UNVERIFIED]` program-specific evaluation criteria not yet pulled from BAA.

---
### Zero-hallucination checklist (Phase 4)
- [x] No invented DARPA/SBIR close dates.
- [x] All dollar figures flagged UNVERIFIED except "no cost-share" and range from brief.
- [x] Topic selection deferred to applicant (one topic only).
- [ ] Applicant to confirm: DARPA close date, per-topic amount, BAA evaluation criteria, STTR vs SBIR requirement.
- [ ] Applicant to form LLC/EIN/UEI before submission (CONDITIONAL gate).
