# Inserir o valor da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Desconto com base na tabela
if valor_compra <= 1000:
    desconto = valor_compra * 0.10  # 10% de desconto
elif valor_compra <= 5000:
    desconto = valor_compra * 0.20  # 20% de desconto
else:
    desconto = valor_compra * 0.30  # 30% de desconto

# Calcula o valor final com o desconto
valor_final = valor_compra - desconto

# Exibe o valor do desconto e o valor final
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")