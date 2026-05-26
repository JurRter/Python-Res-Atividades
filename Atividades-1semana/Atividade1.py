# Faça um programa em Python que pede ao usuário para digitar uma senha.
# Se a senha digitada for exatamente igual a "python123", o programa deve imprimir "Acesso permitido". Caso contrário, o programa deve imprimir "Acesso negado".

# Implemente a solução usando estruturas condicionais. 

senha = str(input("Digite sua senha: "))


if (senha == "python123"):
    print("Acesso permitido")
else:
    print("Acesso negado")    