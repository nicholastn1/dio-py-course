menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor < 0:
            print("Valor inválido!")
            continue
        saldo += valor
        extrato += f"Depósito: {valor}\n"
        print(f"Depósito de {valor} realizado com sucesso!")

    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido!")
            continue
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > saldo:
            print("Saldo insuficiente!")
            continue
        if valor > limite:
            print("Limite de saque excedido!")
            continue
        saldo -= valor
        extrato += f"Saque: {valor}\n"
        numero_saques += 1
        print(f"Saque de {valor} realizado com sucesso!")

    elif opcao == "e":
        print(f"Saldo: {saldo}")
        print(f"Limite: {limite}")
        print(f"Extrato: {extrato}")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Insira uma opção válida.")
