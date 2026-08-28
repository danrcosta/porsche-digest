# Cloudflare Pages Deployment Guide - Porsche Digest V5

## Quick Start

```bash
cd /c/Users/SERVER/Hermes-Workspace/porsche-digest
npx wrangler pages deploy . --project-name=porsche-digest --account-id=0a68341689fffbae0284be2321350415 --branch=main
```

## Prerequisites

- **CLOUDFLARE_API_TOKEN** with Pages:Edit and Workers:Edit permissions
- **CLOUDFLARE_ACCOUNT_ID** = 0a68341689fffbae0284be2321350415
- **GITHUB_TOKEN** with repo write permissions (for automated commits)

## Authentication Setup

### Token Location
https://dash.cloudflare.com/profile/api-tokens

### Required Permissions
1. Account → Cloudflare Pages → **Edit**
2. Account → Workers Scripts → **Edit**
3. Zone → Page Rules → **Edit**
4. Zone → Cache Purge → **Edit** (for cache purging)

### Token Format
- Use **X-Auth-Key** format (cfk_ prefix)
- NOT Bearer token format
- Configure in `~/.hermes/.env` or project `.env`

## Environment Files

### Project .env (`/c/Users/SERVER/Hermes-Workspace/porsche-digest/.env`)
```
CLOUDFLARE_API_TOKEN=cfk_xxx
CLOUDFLARE_ACCOUNT_ID=0a68341689fffbae0284be2321350415
CLOUDFLARE_ZONE_ID=367fbd4a38aca5c99d2e5e309c827915
GITHUB_TOKEN=ghp_xxx
PROJECT_NAME=porsche-digest
PRIMARY_DOMAIN=digest.costafamily.ai
```

## Windows-Specific Notes

### Bash Path Issues
Windows MSYS2/git-bash can fail with complex Windows paths:
```bash
# ✅ GOOD
cd /c/Users/SERVER/Hermes-Workspace/porsche-digest

# ❌ BAD - fails due to spaces/characters
cd "D:\Hermes Project and Files\My Porsche 993 Carrera 4S 1996"
```

### Explicit npx Path
If npx is not found:
```bash
"C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx.cmd" wrangler pages deploy .
```

## Deployment Commands

### Automated (via publish.py)
```bash
python publish.py
```
- Archives current index.html
- Commits to GitHub
- Deploys via wrangler
- Verifies deployment

### Manual Deploy
```bash
npx wrangler pages deploy . --project-name=porsche-digest --branch=main
```

### With Cache Purge
```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/367fbd4a38aca5c99d2e5e309c827915/purge_cache" \
  -H "X-Auth-Key: $CLOUDFLARE_API_TOKEN" \
  -H "X-Auth-Email: $CLOUDFLARE_EMAIL" \
  --data '{"purge_everything":true}'
```

## Common Error Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 10000 | Auth failed | Create new token with correct permissions |
| EBUSY | File lock | Close processes, reboot if needed |
| 403 | WAF/block | Set security_level=low, browser_check=off |
| 404 | Project missing | Create project first |

## Post-Deploy URLs

| URL | Status |
|-----|--------|
| https://digest.costafamily.ai | Production |
| https://porsche-digest.pages.dev | Backup |
| /archive/ | Historical digests |

## Verification Checklist

- [x] index-v5.html deployed (dark theme, PWA)
- [x] styles-v5.css (premium design)
- [x] manifest.json (installable)
- [x] worker.js (service worker)
- [x] Node.js environment ready
- [x] wrangler installed ($ npx wrangler --version)
- [x] .env file configured

## Files in This Directory

| File | Purpose | Status |
|------|---------|--------|
| index-v5.html | V5 HTML with PWA | ✅ Ready |
| styles-v5.css | Premium styling | ✅ Ready |
| manifest.json | PWA manifest | ✅ Ready |
| worker.js | Service worker | ✅ Ready |
| wrangler.toml | Wrangler config | ✅ Ready |
| .env | Variables (DO NOT COMMIT) | ⚠️ Token required |
| publish.py | Auto deploy script | ✅ Ready |