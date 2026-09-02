# Cloudflare Deployment Troubleshooting

## Authentication Error [code: 10000]

### Symptom
```
Authentication error [code: 10000]
```

### Root Cause
Token is either expired, invalid, or lacks required permissions.

### Solution
1. Navigate to https://dash.cloudflare.com/profile/api-tokens
2. Click "Create Token" or "Edit" existing token
3. Required permissions:
   - Account → Cloudflare Pages → Edit
   - Account → Workers Scripts → Edit
   - Zone → Page Rules → Edit
4. Save and update environment variables:
   ```bash
   export CLOUDFLARE_API_TOKEN=cfk_xxx
   export CLOUDFLARE_ACCOUNT_ID=0a68341689fffbae0284be2321350415
   ```

## Windows Bash Path Issues

### Symptom
```
/usr/bin/bash: line 4: cd: /d/Hermes Project and Files/My Porsche 993 Carrera 4S 1996: No such file or directory
bash: no job control in this shell
```

### Root Cause
Bash's startup scripts source to a user project directory with spaces/special characters.

### Solution
```bash
# Use absolute paths with /c/ prefix
bash -c 'cd /c/Users/SERVER/Hermes-Workspace/porsche-digest && command'

# Or use explicit npx path
"C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx.cmd" wrangler ...
```

## EBUSY Error (NTUSER.DAT Lock)

### Symptom
```
EBUSY: resource busy, open 'C:\\...\\NTUSER.DAT'
```

### Solution
1. Close all file explorers and editors
2. If persists, reboot Windows
3. Run deploy from fresh terminal session
4. As last resort, deploy from different machine

## Token Format

The cfk_ token format uses **X-Auth-Key + X-Auth-Email**, NOT Bearer:
```bash
CLOUDFLARE_API_TOKEN=cfk_YOUR_KEY_HERE
```

## Deployment Commands

### Automated via Python wrapper
```bash
cd /c/Users/SERVER/Hermes-Workspace/porsche-digest
python publish.py
```

### Direct wrangler
```bash
npx wrangler pages deploy . --project-name=porsche-digest --branch=main
```

### With explicit paths
```bash
"C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx.cmd" wrangler pages deploy .
```

## Post-Deploy URLs

| URL | Purpose |
|---|---|
| https://digest.costafamily.ai | Production |
| https://porsche-digest.pages.dev | Backup |
| /archive/ | Historical digests |

## Verification Checklist

- [ ] index-v5.html deployed (PWA features)
- [ ] styles-v5.css (dark theme)
- [ ] manifest.json (installable)
- [ ] worker.js (service worker)
- [ ] Node.js/wrangler accessible
- [ ] .env file configured (DO NOT COMMIT)