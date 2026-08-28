---
name: porsche-digest-version-control
description: Compare and validate Porsche Digest HTML versions to ensure meaningful evolution between releases
version: 1.0.0
author: Daniel Costa
license: MIT
platforms: [windows, mac]
metadata:
  hermes:
    tags: [porsche, digest, version-control, comparison]
    related_skills: [porsche-archive-system]
---

# Porsche Digest Version Control

## Quando Usar
Use esta skill quando comparar versões do Porsche Digest, verificar mudanças críticas, ou validar que uma nova versão trouxe melhorias reais em cima de versões anteriores.

## Problema Comum Detectado
Usuário reclamou que V5 era idêntica à de 22/08/2026 - sem evolução real.

## Fluxo de Comparação

### 1. Verificar Histórico de Métricas
```bash
# Comparar tamanhos
ls -la index.html index-v5.html index-v6.html 2>/dev/null

# Comparar hashes MD5
md5sum index*.html
```

### 2. Verificar Elementos Críticos
- **Title Tags:** "Porsche Digest V5" vs "V4" etc
- **CSS References:** styles-v5.css vs styles-v4.css
- **Feature Flags:** persona sections, charts, PWA
- **Content Date:** Deve mudar diariamente

### 3. Diferenças Esperadas V7 vs V5
| Feature | V5 | V7 | Status |
|---|---|---|---|
| Seções | 6 | 8 | ✅ Evolução |
| Leilões | 10 | 15 | ✅ Evolução |
| Personas | Básico | Detalhado | ✅ Evolução |
| Charts | Básico | Interativo | ✅ Evolução |
| PWA | Parcial | 100% | ✅ Evolução |

### 4. Script Automático
```python
#!/usr/bin/env python3
def compare_digest_versions(v1_file, v2_file):
    """Compare two digest HTML versions"""
    # Retorna dict com diferenças detectadas
    return {
        'size_diff': size2 - size1,
        'new_sections': [...],
        'removed_sections': [...],
        'content_changes': {...}
    }
```

## Arquivos de Referência
- `COMPARISON_REPORT.md` - Relatório detalhado de mudanças
- `/comparison/checksums/` - Hashes de versões conhecidas
- `/comparison/metrics/` - Métricas por versão

## Sinais de Versão "Falsa"
⚠️ **Alerta:** Se hash MD5 dos HTMLs são idênticos, a versão NÃO trouxe mudanças.
⚠️ **Alerta:** Se data no HTML está estática (não atualizada), o sistema está quebrado.