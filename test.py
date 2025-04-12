# escopo global o sistema pega 2 numeros do usuario


# função somar
def somar_2numeros(numero1, numero2):
    return numero1 + numero2

# função subtrair
def sub_2numeros(n1, n2):
    return n1 - n2

# função multiplicar
def mul_2numeros(n,k):
    return n * k

# função dividir
def div_2numeros(m, n):
    return float(m)/ n

#Faça um menu de escolha de operação matematica
def menu_operacao_matematica():
    menu = 1
    while menu == 1:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
        print("Esolha uma operação matemática")
        print("\nDigite 1.para Somar")
        print("Digite 2.para Subtrair")
        print("Digite 3.para Multiplicar")
        print("Digite 4.para Dividir")
        print("Digite 0.para Sair\n")

        escolha = input("Digite o numero da operação")
        resultado = 0
        if escolha == "1":
            resultado = somar_2numeros(n1,n2)
        elif escolha == "2":
            resultado = sub_2numeros(n1,n2)
        elif escolha == "3":
            resultado = mul_2numeros(n1,n2)
        elif escolha == "4":
            resultado = div_2numeros(n1,n2)
        else:
            menu = 0
        print(f"O resultado é: {resultado}")


# escopo global o resultado é mostrado
menu_operacao_matematica()