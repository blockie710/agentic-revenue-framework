#!/usr/bin/env python3
"""On-chain payment client (picoads / hunazo / justpayai). Stub.
Real run: poll matches/orders, deliver, settle USDC to EVM wallet.
Mirrors the proven a2a-wallets/picoads_poller.py logic.
"""
def poll_matches(agent_id: str) -> list:
    """Stub: return pending matches for an agent. Real: GET /agents/{id}/matches."""
    return []

if __name__ == "__main__":
    print(poll_matches("0x34F93134dFb4d62e0fbb9833819d084B361dfeac"))
