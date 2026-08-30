#!/usr/bin/env python3
"""Build the Praise & Provoke landing page: inline preview image + QR codes as base64."""
import base64, io, os, qrcode

ROOT = "C:/Users/power/projects/jesus-fat-phobic"
DESIGN = f"{ROOT}/design"
SITE = f"{ROOT}/site"
DOCS = f"{ROOT}/docs"

BTC_ADDR = "bc1qa7txyzk3yqxgln09uzujqcy47eua4f8afsdhec"
USDC_ADDR = "0x05ff3061352c6C30855f1b77F640e9412c56eA1d"

def b64(path, kind):
    with open(path, "rb") as f:
        return "data:" + kind + ";base64," + base64.b64encode(f.read()).decode()

def qr_b64(data, box=8):
    img = qrcode.make(data, box_size=box, border=2)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

preview = b64(f"{DESIGN}/bumper-sticker-preview.png", "image/png")
qr_btc = qr_b64("bitcoin:" + BTC_ADDR)
qr_usdc = qr_b64(USDC_ADDR)

tpl = open(f"{SITE}/index.template.html", encoding="utf-8").read()
html = (tpl
        .replace("{{PREVIEW_B64}}", preview)
        .replace("{{QR_USDC}}", qr_usdc)
        .replace("{{QR_BTC}}", qr_btc))

out = f"{DOCS}/index.html"
os.makedirs(DOCS, exist_ok=True)
open(out, "w", encoding="utf-8").write(html)
print("built:", out, os.path.getsize(out), "bytes")
