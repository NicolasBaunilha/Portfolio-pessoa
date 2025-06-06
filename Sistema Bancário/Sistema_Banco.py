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
    limite_do_saque = 500
    extrato = ""
    numero_de_saques = 0
    SAQUES_DIARIOS = 3

    while True:

        opcao = menu()

        if opcao == "d":
            while True:
                try:
                    deposito = 0
                    deposito = int(input("\nInforme o valor que deseja depositar: "))
                    if deposito <= 0:
                        print("O valor que deseja depositar é inválido, insira um valor válido.")
                    else:
                        saldo += deposito
                        extrato += f"Depósito: R$ {deposito:.2f}\n-----------------------\n"
                        print("Depósito realizado com sucesso!")
                        break
                except ValueError:
                    print("Valor inválido. Por favor digite um número válido.")
        
        elif opcao == "s": 
            while True:
                try:
                    if numero_de_saques == SAQUES_DIARIOS:
                        print("Você já realizou a quantidade máxima de saques diários. Tente novamente amanhã.")
                        break
                    else:
                        pass
                    saque = 0
                    saque = int(input("\nInforme o valor que deseja sacar: "))
                    if saque <= 0 or saque > 500:
                        print("O valor que deseja depositar é inválido, insira um valor válido. (Acima de 0 e abaixo de 500)") 
                    else:
                        saldo -= saque 
                        extrato += f"Saque: R$ -{saque:.2f}\n-----------------------\n"
                        numero_de_saques += 1
                        print("Saque realizado com sucesso!" \
                        "")
                        break
                except ValueError:
                    print("Valor inválido. Por favor digite um número válido.")

        elif opcao == "e":
            print(f"Saldo atual: {saldo:.2f} \n\n-----------------------\n{extrato}")

        elif opcao == "q":
            print("Muito obrigado pela sua preferência, esperamos ter ajudado, até a proxima!")
            break

        else:
            print("O valor inserido não é uma opção válida, por favor insira um valor válido")
        
if __name__ == "__main__":
    main()

print("Processos finalizados.")