# porsche-digest
Daily Porsche 993 Carrera 4S Intelligence Brief — auto-published to `digest.costafamily.ai` via Cloudflare Pages.

## Quick start
```bash
python generator/generate_digest.py
npx wrangler pages deploy dist --project-name porsche-digest-v7
```

## What it does
- Reads `data/latest.json` + `daily_hero.json`
- Generates `index.html` + `archive/YYYY-MM-DD.json`
- Builds static output into `dist/`
- Deploys to Cloudflare Pages

## Source of truth
- `data/latest.json` — canonical daily payload
- `archive/*.json` — historical snapshots
- `generator/generate_digest.py` — build + deploy logic

## Daily ritual
1. Run the generator
2. Review `dist/index.html`
3. Deploy with wrangler
