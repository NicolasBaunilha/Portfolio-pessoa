import textwrap

print("Seja Bem vindo! O qual operação deseja realizar?")

def menu():
    menu = """
    -------MENU-------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    [nu]\tCriar Usuário
    [nc]\tCriar Conta
    [lc]\tListar Contas
    ------------------
    """
    return input(textwrap.dedent(menu))

def main():
    SAQUES_DIARIOS = 3
    LIMITE_DO_SAQUE = 500
    AGENCIA = "0001"

    saldo = 0.0
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

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

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(AGENCIA, numero_conta, usuarios)

        elif opcao == "lc":
            listar_contas(contas)

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

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente em números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("@@@ Já existe usuários com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigle estado): ")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario (smente em números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrada, fluxo de criação de conta interrmpido @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

if __name__ == "__main__":
    main()

print("Processos finalizados.")