# Porsche Digest Version Control - References

## Checksums Conhecidos

| Versão | Arquivo | MD5 Hash | Data | Status |
|---|---|---|---|---|
| V5-atual | index.html | atualizar após deploy | 27/08/2026 | ✅ Deploy |
| V4-final | index-v4.html | xxxxxxxx | 20/08/2026 | ❌ Obsoleto |

## Checklist de Validação Antes do Deploy
- [ ] HTML hash diferente da última versão
- [ ] Data no footer atualizada
- [ ] Novas seções adicionadas
- [ ] Nenhum link quebrado
- [ ] Performance sem degradação

## Diferenças V7 vs V5 (MAGNA)

### Novas Seções (8 vs 6)
1. **Market Dashboard** - dados em tempo real
2. **Valuation Analysis** - charts interativos

### Novos Dados
- **+5 leilões** adicionados (15 vs 10)
- **Preços específicos** de BAT/CarsBids
- **Conversão BRL automática** (5.18 rate)

### Persona Detalhes
- **Driver Zone:** Perfil completo Daniel Costa
- **Collector Corner:** Análise de investimento
- **Custom Shop:** Guides técnicos

## Comando de Verificação
```bash
# Gerar hash e comparar
python compare_versions.py --current --previous
# Deve retornar: "EVOLVED: 15,243 bytes diferentes"
```