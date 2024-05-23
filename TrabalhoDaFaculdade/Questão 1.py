print("Boas vindas a loja do Kaio Gouveia.")

#NOTA:O valor do produto é 100 (Questão 1 [TRABALHO])
produto = int(input('Digite quantos perfumes vai querer (cada perfume custa R$100):'))

produto = produto * 100


#Deixar as coisas nessa ordem do maior ao menor
#prints com seus resultados inteiros, ao fim do código resultado com desconto
if (produto >= 10000):
    desconto = produto * 0.11
    resultado = produto
    print(f'O preço total é {resultado}.')

elif (produto >= 6000 < 10000):
    desconto = produto * 0.07
    resultado = produto
    print(f'O preço total é {resultado}.')

elif(produto >= 2500 < 5999):
    desconto = produto * 0.04
    resultado = produto
    print(f'O preço total é {resultado}.')

#colocando um valor menor que 2500 haverá o resultado com e sem desconto,mas vai aparecer uma mensagem dizendo "O preço total com o desconto é"
#Mesmo assim ambos terão a resposta correta

else:
    resultado = produto
    print(f'O preço total é {resultado}.')
    desconto = 0

resultado = produto - desconto
print(f'O preço total com o desconto é {resultado}.')