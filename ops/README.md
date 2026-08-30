# Praise & Provoke — JESUS IS FAT PHOBIC bumper sticker ops

**Storefront:** https://invisiblemonsters.github.io/jesus-is-fat-phobic/
**Repo:** https://github.com/invisiblemonsters/jesus-is-fat-phobic
**Project dir:** `C:\Users\power\projects\jesus-fat-phobic\`

## Product & pricing
- 7.5″ × 3.75″ matte vinyl bumper sticker, die-cut fish, black on yellow.
- Print file: `design/bumper-sticker-print-300dpi.png` (2250×1125 @300dpi). Vector: `design/sticker.svg`.
- Retail: $49.99 / 10-pack (2 = $89.99, 3 = $124.99). Free US shipping.
- Our cost: $28 / 10-pack at StickerMule (free shipping). Margin ≈ $21.99/pack before any intl surcharge.

## Payment wallets (all receive-only, public)
| Method | Detail |
|---|---|
| USDC (Base, chain 8453) | `0x05ff3061352c6C30855f1b77F640e9412c56eA1d` — key `~/.metatron/sticker-business-wallet.json` |
| BTC (on-chain) | `bc1qa7txyzk3yqxgln09uzujqcy47eua4f8afsdhec` — key `~/.metatron/btc-wallet-new.json` |
| Lightning | `metatronscribe@coinos.io` — creds `~/.metatron/coinos-wallet.json` |

## Order loop (manual v1)
1. Customer submits order form → email lands in powers.chr@gmail.com with name/address/packs/payment/txhash.
2. **Verify payment on-chain before printing:**
   - USDC: https://basescan.org/address/0x05ff3061352c6C30855f1b77F640e9412c56eA1d — look for incoming USDC tx of the exact amount.
   - BTC: https://mempool.space/address/bc1qa7txyzk3yqxgln09uzujqcy47eua4f8afsdhec — confirm amount + 1 confirmation.
   - LN: coinos dashboard (https://coinos.io) → transactions. Amount should match ≈$ fiat at send time.
3. **Place print order** at https://www.stickermule.com/products/bumper-stickers:
   - Size 7.5″ × 3.75″, qty 10 per pack ordered, upload `design/bumper-sticker-print-300dpi.png`, approve proof, ship to the customer's address.
   - StickerMule accepts USDC (Stripe wallet connect) at checkout — keep the loop crypto-native.
4. Reply to customer with tracking. Done.

## Verification automation (next step)
- Add a payment-monitor cron (no_agent script): poll BaseScan/mempool for the two addresses every 30 min; if balance delta > $0, emit order-pending alert with the tx. Script template idea in `tools/` — needs `requests` or plain urllib.
- A BaseScan API key (free) makes USDC token transfers queryable via `?module=account&action=tokentx`.

## StickerMule Store upgrade (makes checkout fully automated)
StickerMule Stores now accept crypto at checkout natively (Mar 2026) — buyers pay USDC, StickerMule prints + ships, we get paid out.
1. Create store at https://www.stickermule.com/stores (needs email + payout details — user action).
2. Upload product: bumper stickers, 7.5″×3.75″, 10-pack, art = `design/bumper-sticker-print-300dpi.png`, price $49.99.
3. Point the "Buy" button on the landing page at the store product URL.
4. Landing page payment block stays as fallback for direct crypto orders.

## Notes / pitfalls
- **Never send USDC on the wrong network** — the address is EVM but only Base is monitored. Landing page says this; ops must too.
- BTC amount floats: accept ≈ retail total; if short by >5%, email customer before printing.
- Content note: provocative religious satire — legal (parody/commentary, no targeted harassment), but mainstream ad platforms will refuse it. That's WHY we're crypto-native and self-hosted. Do not try Etsy/Redbubble/Amazon Merch.
- Keep `tools/build_site.py` as the source of truth for the page; `docs/index.html` is generated (contains base64 images). Pages serves `/docs`.
