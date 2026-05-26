##Juntando tudo (Listas e Cálculos)
#Crie um programa que peça a idade de 4 pessoas.

#Guarde todas as idades digitadas em uma lista.
#Usando um loop for, some todas as idades e mostre o resultado final da soma. 
#Mostre também qual foi a maior idade digitada usando a função max() e a menor idade usando a função min().

idades = []
soma = 0
for i in range(4):
    print("%i* Pessoa" %(i+1))
    idade = int(input("Digite sua idade: "))
    soma += idade
    idades.append(idade)

menor = min(idades)
maior = max(idades)
somasum = sum(idades)

print("Soma: %i\nIdade  menor: %i\nIdade maior: %i\nSomasum: %i"%(soma, menor, maior, somasum))