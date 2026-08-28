# 🎯 Cloudflare Integration - Cloudflare Dashboard Quick Access

## 📍 Áreas Necessárias para Correção de Erros

### 1. **API Tokens** - https://dash.cloudflare.com/profile/api-tokens
**Ação Necessária:** Criar novo token com permissões:
- ✅ Account → Cloudflare Pages → Edit
- ✅ Account → Workers Scripts → Edit
- ✅ Zone → Page Rules → Edit

### 2. **Cloudflare Dashboard** - https://dash.cloudflare.com
**Verificar:**
- 🏢 Account ID: `0a68341689fffbae0284be2321350415`
- 🌐 Zone ID: `367fbd4a38aca5c99d2e5e309c827915`
- 🔧 Project: Porsche Digest Pages

### 3. **GitHub Tokens** - https://github.com/settings/tokens
**Ação Necessária:** Verificar token tem permissão de WRITE

---

## 📁 Estrutura do Projeto Porsche Digest

**Localização:** `C:/Users/SERVER/Hermes-Workspace/porsche-digest/`

```
📦 porsche-digest/
├── 🔐 .env              # Credenciais (não mostrar)
├── ⚙️  wrangler.toml     # Configuração Cloudflare
├── 🚀 publish.py         # Script de deploy automatizado
├── 📄 index-v5.html     # V5 HTML (DOMINANTE)
├── 🎨 styles-v5.css     # Styles premium V5
├── 📱 manifest.json    # PWA Manifest
├── ⚡ worker.js         # Service Worker
├── 🛠️  proxy-worker.js  # Worker para domínio custom
├── 📁 archive/          # Arquivos históricos
├── 📁 previews/         # Páginas de preview
└── 📋 .env.example      # Modelo de configuração

## 🚀 Comandos de Deploy

```bash
# 1. Verificar autenticação
npx wrangler whoami

# 2. Fazer deploy
python publish.py
# OU
npx wrangler pages deploy . --project-name=porsche-digest

# 3. Verificar logs
wrangler pages deployment list
```

## 📊 Status de Erros Monitorados

| Error Code | Descrição | Solução |
|-----------|-----------|---------|
| 10000 | Authentication failed | Criar novo token API |
| EBUSY | Concorrência múltipla | Retry com delay |
| Timeout 60s | Arquivo muito grande | Usar publish.py |