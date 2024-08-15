
cliente1_nome = input("Digite o nome do cliente 1: ")
cliente1_idade = int(input("Digite a idade do cliente 1: "))

cliente2_nome = input("Digite o nome do cliente 2: ")
cliente2_idade = int(input("Digite a idade do cliente 2: "))

cliente3_nome = input("Digite o nome do cliente 3: ")
cliente3_idade = int(input("Digite a idade do cliente 3: "))


quarto_cliente1 = input("Escolha o quarto para cliente 1 (Simples, Duplo, Luxo): ").strip().lower()
quarto_cliente2 = input("Escolha o quarto para cliente 2 (Simples, Duplo, Luxo): ").strip().lower()
quarto_cliente3 = input("Escolha o quarto para cliente 3 (Simples, Duplo, Luxo): ").strip().lower()

dias_cliente1 = int(input("Quantos dias o cliente 1 ficará no hotel? "))
dias_cliente2 = int(input("Quantos dias o cliente 2 ficará no hotel? "))
dias_cliente3 = int(input("Quantos dias o cliente 3 ficará no hotel? "))

preco_simples = 100.00
preco_duplo = 150.00
preco_luxo = 250.00

if quarto_cliente1 == "simples":
    valor_cliente1 = preco_simples * dias_cliente1
elif quarto_cliente1 == "duplo":
    valor_cliente1 = preco_duplo * dias_cliente1
elif quarto_cliente1 == "luxo":
    valor_cliente1 = preco_luxo * dias_cliente1
else:
    valor_cliente1 = 0

if quarto_cliente2 == "simples":
    valor_cliente2 = preco_simples * dias_cliente2
elif quarto_cliente2 == "duplo":
    valor_cliente2 = preco_duplo * dias_cliente2
elif quarto_cliente2 == "luxo":
    valor_cliente2 = preco_luxo * dias_cliente2
else:
    valor_cliente2 = 0


if quarto_cliente3 == "simples":
    valor_cliente3 = preco_simples * dias_cliente3
elif quarto_cliente3 == "duplo":
    valor_cliente3 = preco_duplo * dias_cliente3
elif quarto_cliente3 == "luxo":
    valor_cliente3 = preco_luxo * dias_cliente3
else:
    valor_cliente3 = 0


print(f"\nResumo da estadia:")
print(f"Cliente 1 ({cliente1_nome}): R$ {valor_cliente1:.2f}")
print(f"Cliente 2 ({cliente2_nome}): R$ {valor_cliente2:.2f}")
print(f"Cliente 3 ({cliente3_nome}): R$ {valor_cliente3:.2f}")
