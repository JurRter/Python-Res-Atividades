##Trabalhando com Listas
#Crie um programa que tenha uma lista vazia chamada frutas.

#Peça ao usuário para digitar o nome de 3 frutas e adicione cada uma delas à lista usando o método append().
#Use um loop for para imprimir o nome de todas as frutas inseridas.
#Depois, altere o valor da segunda fruta (índice 1) para "Banana" e imprima a lista completa novamente

Frutas = []

for i in range(3):
    fruta = str(input("Digite a %i* fruta: " %(i+1)))
    Frutas.append(fruta)

for i in range(3):
    print("A %i* fruta é: %s" %(i+1, Frutas[i]))

print("Alterando a fruta de indice 1 para banana!")
Frutas[1] = "Banana"

for i in range(3):
    print("A %i* fruta é: %s" %(i+1, Frutas[i]))