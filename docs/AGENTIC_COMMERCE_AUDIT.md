# Agentic Commerce & Revenue Avenues — Skill/Tool Audit
**Prepared:** 2026-08-18 · **For:** Blake Hogle (pre-revenue solo, MI, non-dilutive only)
**Scope:** All installed skills + deferred tools that can earn or move money autonomously.

## TL;DR
- **Real-money rails that work today (you have accounts/keys):** Amazon Associates (live), picoads (wallet bound, `monetized:false`), clawpump (1 USDC), hunazo (bug confirmed theirs, fix deployed → retry).
- **Real-money rails NOT yet set up:** Stripe, Kit (mcp-kit), JustPayAI (API DOWN per memory), bankofbots, theagora, allowance (needs your phone).
- **Virtual-credit only (NOT real money):** clawdwork, friendzone, clawdsin, agentoctopus (router), deaddrop/claweb/agentdo (agent messaging — no payout).
- **Highest-leverage for the $50 LLC crunch:** Amazon Associates hardware sale (done — need posts) + Stripe/Kit for a paid productized service (e.g. C++20 audit pack).

## Category 1 — Real-Money Marketplaces (you sell, get USDC/fiat)
| Skill | Payout | Status | Eligibility |
|---|---|---|---|
| **Amazon Associates** | Affiliate $ (fiat) | ✅ LIVE (StoreID blockie71009-20) | You post tagged links; 3 sales/180d to stay active |
| **picoads** | USDC on Base | ⚠️ wallet bound, `monetized:false` | Need advertiser match; low yield so far |
| **clawpump** | SOL (token fees) | ⚠️ 1 USDC in account | Gasless launch; 65% of trading fees; speculative |
| **hunazo** | USDC on Base (x402) | 🟡 FIXED (their bug) — retry after deploy | 2% fee; support confirmed GET-auth bug, no change needed on your end |
| **JustPayAI** | USDC on Solana | ❌ API DOWN (per memory) | Was $1 activate + 3% fee; currently unreachable |
| **theagora** | USDC (escrow) | ⚠️ not set up | A2A service commerce; $50 free credit on register |
| **Stripe (mcp)** | Fiat | ⚠️ not set up | Best for selling a productized service |
| **Kit / mcp-kit** | Fiat | ⚠️ not set up | Digital products, newsletters, tip jars |

## Category 2 — Credit / Financing (non-dilutive capital)
| Skill | What | Status | Note |
|---|---|---|---|
| **bankofbots** | USDC loans on BOB Score | ⚠️ not set up | Non-custodial; needs `BOB_API_KEY`+`BOB_AGENT_ID`; builds credit from payment proofs |
| **allowance** | Virtual card, human-approval purchases | ⚠️ needs phone + browser session | Not for earning; for spending on your behalf |

## Category 3 — Agent-to-Agent Messaging / Networks (no direct payout, enable collaboration)
| Skill | Type | Real money? |
|---|---|---|
| **agentdo** | Task queue (pick up/post work) | No payout in skill (external) |
| **deaddrop** | Agent discovery + messaging | No |
| **claweb** | Federated agent mail/chat | No |
| **friendzone** | Private agent groups (virtual tokens) | No (game tokens) |
| **agentoctopus** | Skill router (not commerce) | No |
| **clawdsin** | Agent pro network (Claw Score) | No |
| **agentwell** | Wellness/cognition API | No (ops) |

## Category 4 — Spend Tracking / Governance
| Skill | Use |
|---|---|
| **payrail402** | Cross-rail spend tracking (visa/mc/stripe/x402/ach) — control plane |
| **agentwell cost_guard** | Token-spend guardrails |

## Recommended Activation Order (given $50 LLC crunch + non-dilutive constraint)
1. **Amazon Associates** — already live. Post the 7-day X calendar (drafted) + Reddit/Discord. 2 hardware sales = $50. (HIGHEST priority, zero setup.)
2. **Stripe or Kit** — set up to sell a productized service (e.g. "C++20 zero-alloc audit pack" at $49). Converts your audit skill into recurring fiat. Needs a verified domain (Kit) or Stripe acct.
3. **hunazo** — support confirmed it was their prod GET-auth bug (now fixed); retry the original `/orders` request after deploy. No email send needed. $60 listing unblocked once it returns 200.
4. **theagora / JustPayAI** — list a "C++ audit" or "DSP consulting" service for USDC once set up (JustPayAI API must come back up).
5. **bankofbots** — only after you have real payment proofs; builds loan eligibility as a backstop, not day-1.

## What I will NOT do (guardrails)
- No fake reviews, no cookie-stuffing, no buying through my own Associate link.
- No moving your Coinbase/clawpump funds without explicit instruction.
- No claiming "earned" until a verifiable payout/settlement confirms it.
- Virtual-credit skills (clawdwork etc.) are reputation only — I won't present them as revenue.
