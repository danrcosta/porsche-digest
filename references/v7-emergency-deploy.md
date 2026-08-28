# Porsche Digest V7 Emergency Deploy Guide

## When Wrangler Tokens Fail

### Symptom
```
X [ERROR] A request to the Cloudflare API ... failed.
  Authentication error [code: 10000]
  Invalid access token [code: 9109]
```

### Quick Fix: Manual Dashboard Deploy

1. Open Cloudflare Dashboard → [Pages](https://dash.cloudflare.com)
2. Select project: **porsche-digest**
3. Click **New Deploy** → **Upload files**
4. Drag-and-drop ZIP file OR select individual files
5. Click **Deploy Site**

### Prepare Files

From project root:
```bash
cd ~/Hermes-Workspace/porsche-digest
mkdir -p v7-deploy
cp index.html styles-v7.css manifest.json icon-192.png v7-deploy/
# OR create ZIP:
zip -r porsche-digest-v7.zip index.html styles-v7.css manifest.json icon-192.png
```

## Token Debugging Checklist

| Check | What to Verify |
|-------|----------------|
| Token Type | Must start with `cft_` (NOT `cfat_`) |
| Permissions | `Cloudflare Pages → Edit`, `Workers Scripts → Edit`, `Memberships → Read` |
| Account ID | `0a68341689fffbae0284be2321350415` |
| Variable Name | `CLOUDFLARE_API_TOKEN` |

## Verify Success

```bash
curl -I https://digest.costafamily.ai
# Should return: HTTP/1.1 200 OK
```