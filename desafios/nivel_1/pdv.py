lista_compras = []

while True:
    cont_descontos = 0
    valor_original = float(input('Digite o valor da compra (ex: 1250.50): (0 pra encerar)\n>>> ').strip())
    if not valor_original:
        break
    valor_final = valor_original

    idade = int(input('Digite a sua idade: ').strip())

    if idade < 0 or valor_original < 0:
        print('Números negativos não são permitidos. Tente novamente...\n')
        continue

    if idade >= 65:
        valor_final *= 0.8
        cont_descontos += 1
        print(' - Desconto de 20% por idade aplicado!')

    if valor_final > 100:
        valor_final *= 0.9
        cont_descontos += 1
        print(' - Desconto de 10% por preço aplicado!')


    print('Valor Final: R$ %.2f' % valor_final, end="\n\n")
    lista_compras.append([valor_original, valor_final, cont_descontos])


print('RESUMO DO DIA')
print('Total de compras:', len(lista_compras))
print('Total bruto: R$ %.2f' % sum(map(lambda x: x[0], lista_compras)))
print('Total de descontos:', sum(map(lambda x: x[2], lista_compras)))
print('Total final: R$ %.2f' % sum(map(lambda x: x[1], lista_compras)))
