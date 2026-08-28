# 🚀 Cloudflare Connection - INSTRUÇÕES PARA CONEXÃO

## 📍 ACESSO IMEDIATO

### 1. 🔐 Cloudflare API Tokens
**URL:** https://dash.cloudflare.com/profile/api-tokens

**PASSO A PASSO:**
1. Clique em **"Create Token"** (Criar Token)
2. Escolha template: **"Edit Cloudflare Workers"**
3. Em **Permissions** (Permissões), adicione:
   - ✅ **Account → Cloudflare Pages → Edit**
   - ✅ **Account → Workers Scripts → Edit**
   - ✅ **Zone → Page Rules → Edit**
4. Clique em **Continue to summary**
5. Copie o token gerado
6. Cole no arquivo: `C:/Users/SERVER/Hermes-Workspace/porsche-digest/.env`
   - Linha: `CLOUDFLARE_API_TOKEN=seu_token_aqui`

### 2. 🏠 GitHub Personal Access Token
**URL:** https://github.com/settings/tokens

**PASSO A PASSO:**
1. Clique em **"Generate new token"** (Gerar novo token)
2. Nomeie: **"Porsche Digest Deploy"**
3. Selecione permissão: **`repo → write`**
4. Clique em **Generate token**
5. **COPIE IMMEDIATAMENTE** (não será mostrado novamente)
6. Cole no arquivo: `C:/Users/SERVER/Hermes-Workspace/porsche-digest/.env`
   - Linha: `GITHUB_TOKEN=seu_token_aqui`

### 3. ✅ VERIFICAR AUTENTICAÇÃO
Depois de inserir os tokens no .env, execute no terminal:
```bash
npx wrangler whoami
```

### 4. 🚀 FAZER DEPLOY DA V5

**Opção A - Automatizado (recomendado):**
```bash
python publish.py
```

**Opção B - Manual:**
```bash
npx wrangler pages deploy . --project-name=porsche-digest
```

---

## 📊 STATUS ATUAL DO PROJETO

| Arquivo | Status |
|---|---|
| `index-v5.html` | ✅ Pronto (392 linhas) |
| `styles-v5.css` | ✅ Pronto (16KB) |
| `manifest.json` | ✅ PWA configurado |
| `wrangler.toml` | ✅ Configurado |
| `.env` | ⚠️ Aguarda tokens |

---

## 🎯 RESULTADO ESPERADO

Quando tudo estiver conectado corretamente:
1. O deploy será feito para `porsche-digest.pages.dev`
2. O domínio `digest.costafamily.ai` será vinculado automaticamente
3. O PWA estará funcional (instalação em dispositivos)
4. Histórico em `/archive/YYYY-MM-DD.html` será gerado

---

## ❌ TROUBLESHOOTING

**Se wrangler whoami falhar:**
- Verifique se o token tem as permissões corretas
- Verifique se não expirou o token

**Se deploy falhar com timeout:**
- Use: `python publish.py` (ele lida com arquivos grandes)
- Ou divida em partes menores

**Se domínio não aparecer:**
- Verifique Zone ID correto em Cloudflare DNS