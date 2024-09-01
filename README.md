## Mapper em Python com JSON

Projeto de automação com Python para geração de um novo arquivo remapeado usando JSON.

Motivação: Normalizar uma base de dados de um sistema legado para uma base de dados corrente.

### Pré-requisitos
  - Python 3

### Objetivos
- [x] Traduzir o nome dos campos para inglês.
- [x] Converter o valor de venda de reais para centavos.
- [x] Remover o campo ativo.
- [x] Acrescentar o campo de custo.
- [x] Acrescentar o campo de quantidade.

### Antes
```json
{
  "data": [
    {"id": 1, "descricao": "shampoo", "valor": 20.5, "ativo": 1},
    {"id": 2, "descricao": "café", "valor": 10, "ativo": 1},
    {"id": 3, "descricao": "chocolate", "valor": 2, "ativo": 0}
  ]
}
```
*table-legacy.json*
### Depois
```json
{
  "data": [
    {"id": 1, "description": "shampoo", "priceInCents": 2050, "costInCents": 1025, "amount": 1},
    {"id": 2, "description": "café", "priceInCents": 1000, "costInCents": 500, "amount": 1},
    {"id": 3, "description": "chocolate", "priceInCents": 200, "costInCents": 100, "amount": 1}
  ]
}
```
*table-current.json*