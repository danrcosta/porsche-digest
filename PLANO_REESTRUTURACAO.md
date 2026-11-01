# Porsche Digest — Plano de Reestruturação e Validação

**Data:** 2026-11-01  
**Autor:** Hermes (assistente pessoal)  
**Projeto:** danrcosta/porsche-digest  
**Status:** Planejamento — aguardando aprovação do Daniel

---

## 1. Resumo do Estado Atual (descoberto)

| Camada | O que existe | Observação |
|--------|--------------|------------|
| **GitHub (`danrcosta/porsche-digest`)** | Repo clonado; código + dados + deploy scripts | Estrutura bagunçada: arquivos duplicados, scripts antigos, `generate_digest.py` quebrado por ofuscamento de strings (`la***REMOVED***`). |
| **Lovable (`porsche-993-digest.lovable.app`)** | Site publicado com conteúdo de 31/08/2026 | Parece ser um build separado (React), **não reflete** o `dist/` do repo nem o `data/latest.json`. |
| **Cloudflare Pages** | Deploy do projeto `porsche-digest-v7` via `wrangler pages deploy dist` | O domínio `digest.costafamily.ai` serve o `dist/index.html` do repo (versão 04/10/2026). O Lovable serve outra versão. |
| **Generator** | `generator/generate_digest.py` + `daily_hero_image.py` + `get_quote.py` | Estava com erro de sintaxe por ofuscamento de strings (`latest`, `road trips`). **Corrigido**. |

### Problemas confirmados

1. **Generator quebrado** — ofuscamento corrompeu variáveis/strings; impedia rebuild.
2. **Fonte da truth não clara** — `data/latest.json` é a base mais rica (2026-10-28), mas o `dist/index.html` estava defasado (04/10).
3. **Duplicação de assets** — `dist/`, `v7-deploy/`, `assets/hero/` com imagens soltas.
4. **Deploy duplicado** — Lovable vs Cloudflare Pages.
5. **Arquivos mortos** — `bbc_search.html`, `bing_search.html`, `google_search.html`, `g1_gkpn.html`, `g1_search.html`, `deploy-v7-api.py`, `deploy.sh`, `deploy-checklist.md`, `C:Tempempty_env.txt`, `C:UsersSERVERreplace.txt`.

---

## 2. O que já foi ajustado (antes do plano)

- **Corrigido `generate_digest.py`**: restauradas as strings ofuscadas (`latest`, `road trips`, `latest.json`). O script agora compila e executa.
- **Execução bem-sucedida**: o generator rodou, gerou `index.html` + `data/latest.json` + `archive/2026-11-01.json` sem erros.
- **Verificação**: `diff index.html dist/index.html` retornou vazio — o `dist/` já estava atualizado.

---

## 3. Lista Completa de Fontes Cadastradas (MASTER)

Consolidado de 6 locais: `latest.json`, `digest.json`, `get_community_sources()` (93), `PORSCHE_SOURCES_COMPREHENSIVE.md` (29KB), `chat-history.json`, V7 `config/sources.json` + `personas.json` + `library.json`.

### 3.1 Fontes oficiais Porsche
- Porsche Stories, Porsche Newsroom, Porsche Classic, Porsche Classic Parts, Porsche COA Request, Porsche Tequipment, Porsche Official YouTube, Porsche Classic YouTube, Porsche (IG), Porsche Classic (IG), Porsche Design, Porsche Panorama (PCA)

### 3.2 Comunidade & Fóruns
- Rennlist 993 Forum, Pelican Parts Forums + Tech Articles + 993 catalog, 6SpeedOnline 911 Carrera, Reddit r/Porsche + r/911, Total 911 Magazine + RSS + Buyer's Guide, Porsche Club Brasil + Eventos, Porsche BR Facebook, PCA.org + PCA Concours, Petrolicious + RSS, FLATSIX Magazine, Opposite Lock, Speed Hunters, DriveTribe, Supercars.net, Road & Track, MotorTrend, Meetup.com, Classic & Sports Car, Octane Magazine, Sports Car International, Sports Car Market, 911 & Porsche World, Stuttcars.com

### 3.3 Social & YouTube
- @porsche, @porscheclassic, @aircooled.net, @993_911, @magnuswalker, @petrolicious (IG)
- YouTube: Porsche Official, Porsche Classic, Petrolicious, Hagerty, Jay Leno's Garage, RegularCars, The Smoking Tire, Chris Harris on Cars, Harry's Garage, Everyday Driver, MotoMan TV, DtRockstar1, Total 911 Magazine, Magnus Walker, Bitchin' Rides, MotorTrend, Rob Dahm, Rebuild Rescue, Adam LZ, Chris Fix, Garage Time, The Flat Six Garage, Cutting Edge Engineering, Canzoniero, Horsepower University, Porsche Design

### 3.4 Auctions & Marketplaces
- Bring a Trailer, Cars & Bids, RM Sotheby's, Gooding & Company, Bonhams, Mecum Auctions, Collecting Cars, COYS Auctions, AutoHunter by Cox, eBay Motors, Elferspot, PCarmarket, Classic.com 993 Market + Insights, mobile.de, AutoScout24

### 3.5 Valuation Services
- Hagerty Valuation Tools + 993 Market Report, NADA Guides, PriceMyClassic, AutoTrader Classics, duPont Registry, Classic.com Insights 993

### 3.6 Builders & Restorers
- Singer Vehicle Design, Gunther Werks, RUF Automobile, Canepa Design, DP Motorsport, Lanzante Motorsport, Elephant Racing, TechArt, RWB, FVD Brombacher, AutoAtlantis BR, Drivestyle Sportwagen, Eberlein Automobile, SINDIK Automobile, Mechatronik GmbH, ENVER Services, Freisinger Motorsport, Early 911S (Manfred Hering)

### 3.7 Parts & Technical
- FCP Euro, Genuine Porsche Parts, Stoddard Porsche, Suncoast Parts, AutoAtlantis BR, Pelican Parts 993, Porsche Classic Tequipment, 8speedshop, Bilstein/KW, TechInfo Porsche (PET), PorschePerfect Guides, Partswise, Fabspeed Performance, GIAC Tuning, BBI Autosport

### 3.8 Events & Concours
- Pebble Beach Concours, Rennsport Reunion, PCA Concours, Porsche Club Brasil Eventos, Goodwood Festival of Speed

### 3.9 Dealers & Workshops (European Specialist Directory) — Verified 2026-10-04
- **Switzerland (Buy):** Fastback Motors, Leuba Collection, Elite Sportwagen AG, Cars for Drivers Switzerland SA, Klausen Cars SA, Weber Motorentechnik AG, Sportec AG, Porsche Classic Zentrum Genf
- **Switzerland (Service):** Klausen Cars SA, Weber Motorentechnik AG, Sportec AG, Porsche Classic Zentrum Genf
- **Germany:** Werk 2 Sportwagen GmbH, Early 911S (Manfred Hering), Kickdown GmbH, JANSEN Classische Automobile, automax. GmbH, Dirk Rüschoff, Springbok Sportwagen, AECARS BV, RS-Mobility GmbH, ELFERCENTRUM GmbH, Dresden Motor Classics, Sportwagenclassics, Steenbuck, Triple & Crown, DAVID Finest Sports Cars, Schaltkulisse GmbH, Mechatronik GmbH, Freisinger Motorsport, RUF Automobile, ENVER Services
- **Belgium:** Carrera-Sport-Classics (Guy Claessens), The Automobile Store, Autohandel Sneppe Bv
- **France:** MECANICUS, ARNAGE MOTORS – CarJager, L'art de l'automobile, A. Fein Automobile, Classiccenter
- **Italy:** Evoluzione Collections, M.R. srl
- **Spain:** 11erEcke
- **Sweden:** Daytona Automobil
- **Netherlands:** Porsche Centrum Gelderland, Porsche Centrum Twente, Oldtimerfarm BV, Automobielbedrijf van Schagen, Theunissen Automobielen, OM-Automobile GmbH, Maassen Classics, H. Schäffer GmbH, SD Automobile, Automobile Stieglbauer, Gallery Aaldering, Car Service Visser
- **UK:** Autofarm, Tuthill Porsche, SST Auto / Speedsport Tuning
- **USA (Dealers):** Beverly Hills Car Club, AutoKennel, European Collectibles, Canepa, DriverSource, Bocars, Sloan Motor Cars, Copley Motorcars, The Toy Barn, Daniel Schmitt & Co., Marshall Goldman, Fantasy Junction, California Porsches, Makellos Classics, CPR Classic, Fusion Motor Company, HCC Specialty Cars, LBI Limited, Gullwing Motor Cars, The Stable, Ltd.
- **USA (Workshops):** Patrick Motorsports, TurboKraft, TRE Motorsports, Callas Rennsport, Rothsport Racing, Protomotive, Zims Autotechnik, Kelly-Moss, Automobile Associates of Canton, Sonderwerks, Jesse's Garage, Aase Motors, Einmalig, Supertec Performance, Burnham Performance, Ed Pink Racing Engines, Hergesheimer Motorsports, Modern Aircooled, Trafton's Foreign Auto, Hi-Tec Automotive

### 3.10 APIs/Feeds
- Exchange Rate API, YouTube Data API v3 (Porsche), Content Hub Imgix (CDN imagens Porsche)

### 3.11 Notícias & Conteúdo (em `latest.json`)
- Porsche Stories (5–7 artigos fixos): 993 seven things, engine oil guide, buying guide, restoration guide, classic car care
- 10 auction listings ativos (BaT, Cars & Bids, Classic.com) — 1994–1998 C4S/Carrera/Turbo
- 3 vídeos por persona (Drivers: Porsche/Hagerty/Porsche Stories; Collectors: Porsche Classic/Canzoniero; Custom: Smoking Tire/Horsepower University/Porsche Design)

---

## 4. Regras de Atualização

| Item | Frequência | Responsável | Método |
|------|------------|-------------|--------|
| **Conteúdo do site (`index.html`)** | Diário 07:00 BR | Daniel / Hermes | `python generator/generate_digest.py` → `git commit` + deploy |
| **`data/latest.json`** | Mesmo do site | Generator | Escrito automaticamente pelo generator |
| **Archive JSON** | Diário | Generator | `archive/YYYY-MM-DD.json` |
| **Hero image** | Diária (seed por data) | `daily_hero_image.py` | Determinística; troca automaticamente |
| **Quote diária** | Diária | `get_quote.py` | Seed por data |
| **Exchange rate** | On-demand (API) | Generator | `api.exchangerate-api.com/v4/latest/USD` |
| **Deploy Cloudflare** | Após cada build | Daniel / Hermes | `npx wrangler pages deploy dist --project-name porsche-digest-v7` |
| **GitHub Actions (opcional)** | Push em `main` | GitHub | Build + deploy automático |

### Regras de negócio do conteúdo
- Máximo **5 artigos** Porsche Stories (ordenados por `days_ago`).
- Máximo **10 auction listings**.
- Máximo **3 vídeos por persona** (fixos, não mutáveis por enquanto).
- **Owner card** fixo: Daniel Costa / 1996 993 C4S.
- **Valuation**: C4S, Carrera, Turbo — USD + BRL (cotação do dia).
- **Turbo S highlight**: fixo no template.

---

## 5. Estrutura de Pastas Proposta (após reestruração)

```
porsche-digest/
├── data/
│   └── latest.json              # Fonte da verdade para Lovable + dist
├── archive/
│   └── YYYY-MM-DD.json          # Histórico diário
├── assets/
│   └── hero/                    # Imagens hero locais (opcional)
├── generator/
│   ├── generate_digest.py       # Gera HTML + JSON + archive
│   ├── daily_hero_image.py      # Seed de hero image
│   └── get_quote.py             # Seed de quote diária
├── templates/
│   └── digest_template_v3.html  # Template HTML com placeholders
├── dist/                        # Build final para Cloudflare Pages
│   ├── index.html
│   ├── styles-v7.css
│   ├── manifest.json
│   ├── _headers
│   └── icon-192.png
├── v7-deploy/                   # Backup alternativo (manter ou remover)
├── personas/                    # Definições das 3 personas
├── reference_docs/              # PDFs e docs técnicos
├── skills/                      # Skill de versionamento
├── scripts/
│   ├── build.sh                 # Build automatizado (novo)
│   └── deploy.sh                # Deploy automatizado (novo)
├── data/digest.json             # Pode ser mantido para compatibilidade
├── daily_hero.json              # Pode ser mantido para compatibilidade
├── wrangler.toml                # Config Cloudflare Pages
├── index.html                   # Link para dist/index.html (ou remover)
└── README.md                    # Documentação do projeto
```

---

## 6. Pipeline Atual (funcionando)

```
[1] Dados fixos/atuais
    ├── data/latest.json (notícias, auctions, valuation, vídeos, community)
    ├── daily_hero.json (hero image do dia)
    └── get_quote.py (quote diária)

[2] Generator
    └── python generator/generate_digest.py
        ├── Lê data/latest.json + daily_hero.json
        ├── Gera templates/digest_template_v3.html → index.html
        ├── Escreve data/latest.json (refresh)
        ├── Escreve archive/YYYY-MM-DD.json
        └── (Opcional) Deploy via wrangler

[3] Build
    └── Copia index.html + assets + styles-v7.css → dist/

[4] Deploy
    └── npx wrangler pages deploy dist --project-name porsche-digest-v7
        └── https://digest.costafamily.ai
```

---

## 7. Objetivos do Projeto

1. **Briefing diário** de Porsche 993 Carrera 4S para Daniel Costa.
2. **Conteúdo curado** por 3 personas (Driver, Collector, Custom).
3. **Dados de mercado** em tempo quase-real (auctions, valuation).
4. **Publicação automática** via Cloudflare Pages.
5. **Fonte da verdade única**: `data/latest.json`.
6. **Design premium** (Dark + Gold, tipografia Porsche).
7. **Performance**: estático, cacheável, sem backend.
8. **Extensibilidade**: suporte a Lovable React app no futuro.

---

## 8. Tarefas do Plano (em ordem)

### 8.1 Limpeza e organização (commit separado)
- [ ] Remover arquivos mortos: `bbc_search.html`, `bing_search.html`, `google_search.html`, `g1_gkpn.html`, `g1_search.html`, `deploy-v7-api.py`, `deploy.sh`, `deploy-checklist.md`, `C:Tempempty_env.txt`, `C:UsersSERVERreplace.txt`, `proxy-worker.js`, `test_cf_mcp.py`, `run_browser_task.py`, `publish.py`, `update_cname.py`, `update_cname_v2.py`.
- [ ] Remover `v7-deploy/` ou integrar seus arquivos ao `dist/`.
- [ ] Remover `dist/` duplicados desnecessários.
- [ ] Consolidar `styles-v7.css` (raiz + dist) em um só lugar.
- [ ] Atualizar `README.md` com instruções claras de build/deploy.

### 8.2 Scripts de automação
- [ ] Criar `scripts/build.sh` (bash) que:
  1. Roda `python generator/generate_digest.py`
  2. Copia `index.html`, `styles-v7.css`, `manifest.json`, `_headers`, `icon-192.png`, `sw.js` para `dist/`
  3. Copia `assets/hero/*` para `dist/assets/hero/`
- [ ] Criar `scripts/deploy.sh` (bash) que:
  1. Roda `scripts/build.sh`
  2. Roda `npx wrangler pages deploy dist --project-name porsche-digest-v7`
- [ ] Converter scripts para PowerShell se necessário para o ambiente Windows de Daniel.

### 8.3 Validação do build local
- [ ] Executar `scripts/build.sh` localmente.
- [ ] Abrir `dist/index.html` em browser para verificação visual.
- [ ] Comparar hero title, hero image, quote, data, auctions, valuation, vídeos com `data/latest.json`.
- [ ] Verificar links quebrados (imagens externas) com `curl -I`.
- [ ] Verificar que `data/latest.json` reflete o conteúdo publicado.

### 8.4 Deploy e sincronização
- [ ] Fazer commit de todas as correções.
- [ ] Push para `main` no GitHub.
- [ ] Deploy manual no Cloudflare Pages.
- [ ] Validar `https://digest.costafamily.ai`.
- [ ] (Opcional) Configurar GitHub Actions para deploy automático.

### 8.5 (Futuro) Integração Lovable
- [ ] Decidir: manter Lovable como frontend consumindo `data/latest.json` ou migrar para o HTML estático?
- [ ] Se mantiver Lovable: garantir que `data/latest.json` é o único output do generator.
- [ ] Se migrar para estático: desativar Lovable deploy.

### 8.6 (Futuro) Conteúdo dinâmico
- [ ] Implementar fetch real de notícias (Porsche RSS, BaT, Cars & Bids) — atualmente hard-coded.
- [ ] Implementar hero image real (download/upload) ao invés de seed determinística.
- [ ] Implementar quote real via API/curadoria.

---

## 9. Checklist de Validação Pós-Execução

- [ ] `python generator/generate_digest.py` roda sem erros.
- [ ] `data/latest.json` contém data atual (hoje).
- [ ] `archive/YYYY-MM-DD.json` existe.
- [ ] `dist/index.html` abre sem erros no browser.
- [ ] Hero image carrega (HTTP 200).
- [ ] Quote, data, valuation, auctions, vídeos aparecem corretamente.
- [ ] `npx wrangler pages deploy dist` sucede.
- [ ] `https://digest.costafamily.ai` reflete o conteúdo mais recente.

---

## 10. Decisões Pendentes (para Daniel)

1. **Manter ou desativar o deploy do Lovable?**
2. **Usar scripts bash ou PowerShell** para build/deploy no Windows?
3. **Manter `v7-deploy/`** ou remover?
4. **Implementar fetch real de conteúdo** (RSS/auction sites) ou manter hard-coded por enquanto?
5. **Adicionar GitHub Actions** para deploy automático?

---

## 11. Próximos Passos Imediatos (se Daniel aprovar)

1. Executar **8.1** (limpeza).
2. Executar **8.3** (validação local).
3. Executar **8.4** (deploy).
4. Iterar baseado em feedback visual.
