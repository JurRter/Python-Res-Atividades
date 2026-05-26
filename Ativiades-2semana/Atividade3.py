##Matrizes simples
#Dada a matriz abaixo (uma lista de listas) que representa as notas de 2 alunos em 3 provas:
#notas_alunos = [
#    [7.5, 8.0, 9.0], 
#    [6.0, 7.5, 8.5]
#]
#Faça um print para exibir especificamente a nota 8.5 acessando os índices corretos (linha e coluna).
#Use um loop for aninhado (um for dentro de outro for) para percorrer a matriz e imprimir todas as notas, uma por uma.

notas_alunos = [
   [7.5, 8.0, 9.0], 
   [6.0, 7.5, 8.5]
]

print(notas_alunos[1][2])

for aluno in range(2):
    print("Aluno %i: " %(aluno+1))
    for prova in range(3):
        print("Prova %i: " %(prova+1))
        print(notas_alunos[aluno][prova])