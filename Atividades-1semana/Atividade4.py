#Em uma turma, as notas finais de 4 alunos precisam ser classificadas.
#Faça um programa em Python que:

#Peça a nota de cada aluno (de 0 a 10)
#Para cada nota, mostre:
#"Aprovado" se nota >= 7
#"Recuperação" se nota >= 5 e < 7
#"Reprovado" se nota < 5
#Ao final, exiba quantos alunos ficaram Aprovados, quantos em Recuperação e quantos Reprovados.
#Desenvolva o programa utilizando laço for e estruturas condicionais.

Aprovados = 0
Recuperação = 0
Reprovados = 0

for i in range(4):
    print("Aluno numero", i+1)
    notafinal = float(input("Digite sua nota(0 a 10): "))
    if(notafinal >= 7):
        print("Aprovado!")
        Aprovados += 1
    elif(notafinal >= 5):
        print("Recuperação")
        Recuperação += 1
    else:
        print("Reprovado")
        Reprovados += 1

print("Quantidade de alunos: \nAprovado: %i\nRecuperação: %i\nReprovados %i\n" %(Aprovados, Recuperação, Reprovados))