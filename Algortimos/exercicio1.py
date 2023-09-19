#  Insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 5 e 3 ao mesmo tempo
if numero % 5 == 0 and numero % 3 == 0:
    print(f"{numero} é divisível por 5 e 3 ao mesmo tempo.")
else:
    print(f"{numero} não é divisível por 5 e 3 ao mesmo tempo.")



