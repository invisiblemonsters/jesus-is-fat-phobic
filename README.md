# JESUS IS FAT PHOBIC — bumper stickers

Vinyl bumper stickers, sold crypto-native (USDC / BTC / Lightning). Printed by a real
print shop, shipped to your door. Pay with crypto — no card, no bank, no account.

- **Storefront:** https://invisiblemonsters.github.io/jesus-is-fat-phobic/
- **Size:** 7.5″ × 3.75″, matte vinyl, removable adhesive, weatherproof
- **Price:** $49.99 / 10-pack, free US shipping

## Repo layout
- `design/` — print-ready artwork (`bumper-sticker-print-300dpi.png`, `sticker.svg`, generator script)
- `docs/` — generated landing page (served by GitHub Pages from `/docs`)
- `site/` — landing page template
- `tools/build_site.py` — inlines preview + QR codes into the page
- `ops/README.md` — order loop, wallets, fulfillment details

## Build
```
python tools/build_site.py   # regenerates site/index.html from template
```
