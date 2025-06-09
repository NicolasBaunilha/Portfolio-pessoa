import textwrap

print("Seja Bem vindo! O qual operação deseja realizar?")

def menu():
    menu = """
    -------MENU-------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
     
    """
    return input(textwrap.dedent(menu))

def main():
    saldo = 0.0
    LIMITE_DO_SAQUE = 500
    extrato = ""
    numero_de_saques = 0
    SAQUES_DIARIOS = 3

    while True:
        opcao = menu()

        if opcao == "d":
            try:
                valor = float(input("Insira o valor do deposito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "s": 
            try:
                saque = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_de_saques = sacar(
                    saldo=saldo,
                    saque=saque,
                    extrato=extrato,
                    LIMITE_DO_SAQUE=LIMITE_DO_SAQUE,
                    numero_de_saques=numero_de_saques,
                    SAQUES_DIARIOS=SAQUES_DIARIOS
                    )
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            break

        else:
            print("O valor inserido não é uma opção válida, por favor insira um valor válido")

def sacar(*, saldo, saque, extrato, LIMITE_DO_SAQUE, numero_de_saques, SAQUES_DIARIOS ):
    if numero_de_saques >= SAQUES_DIARIOS:
        print("Limite diário de saques atingido.")
    elif saque > saldo:
        print("Saldo insuficiente.")
    elif saque > LIMITE_DO_SAQUE:
        print("Valor excede o limite permitido.")
    elif saque <= 0:
        print("Valor inválido.")
    else:
        saldo -= saque
        extrato += f"Saque: R$ -{saque:.2f}\n"
        numero_de_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_de_saques

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Valor inválido para depósito.")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    return saldo, extrato
                
def exibir_extrato(saldo, extrato):
    print(f"Saldo atual: {saldo:.2f} \n\n-----------------------\n{extrato}")

if __name__ == "__main__":
    main()

print("Processos finalizados.")