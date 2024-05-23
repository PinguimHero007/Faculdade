print('Boas vindas a soverteria de Açaí e Cupuaçu do Kaio Gouveia')

print ('-' * 18 + 'Cardapio' + '-' * 19)
print ('-' * 45)
print('----| Tamanho | Cupuaçu (CP)| Açaí (AC) |----')
print('----|    P    |    R$9.00   |  R$11.00  |----')
print('----|    M    |    R$14.00  |  R$16.00  |----')
print('----|    G    |    R$18.00  |  R$20.00  |----')
print ('-' * 45)

#Acumuladores
totalP = 0
totalM = 0
totalG = 0

#CP vai gerar todas essas condições abaixo
sabor = (input('Entre com o sabor desejado (CP/AC):'))

if sabor == 'CP':

    tamanho = (input('Entre com o tamanho desejado (P/M/G):'))

    if tamanho == 'P':
        print(input('você escolheu um Cupuaçu no tamanho P: R$9.00'))
        totalP += 9.00

    elif tamanho == 'M':
        print(input('você escolheu um Cupuaçu no tamanho M: R$14.00'))
        totalM += 14.00

    elif tamanho == 'G':
        print(input('você escolheu um Cupuaçu no tamanho G: R$18.00'))
        totalG += 18.00

#Caso o cliente erre vai gerar esse abaixo
    else:
        print('Erro, escolha um valor válido P, M, G')

#AC que vai gerar essas condições abaixo
elif sabor == 'AC':

    tamanho = (input('Entre com o tamanho desejado (P/M/G):'))

    if tamanho == 'P':
        print(input('você escolheu um Açaí no tamanho P: R$11.00'))
        totalP += 11.00

    elif tamanho == 'M':
        print(input('você escolheu um Açaí no tamanho M: R$16.00'))
        totalM += 16.00

    elif tamanho == 'G':
        print(input('você escolheu um Açaí no tamanho G: R$20.00'))
        totalG += 20.00

    else:
        print('Erro, escolha um valor válido P, M, G')


#Se cometer erro no sabor
else:
    print('Erro, escolha um sabor válido CP, AC')


#Acumuladores no final
print(f'Total acumulado para tamanho P: R${totalP:.2f}')
print(f'Total acumulado para tamanho M: R${totalM:.2f}')
print(f'Total acumulado para tamanho G: R${totalG:.2f}')
print(f'Total geral acumulado: R${totalP + totalM + totalG:.2f}')