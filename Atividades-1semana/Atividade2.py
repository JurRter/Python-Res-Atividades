#Desenvolva um algoritmo em Python que receba do usuário o valor de uma compra.
#Em seguida, aplique as seguintes regras de desconto:

#Se o valor for maior que 200, aplique desconto de 15%
#Se o valor for de 100 a 200(incluso), aplique desconto de 10%
#Se o valor for menor que 100, não aplique desconto
#Mostre na tela o valor do desconto e o valor final a pagar.

# Escreva o programa usando if, elif e else.

valor = float(input("Digite o valor da compra: "))

if(valor > 200):
    valordesconto = valor - valor*0.15
    print(valordesconto, "Valor economizado com o desconto de 15%: ", valor*0.15)
elif(valor >= 100):
    valordesconto = valor - valor*0.1
    print(valordesconto, "Valor economizado com o desconto de 10%: ", valor*0.1)
else:
    print(valor, "Não ouve nenhum desconto!")