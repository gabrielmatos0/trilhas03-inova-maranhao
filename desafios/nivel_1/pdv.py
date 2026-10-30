lista_compras = []

while True:
    # entradas
    cont_descontos = 0
    valor_original = float(input('Digite o valor da compra (ex: 1250.50): (0 pra encerar)\n>>> ').strip())
    if not valor_original:
        break
    valor_final = valor_original

    qtd_itens = int(input('Qtd. de itens:\n>>> ').strip())
    idade = int(input('Digite a sua idade: ').strip())
    cupom = input('Cupom de fidelidade: ').strip()

    # validar entradas
    if idade < 0 or valor_original < 0:
        print('Números negativos não são permitidos. Tente novamente...\n')
        continue
    if qtd_itens <= 0:
        print('Informe uma quantidade de itens válida. Tente novamente...\n')
        continue

    # aplicar descontos (requisitos funcionais)
    if idade >= 65:
        valor_final -= valor_original * 0.2
        cont_descontos += 1
        print(' - Desconto de 20% por idade aplicado!')

    if valor_final > 100:
        valor_final *= 0.9
        cont_descontos += 1
        print(' - Desconto de 10% por preço aplicado!')

    # descontos extras (tarefa bônus) (pela qtd de itens e pelo cupom) 
    if qtd_itens > 3:
        valor_final -= valor_original * 0.05
        cont_descontos += 1
        print(' - Desconto de 5% pela qtd. de itens aplicado!')
    if cupom == 'FIDELIDADE10':
        valor_final -= valor_original * 0.1
        cont_descontos += 1
        print(' - Desconto de 10% pelo cupom aplicado!')

    # armazenar compra
    print('Valor Final: R$ %.2f' % valor_final, end="\n\n")
    lista_compras.append([valor_original, valor_final, cont_descontos])


# mostrar e armazenar resumo do dia
texto = f'''
RESUMO DO DIA
Total de compras: {len(lista_compras)}
Total bruto: R$ {sum(map(lambda x: x[0], lista_compras)):.2f}
Total de descontos: {sum(map(lambda x: x[2], lista_compras)):.2f}
Total final: R$ {sum(map(lambda x: x[1], lista_compras)):.2f}
'''

print(texto)

with open('resumo.txt', 'w') as arquivo:
    arquivo.write(str(lista_compras) + '\n')
    arquivo.write(texto)
