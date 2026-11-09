# Microsoft for Startups Founders Hub — Application Package

**GrantHermes Phase 4 (accelerator/OSS artifact) · ZERO-HALLUCINATION**
**Eligibility tag:** ✅ ELIGIBLE · **Fit score:** 92/100 · **Non-dilutive:** Yes (no equity, no funding requirement)

---

## 1. Program Snapshot (verified)
- **What it is:** Microsoft for Startups Founders Hub — free program, no equity taken, no funding/referral required, idea-stage founders accepted.
- **Benefits:** Up to **$150,000** in Azure credits, GitHub Enterprise, OpenAI credits, and Microsoft 365 (E5) licenses.
- **Apply URL:** https://foundershub.microsoft.com (entry also via https://www.microsoft.com/en-us/startups)
- **Source of truth:** learn.microsoft.com/en-us/startups/microsoft-for-startups/application

## 2. Applicant & Company Overview
- **Founder:** Blake Hogle (GitHub/handle: `blockie710`)
- **Entity:** Nexus Signalworks — currently **sole proprietor**, forming a **Michigan LLC ~2026-09-03** (Hudsonville, MI)
- **Stage:** Pre-revenue, solo, deep-tech
- **Focus:** C++20 / AVX2 real-time DSP, audio plugin + broadcast systems, AI R&D

## 3. Product Description
A **native, zero-allocation C++20 / AVX2 DSP engine** with an AI-assisted preset layer, shipping as **VST3 / AU / AAX** plugins. Deliberately **anti-Electron** — all signal processing is hand-written native SIMD code with deterministic, allocation-free audio paths. Alongside the commercial engine, the founder builds open-source agentic-revenue tooling (see GitHub Sponsors package) and the ConsoleStrip-Pro audio plugin.

## 4. What the Credits Will Be Used For
1. **Build & test the AI-assisted preset engine** — Azure compute for model-assisted preset generation, embedding/retrieval experiments, and inference evaluation against the native DSP layer.
2. **CI / build infrastructure for the DSP engine** — GitHub Actions + Azure-hosted runners to compile, fuzz, and benchmark the C++20/AVX2 codebase across Windows/macOS, plus artifact storage for plugin installers.
3. **OpenAI credits** — prototyping the preset-assist UX and agentic tooling.
4. **M365 E5** — operations, email, and document tooling for the forming LLC.

## 5. Why Fit (92/100)
- Idea-stage and pre-revenue are explicitly accepted — no VC funding or shipped product required.
- Deep-tech AI + native DSP maps directly to Azure AI / OpenAI credit use cases.
- CI-for-native-builds is a textbook Azure workload.
- Non-dilutive, founder-friendly, no equity — matches the agentic-revenue, own-your-infra thesis.

## 6. Exact Apply Steps
1. Create/sign in with a **personal Microsoft account** (Outlook/Hotmail/Live) that has **no prior Azure subscription** and has **not previously received > $10,000 in Azure credits**.
2. Go to **https://foundershub.microsoft.com** → "Apply" / "Join".
3. Register the **startup name** — must match your legal documents (use "Nexus Signalworks"; if LLC not yet filed, enter the intended legal name and update later — see flag below).
4. Provide founder details (Blake Hogle, `blockie710`), location (Hudsonville, MI, USA), and a short company/product description (use §3 above).
5. Select technical focus areas (AI / ML, Developer Tools) and intended Azure use (§4).
6. Submit; typical review is fast for idea-stage accounts. On approval, activate Azure credits and GitHub Enterprise from the Founders Hub dashboard.

## 7. ⚠️ LLC Flag (read before applying)
- Founders Hub **accepts idea-stage founders without a formal entity** — you can apply now as an individual / very-early founder.
- An **LLC is helpful but not strictly required** at apply time. Because the MI LLC is targeted for **~2026-09-03**, you may apply immediately using the intended legal name "Nexus Signalworks" and update entity details once the LLC is filed.
- Keep the registered startup name consistent with legal documents to avoid later verification friction.

---
*Prepared by GrantHermes Phase 4. All program facts verified against Microsoft documentation; applicant facts sourced from the grant brief. No figures invented.*
