# Entrada: João
# Saída: Olá, João! Seja bem-vindo

#1,2 passo
# nome = input("Digite seu nome: ")

#3 passo
# print(f"Olá, {nome}! Seja bem vindo ")


# Solicite um número e diga se ele é par ou ímpar.
# Dica: use o operador %.
# numero = int(input("Digite um numero: "))

# if numero%2 == 0 :
#     print("Seu nuemro é par")
# else:
#     print("Seu numero é impar")


# Crie uma lista vazia chamada nomes. Peça ao usuário 3 nomes e adicione-os à lista. Depois,
# mostre todos os nomes cadastrados.
# listaNomes = []

# #REPETE QUANTAS VEZES VOCE DEFINIR DENTRO DO RANGE
# for i in range(1,4):
#     nome = input(f"Digite o {i}° nome: ")
#     listaNomes.append(nome)

# #REPETE O NUMERO DE VEZES DE ITEMS DENTRO DE LISTAS
# for n in listaNomes:
#     print(n)


#-------------------------------------------

#função
def adiciona_nome(ls):
    ls.append(input("Digite um nome"))
    print(ls)

#função
def remove_nome(ls):
    ls.remove(input("Digite nome"))
    print(ls)
    
menu = 1
listaNomes = []
while menu==1:
    print("O que voce quer fazer?")

    print("1. Adicionar nomes")
    print("2. Remover nomes")

    escolha = input("Digite uma opção: ")

    if escolha == "1":
        adiciona_nome(listaNomes)
        menu+=1
    elif escolha == "2":
        remove_nome(listaNomes)
        menu+=1
    else: 
        print("Código inválido!")


#se a escolha for 1 executa função 1
#se a escolha for 2 executa a função 2
# Se for outra messagem de erro
