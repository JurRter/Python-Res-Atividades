#Elabore um programa em Python que solicite ao usuário a digitação de 6 números inteiros.
#Ao final, o programa deve exibir:

#Quantos dos números digitados são pares
#Quantos são ímpares
#Implemente a solução utilizando um laço de repetição e estrutura condicional para classificar os números.


impar = 0
par = 0

for i in range(6):
    print("Tentiva numero", i+1)
    valor = int(input("Digite seu numero: "))
    if(valor % 2):
        print("O valor e impar!!")
        impar = impar + 1
    else:
        print("O valor é par!!!")
        par += 1

print("Tivemos %i numeros pares e %i numeros impares" %(par,impar))