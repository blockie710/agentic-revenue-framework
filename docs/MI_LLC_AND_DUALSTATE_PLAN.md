# MI LLC Formation Funding Plan + MI/CA Dual-State Tax Feasibility
**Prepared:** 2026-08-17 · **Governance:** CoFounderHermes (entity strategy) + GrantHermes (non-dilutive) + verified primary tax sources
**Correction note:** earlier estimate of "$300–$500" LLC cost was WRONG. Actual MI cost ~$100 (verified by applicant). This doc uses the correct figure.

---

## PART A — MI LLC Formation: Raising ~$100 (corrected)

### Actual cost breakdown (Michigan)
| Item | Cost | Cadence |
|---|---|---|
| Articles of Organization filing | $50 | one-time |
| DBA (assumed name) | $20 | one-time |
| Registered agent | $50 | per year |
| **Total to form + Year 1** | **~$120** ($70 one-time + $50/yr) | |

No legal fees required for a solo single-member LLC filed via LARA online.

### Funding path (no dilution, no pre-capital raise)
The LLC is cheap enough that **agent-driven revenue primes it directly** — no external raise:

1. **picoads monetize_link (LIVE now):** provide one URL you'd recommend anyway →
   tracked link → first conversion settles USDC to EVM `0x34F9…feac`. One
   $20–$50 commission covers the registered agent; 2–3 cover full formation.
2. **GitHub Sponsors (ELIGIBLE, free):** enable on OSS repos; compounds toward
   the recurring $50/yr.
3. **NLnet NGI0 (ELIGIBLE, reopens 2026-09-03, €10–50k):** the real capital
   event — but ~2 months out. Use picoads in the interim.
4. **hunazo ($60 listing live):** blocked on 401 auth — not a near-term contributor
   until signature-header contract resolved.

**Verdict:** ~$120 is coverable from the first 1–2 picoads conversions. Form the
LLC the moment picoads pays out (or self-fund $120 from personal; recoverable in
week 1 of agent revenue). No grant needed for formation.

---

## PART B — MI + CA Dual-State / Split-Residency Tax Feasibility

### Primary-source findings
| Source | Rule established |
|---|---|
| FTB.ca.gov (Part-year/Nonresident) | CA resident = taxed on **worldwide** income. Nonresident = only **CA-source** income. Part-year = split by period. Safe harbor for domiciled-CA persons away under employment contract (FTB Pub 1031). |
| CA tax guide (linked to FTB forms) | **CA does NOT disregard single-member LLCs** for the **$800 min franchise tax** + **$900+ LLC fee** (based on total CA gross receipts, not profit). $800 due first partial year; temporary waiver for entities formed ≥2021 is unreliable. |
| Michigan | Flat **4.25%** personal income tax; part-year residents allocate income by residency period. **No franchise/LLC entity tax.** |

### Feasibility assessment

**Q: Can you operate across MI + CA with a split-residency plan?**
- **Residency:** If domiciled in MI and temporarily in CA under a contract, CA
  safe harbor (FTB Pub 1031) can preserve nonresident status → avoids CA
  worldwide-income tax. If you establish CA domicile, you're a CA resident
  taxed on worldwide income (bad for an agentic business with nonlocal income).
- **Entity location is the lever, not residency alone:** Forming the LLC in **MI**
  avoids CA's $800/yr + receipt-based fee entirely. A CA-formed LLC imposes
  those fees **regardless of where you live** (CA doesn't disregard SMLLCs).

**Recommendation (zero-hallucination, flagged constraints):**
1. **Form LLC in MICHIGAN.** No franchise tax; only $50/yr registered agent.
2. **Maintain MI domicile** as primary; treat any CA time as nonresident
   (document stay duration, keep MI driver license/registration/vote).
3. **If CA presence is required:** rely on FTB Pub 1031 safe harbor; ensure
   income is **not** CA-sourced (services performed remotely for a non-CA
   entity = generally non-CA-source). Keep written records.
4. **Do NOT form a CA LLC** unless you actually operate a CA-sourced business
   there — the $800 + fee is a pure drag.

### Risks / caveats (flagged UNVERIFIED)
- Exact CA SMLLC fee tiers for 2026 not re-quoted from FTB form 3522/568 this
  session — confirm current year before any CA formation. **UNVERIFIED.**
- MI/CA reciprocal agreement and specific day-count thresholds (FTB Pub 1031)
  not fully parsed — engage a CA-licensed CPA before executing split-residency.
  **This analysis is not tax advice.**
- "Split residency" is not a formal status — you are resident of ONE state and
  nonresident/part-year of the other. Plan accordingly.

---

## PART C — Execution Sequence
1. **Now:** Enable GitHub Sponsors; provide a URL for picoads monetize_link.
2. **On first picoads payout (~$50–$120):** File MI LLC (LARA online) + DBA.
3. **2026-09-03:** Submit NLnet proposal (drafted: NLNET_PROPOSAL_DRAFT.md).
4. **Post-entity:** STTR + STF unlock; CA safe-harbor residency maintained.
5. **CPA consult** before any CA domicile change or CA LLC formation.

*All cost/tax figures are planning estimates from primary sources cited above;
verify current-year amounts with MI LARA and a CA-licensed CPA before filing.*
