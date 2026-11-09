<!--
================================================================================
GrantHermes Pipeline — PHASE 4 ARTIFACT (Government / Foundation)
--------------------------------------------------------------------------------
Solicitation : NSF 26-510 — SBIR/STTR Phase I/II, "Developing Deep Technologies
               that Advance U.S. Competitiveness and Security"
Applicant    : Blake Hogle  (currently sole proprietor; forming
               "Nexus Signalworks, LLC" — MI LLC, target filing 2026-09-03)
Location     : Hudsonville, MI, United States
Artifact Tag : CONDITIONAL  — clears upon: (1) MI LLC filed,
               (2) EIN issued, (3) SAM.gov UEI active
Fit Score    : 88 / 100
Created      : 2026-08-18
Zero-Hallucination Governance:
   [VERIFIED]    confirmed against official source during drafting
   [UNVERIFIED]  must be confirmed by applicant on sbir.gov / official portal
   [ESTIMATE]    skeleton planning figure — adjust before submission
   [APPLICANT]   founder-supplied fact — fill in from records
================================================================================
-->

# NSF SBIR Phase I Proposal Skeleton — Nexus Signalworks, LLC
**"On-Device, Zero-Allocation C++20/AVX2 DSP Engine with an AI-Assisted Preset/Parameter-Analysis Layer for Pro-Audio and Low-Latency Broadcast"**

> **STATUS: CONDITIONAL.** This skeleton is submission-ready in structure but is **gated** on entity formation. NSF requires the applicant to be a U.S. small business at submission. Until "Nexus Signalworks, LLC" is filed in Michigan with an active EIN and SAM.gov UEI, submit under the sole proprietorship **only if it meets the small-business test** — otherwise hold submission until formation completes (target 2026-09-03). See §10 Compliance.

---

## Verification Legend (read first)
| Symbol | Meaning |
|--------|---------|
| `[VERIFIED]` | Confirmed against NSF 26-510 / sbir.gov during drafting |
| `[UNVERIFIED]` | Applicant must confirm on sbir.gov before submission |
| `[ESTIMATE]` | Skeleton planning number; replace with actuals |
| `[APPLICANT]` | Supply from company records |

---

## §1. Executive Summary
**Applicant.** Blake Hogle, solo founder (Hudsonville, MI), forming *Nexus Signalworks, LLC*. Deep expertise in C++20, AVX2 SIMD, real-time DSP, and broadcast audio systems. Pre-revenue.

**Problem.** Pro-audio and broadcast toolchains are dominated by (a) cloud-dependent GenAI features that add network latency, create data-liability exposure, and break real-time constraints, and (b) Electron-based plugin UIs that violate real-time-safe, lock-free audio-thread discipline.

**Solution.** A native, **zero-allocation C++20 / AVX2 SIMD DSP engine** with a thin **AI-assisted preset/parameter-analysis layer** that runs **on-device** (no cloud). Targets VST3 / AU / AAX plugin formats and low-latency broadcast streaming. The engine is real-time-safe and lock-free; the UI is native ImGui/Skia (anti-Electron).

**Core IP posture.** The DSP core is **hand-tuned native signal processing** protected as **trade secret + copyright** — *not* a trained GenAI model. AI is used **only** as an acceleration / preset-analysis feature. A **DATA_MANIFEST** tracks all training-data provenance, and an **AI-Use Governance Policy + OA AI clause** is adopted, making the AI layer liability-free and auditable. `[APPLICANT: attach both documents as appendices]`

**Ask.** NSF SBIR Phase I — **$275,000** `[ESTIMATE; see §6 ceiling note]` for a **6-month** `[VERIFIED: NSF permits 6–18 mo]` R&D effort validating technical merit and commercial feasibility, with a Phase II path to $1.75M / 24 months. `[UNVERIFIED: confirm Phase II ceiling on sbir.gov]`

**Why NSF Deep Technologies (26-510).** The work is a deep, hard-tech, on-device compute advance (real-time-safe SIMD DSP + on-device ML inference for audio) with clear U.S. competitiveness and security relevance (sovereign, on-premise audio IP; no foreign-cloud dependency).

---

## §2. Project Description

### 2.1 Technical Merit & Feasibility
- **Zero-allocation real-time core.** All audio-callback paths are allocation-free and lock-free; state is pre-allocated at load. This is the foundational feasibility claim and the principal differentiator from GC/Electron stacks. `[APPLICANT: cite measured worst-case jitter/buffer-underrun results from prototype]`
- **AVX2 SIMD DSP kernels.** Hand-written C++20 SIMD kernels for the core transforms (EQ, dynamics, convolution/IR, spectral); copyrightable source + trade-secret tuning coefficients. `[APPLICANT: list kernel inventory + benchmark vs scalar baseline]`
- **On-device AI preset/parameter-analysis layer.** A small, locally-run model (no cloud) that analyzes parameter spaces / suggests presets. Bounded scope: inference only; no training of generative models by the firm. Clean **DATA_MANIFEST** documents every training artifact. `[APPLICANT: specify model family, footprint, latency budget]`
- **Plugin + broadcast targets.** VST3 / AU / AAX wrappers sharing one engine; a low-latency streaming path for broadcast. Common real-time-safe HAL. `[APPLICANT: name host DAWs / streaming targets to be validated]`
- **Native UI (anti-Electron).** ImGui + Skia rendering, no web runtime in the audio process. `[APPLICANT: screenshot/architecture diagram]`

### 2.2 Novelty & Differentiation
| Axis | Cloud-GenAI incumbents | Nexus Signalworks |
|------|------------------------|-------------------|
| Latency | Network round-trip | On-device, real-time-safe |
| Data liability | Training/scoring in cloud | Clean DATA_MANIFEST, on-prem |
| Real-time safety | Breaks audio thread | Zero-alloc, lock-free |
| UI | Electron (heavy) | Native ImGui/Skia |
| Core IP | Model weights | Hand-tuned DSP (TS+copyright) |

**Novelty statement.** First `[APPLICANT: justify "first"/claim scope]` integration of a zero-allocation AVX2 DSP core with an on-device, provenance-tracked AI preset layer that preserves real-time-safe, lock-free guarantees across VST3/AU/AAX and broadcast.

### 2.3 Commercial Potential
- **Market.** Pro-audio plugin market + broadcast audio-processing segment. `[UNVERIFIED: insert TAM/SAM/SOM with cited sources — do NOT estimate from memory]`
- **Customers.** Independent + studio audio engineers; plugin developers (license the engine); broadcasters needing low-latency, on-prem processing.
- **Channel.** KVR Audio, ADC (Audio Developer Conference), direct developer relations. See §5.

### 2.4 Results from Prior NSF Support
**None.** New company, pre-revenue, no prior federal support. `[APPLICANT: confirm no prior NSF awards under any entity]`

### 2.5 References
`[APPLICANT: add numbered citations — SIMD/DSP literature, VST3/AU/AAX SDK docs, on-device ML inference refs, market reports]`

---

## §3. Phase I Objectives
1. **O1 — Validate zero-alloc/lock-free core** at target block sizes with measured jitter < threshold. `[APPLICANT: define threshold]`
2. **O2 — Port + benchmark AVX2 kernels** vs scalar; document speedup + numerical equivalence.
3. **O3 — Stand up on-device AI preset layer** with a complete DATA_MANIFEST; demonstrate inference within real-time budget.
4. **O4 — Ship VST3/AU/AAX wrapper skeleton** + a broadcast streaming path; pass smoke validation in ≥2 hosts.
5. **O5 — De-risk commercialization**: customer-discovery interviews (≥ N) `[APPLICANT: set N]`, pricing model, GTM plan.
6. **O6 — IP + governance pack**: trade-secret register, copyright notices, AI-Use Governance Policy + OA AI clause finalized. `[APPLICANT: define "OA" acronym precisely]`

---

## §4. Work Plan, Milestones & 6-Month Timeline
**Period:** 6 months from award start `[VERIFIED NSF allows 6–18; this plan uses the minimum]`.

| Mo | Work Package | Milestone / Exit Criteria | Owner |
|----|--------------|---------------------------|-------|
| 1 | WP1 Core hardening | Zero-alloc allocator + lock-free queues; jitter bench | B. Hogle |
| 2 | WP2 SIMD kernels | AVX2 kernel set + equivalence tests | B. Hogle + consultant `[APPLICANT]` |
| 3 | WP3 On-device AI layer | Inference prototype + DATA_MANIFEST v1 | B. Hogle |
| 4 | WP4 Plugin wrappers | VST3/AU/AAX build; 2-host smoke pass | B. Hogle + subcontractor QA `[APPLICANT]` |
| 5 | WP5 Broadcast path + UI | Native ImGui/Skia UI; streaming latency demo | B. Hogle |
| 6 | WP6 Commercialization + IP | Customer discovery report, pricing, GTM; IP pack | B. Hogle |

**Milestones (go/no-go):** M1 end-Mo2 (kernel parity), M2 end-Mo4 (plugin builds in hosts), M3 end-Mo6 (Phase II decision package). `[ESTIMATE schedule — adjust]`

---

## §5. Commercialization Plan
- **Product.** Native DSP engine + plugin line + licensable SDK for developers.
- **Pricing.** `[APPLICANT/ESTIMATE: per-plugin tiered, SDK/site license, subscription for preset packs — define]`
- **GTM.** KVR Audio launch, ADC demo/poster, developer outreach, broadcaster PoC.
- **Phase II use of funds.** Scale engine to full product, expand format coverage, harden for broadcast certification. `[Ties to $1.75M/24mo — UNVERIFIED ceiling]`
- **Post-award leverage.** Pair with **Michigan ETF match** (see companion file) for non-dilutive upside.

---

## §6. Budget — Phase I (itemized, target $275,000)
> `[ESTIMATE]` figures. **NSF 26-510 Phase I ceiling is $305,000 inclusive of direct + indirect + TABA + optional I-Corps** `[VERIFIED]`. The $275K below is the conservative target from the pipeline; scale toward $305K if justified, and add TABA / optional I-Corps as separate authorized lines. Enter on the official NSF SBIR budget form.

| Line | Category | Amount (USD) | Note |
|------|----------|-------------:|------|
| 1 | PI salary — B. Hogle, 6 mo `[APPLICANT rate]` | 120,000 | `[ESTIMATE]` |
| 2 | Consultant — DSP/plugin dev, ~3 mo | 36,000 | `[ESTIMATE]` |
| 3 | Subcontract — independent QA / plugin validation lab | 24,000 | `[ESTIMATE]` |
| 4 | Equipment — dev workstations, audio I/O, measurement HW | 18,000 | `[ESTIMATE]` |
| 5 | Software/licenses — JUCE, analyzers, CI | 14,000 | `[ESTIMATE]` |
| 6 | Travel — customer discovery + ADC | 9,000 | `[ESTIMATE]` |
| 7 | Materials & supplies | 4,000 | `[ESTIMATE]` |
| 8 | Other direct — entity formation, IP filing, legal | 10,000 | `[ESTIMATE]` |
| 9 | Indirect (de minimis / negotiated rate) | 40,000 | `[ESTIMATE; confirm rate]` |
| | **TOTAL** | **275,000** | |

`[APPLICANT: attach NSF budget form; confirm indirect rate method; add TABA line if used]`

---

## §7. Key Personnel & Capability
| Role | Name | Commitment | Capability |
|------|------|-----------|------------|
| PI / Founder | Blake Hogle | **>50% of firm effort** `[VERIFIED requirement — see §10]` | C++20, AVX2 SIMD, real-time DSP, broadcast systems |
| Consultant (planned) | `[APPLICANT]` | Part-time | Plugin/FX engineering |
| QA subcontractor (planned) | `[APPLICANT]` | Milestone-based | Independent validation |

**Capability gap plan.** Solo founder → add consultant + QA subcontract in Phase I; Phase II hiring plan `[APPLICANT]`.

---

## §8. Facilities & Resources
- **Location.** Hudsonville, MI (home office / dedicated dev lab). `[APPLICANT: describe]`
- **Compute.** Build/CI farm, AVX2-capable workstations. `[APPLICANT: specs]`
- **Audio test rig.** Reference monitors, audio interfaces, measurement SW. `[APPLICANT]`
- **SDKs.** VST3/AU/AAX SDKs (licensing per manufacturer). `[APPLICANT: confirm access]`

---

## §9. Risk & Mitigation
| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Entity not formed by submission | Med | Hold to 2026-09-03 target; verify SAM UEI before submit |
| On-device AI exceeds real-time budget | Med | Bounded model; fall-back to heuristic preset analysis |
| Plugin wrapper host-compat failures | Med | Early 2-host smoke; external QA subcontract |
| Single-founder bandwidth | High | Consultant + scoped Phase I objectives |
| IP leakage pre-filing | Low | Trade-secret register + governance policy before disclosure |

---

## §10. SBIR-Specific Compliance Notes
- **U.S. small business.** Applicant must qualify at submission. Until LLC formed, confirm sole proprietorship meets SBA size/standard. `[UNVERIFIED — verify SBA test]`
- **PI employed >50% at the firm.** Blake Hogle is the founding PI and will devote >50% of personal effort to the firm during the project. `[VERIFIED requirement; APPLICANT: certify on forms]`
- **Project Pitch prerequisite.** NSF requires a **Project Pitch invitation** before a full proposal. `[VERIFIED]` — submit pitch well before the Nov 4, 2026 deadline. `[APPLICANT: track pitch status]`
- **SAM.gov UEI + registration.** Required for award. Formation target 2026-09-03 leaves margin before award admin. `[APPLICANT: confirm SAM registration timeline]`
- **No prior NSF support** → "None" section. `[APPLICANT: confirm]`
- **AI-use disclosure.** Declare AI-use scope (acceleration/preset-analysis only; not model training) + DATA_MANIFEST + governance policy in proposal appendices. `[APPLICANT: attach]`
- **Phase II ceiling** $1.75M/24mo — `[UNVERIFIED: confirm on sbir.gov]`.

---

## §11. Required NSF Forms / Submission Checklist
- [ ] SAM.gov UEI active (post LLC formation)
- [ ] Project Pitch invitation received `[VERIFIED prerequisite]`
- [ ] NSF SBIR Cover / proposal forms (Gov submission system)
- [ ] Project Summary (≤ prescribed limit)
- [ ] Project Description (§2; ≤ page limit per 26-510) `[UNVERIFIED: confirm page limit]`
- [ ] Budget form (§6) + justification
- [ ] Biographical sketch(es)
- [ ] Current & Pending Support ("None")
- [ ] Facilities/Equipment
- [ ] Data Management Plan (brief)
- [ ] References
- [ ] Letter of Support from MI ETF (optional but strengthens — see companion file)
- [ ] AI-Use Governance Policy + OA AI clause + DATA_MANIFEST (appendices)

**Deadline:** **November 4, 2026, 5:00 PM submitter's local time** `[VERIFIED]`. Recurring windows: 1st Thu Mar / 1st Wed Jul / 1st Wed Nov `[UNVERIFIED: verify Jul window — secondary sources cited Jul 27, 2026; reconcile on sbir.gov]`.

---

## §12. Open Items Before Submission (pre-sub gaps)
1. Confirm LLC filing + EIN + SAM UEI timeline vs 2026-09-03.
2. Define "OA AI clause" acronym precisely; finalize governance docs.
3. Populate `[APPLICANT]` technical metrics, benchmarks, diagrams.
4. Insert verified TAM/SAM/SOM with cited market sources.
5. Obtain Project Pitch invitation; schedule submission.
6. Reconcile NSF 26-510 Phase I ceiling ($305K) vs $275K target; finalize budget.
