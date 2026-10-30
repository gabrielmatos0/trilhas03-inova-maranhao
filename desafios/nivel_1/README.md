# Sistema PDV

## Objetivo 🎯

Sistema de Ponto de Venda criado para registrar as informações de compras, aplicar os descontos necessários e, ao final, mostrar ao usuário um resumo detalhado das vendas do dia.

O software recebe as informações da venda (valor, quantidade de itens, idade do cliente e cupom aplicado) e, a partir desses dados, verifica se ele pode:

1. aplicar o desconto de 20% por idade (idade >= 65)
2. se esse valor já descontado é maior que 100, aplicar o desconto de 10% pelo valor
3. aplicar 5% de desconto se a quantidade de itens for maior que 3
4. aplicar 10% de desconto se o cupom recebido for FIDELIDADE10

O programa será encerrado ao digitar valor de compra 0 (zero)
## Como Rodar o Programa ⬇️

`python pdv.py`

## Como Testar o Sistema
> Aplique os dados abaixo no programa: (Valor e Idade)

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---|---|---|---|---|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |
