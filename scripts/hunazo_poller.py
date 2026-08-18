#!/usr/bin/env python3
"""
hunazo_poller.py — autonomous order fulfillment for the hunazo Base marketplace.
Auth: wallet-signature challenge (GET /auth/challenge?wallet= -> sign -> X-Signature header).
Flow:
  1. GET /auth/challenge?wallet=EVM  -> message
  2. sign message with EVM private key (EIP-191)
  3. GET /orders?role=seller&status=paid  (with X-Signature) -> paid orders
  4. for each: build deliverable, POST /orders/{id}/fulfill {seller_wallet, tracking_info}

DRY_RUN=1 (default): list paid orders only, do not fulfill.
Private key read locally from wallet.evm.key, never transmitted.
"""
import os, sys, json, urllib.request, urllib.error
from dotenv_shim import load_env
HERE = os.path.dirname(os.path.abspath(__file__))
load_env(os.path.join(HERE, ".env"))
from eth_account import Account
from eth_account.messages import encode_defunct

DRY = os.environ.get("DRY_RUN", "1") == "1"
EVM = os.environ["EVM_WALLET_ADDRESS"]
AGENT = os.environ.get("HUNazo_AGENT_ID", "")
BASE = "https://hunazo.com"
UA = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "Accept": "application/json"}

with open(os.path.join(HERE, "wallet.evm.key")) as f:
    priv = f.read().strip()
acct = Account.from_key(priv)
assert acct.address.lower() == EVM.lower()

def api(method, path, body=None, sig=None, params="", auth=None):
    h = dict(UA)
    if sig: h["X-Signature"] = sig
    if auth: h.update(auth)
    data = json.dumps(body).encode() if body is not None else None
    url = BASE + path + params
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read().decode()

# 1. challenge
st, b = api("GET", "/auth/challenge", params="?wallet=" + EVM)
ch = json.loads(b)
print("[challenge]", st, str(ch)[:120])
msg = ch.get("message") or ch.get("challenge") or (ch.get("data", {}) or {}).get("message")
if not msg:
    print("No challenge message returned:", b[:200]); sys.exit(1)
ts = ch.get("timestamp")
# nonce is the trailing segment of the challenge message: agent-marketplace:<wallet>:<ts>:<nonce>
nonce = msg.rsplit(":", 1)[-1]
sig = acct.sign_message(encode_defunct(text=msg)).signature.hex()
print("[signed] len", len(sig))
auth_hdrs = {"X-Wallet": EVM, "X-Signature": sig, "X-Timestamp": str(ts), "X-Nonce": str(nonce)}

# 2. list paid orders for seller
st, b = api("GET", "/orders", params=f"?wallet={EVM}&status=paid", sig=sig, auth=auth_hdrs)
print("[orders]", st)
orders = json.loads(b) if b.strip().startswith(("[", "{")) else []
if isinstance(orders, dict):
    orders = orders.get("orders", orders.get("items", []))
print("paid orders:", len(orders) if isinstance(orders, list) else "n/a")

if not isinstance(orders, list) or not orders:
    print("No paid orders to fulfill. Done.")
    sys.exit(0)

from fulfillment_engine import build
for o in orders:
    oid = o.get("id") or o.get("order_id")
    print(f"  order {oid} -> fulfilling (dry={DRY})")
    if DRY:
        continue
    spec = {"type": "meter-glow", "palette": "neon", "target": "webgl", "order_id": oid}
    d, man = build(spec)
    st, b = api("POST", f"/orders/{oid}/fulfill",
                {"seller_wallet": EVM, "tracking_info": json.dumps(man)}, sig=sig)
    print(f"    fulfill: {st} {b[:120]}")
print("Done.")
