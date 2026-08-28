# 🚀 Deploy Checklist - Porsche Digest V5

## ✅ Status Atual

- [x] Cloudflare login verificado
- [ ] Credenciais .env atualizadas
- [x] index-v5.html pronto (392 linhas)
- [x] styles-v5.css pronto
- [x] manifest.json pronto
- [x] publish.py pronto

## 🔐 Credenciais Necessárias AGORA

```bash
# Atualizar .env com:
CLOUDFLARE_API_TOKEN=cfk_***
CLOUDFLARE_ACCOUNT_ID=0a68341689fffbae0284be2321350415
GITHUB_TOKEN=ghp_***
```

## 📋 Próximos Passos para o Usuário

1. **Criar/atualizar token Cloudflare:**
   - https://dash.cloudflare.com/profile/api-tokens
   - Template: "Edit Cloudflare Workers"
   - Permissions: Pages Edit, Workers Scripts Edit, Page Rules Edit

2. **Criar token GitHub:**
   - https://github.com/settings/tokens
   - Permissions: repo → write

3. **Atualizar .env:**
   - Adicionar os tokens acima

4. **Deploy commands:**
   ```bash
   cd C:/Users/SERVER/Hermes-Workspace/porsche-digest
   python publish.py
   ```

## 📊 Destino Final

- **Production URL:** https://digest.costafamily.ai
- **Backup URL:** https://porsche-digest.pages.dev