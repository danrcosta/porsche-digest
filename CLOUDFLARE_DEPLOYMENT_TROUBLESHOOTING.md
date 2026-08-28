# Cloudflare Pages Deployment Troubleshooting

## Windows Terminal Environment Issues

### Problem: Bash Script Failures with C:/ Paths
**Symptom:**
```
/usr/bin/bash: line 4: cd: /d/Hermes Project and Files/My Porsche 993 Carrera 4S 1996: No such file or directory
bash: no job control in this shell
```

**Root Cause:**
Bash in MSYS2/git-bash tries to change to a Windows user directory that contains spaces and special characters. The shell's default startup script (`~/.bashrc` or `bash_profile`) sources settings that cd to a user-specific project directory.

**Fix:**
1. **Use absolute paths in commands:**
   ```bash
   bash -c 'cd /c/Users/SERVER/Hermes-Workspace/porsche-digest && command'
   ```
2. **Or disable profile loading:**
   ```bash
   bash --norc --noprofile -c 'cd /c/Users/SERVER && command'
   ```
3. **Or use forward slashes consistently:**
   ```bash
   cd /c/Users/SERVER/Hermes-Workspace/porsche-digest  # Works
   # Avoid: cd "D:\Hermes Project..."  # Fails due to spaces
   ```

### Problem: npx/subprocess Not Found
**Symptom:**
```
FileNotFoundError: [WinError 2] The system cannot find the file specified
```

**Fix:**
1. **Use explicit npx path:**
   ```bash
   "C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx.cmd" wrangler pages deploy .
   ```
2. **Or add to PATH in environment:**
   ```python
   env = os.environ.copy()
   env['PATH'] = 'C:\\Users\\SERVER\\AppData\\Roaming\\npm;' + env.get('PATH', '')
   subprocess.run(['npx', 'wrangler', ...], env=env)
   ```

## Cloudflare Authentication

### Error Code 10000
**Symptom:**
```
Authentication error [code: 10000]
```

**Fix:**
1. Go to https://dash.cloudflare.com/profile/api-tokens
2. Create new token with these permissions:
   - Account → Cloudflare Pages → Edit
   - Account → Workers Scripts → Edit
   - Zone → Page Rules → Edit
3. Use `X-Auth-Key` format (cfk_ prefix) not Bearer token

### Token Format Requirements
The `cfk_` token format uses **X-Auth-Key + X-Auth-Email**, NOT Bearer tokens:
```bash
export CLOUDFLARE_API_TOKEN=cfk_...
export CLOUDFLARE_ACCOUNT_ID=0a68341689fffbae0284be2321350415
export CLOUDFLARE_EMAIL=danrc@mac.com
```

## Direct Deployment Commands

### Method 1: Wrapper (Recommended)
```bash
cd /c/Users/SERVER/Hermes-Workspace/porsche-digest
python publish.py
```

### Method 2: Direct wrangler
```bash
cd /c/Users/SERVER/Hermes-Workspace/porsche-digest
npx --yes wrangler pages deploy . --project-name=porsche-digest --account-id=0a68341689fffbae0284be2321350415 --branch=main
```

### Method 3: Explicit path
```bash
"C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx.cmd" wrangler pages deploy . --project-name=porsche-digest --branch=main
```

## URLs After Deploy

| URL | Purpose |
|---|---|
| https://digest.costafamily.ai | Production |
| https://porsche-digest.pages.dev | Backup Cloudflare Pages |
| https://digest.costafamily.ai/archive | Historical archives |
| https://porsche-digest.pages.dev/archive | Alternative archive path |

## Verification Checklist

After deployment:
- [ ] Homepage loads correctly
- [ ] PWA installable (manifest linked)
- [ ] Service worker registered (offline capability)
- [ ] Charts render (Chart.js)
- [ ] Mobile responsive (***REMOVED*** 430px breakpoint)
- [ ] Theme toggle works (dark/light)
- [ ] Archive directory populated