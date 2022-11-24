def menu():
    menu = """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] lista contas
    [nu] Novo usuario
    [q] Sair

    
     => """""

    def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f'Deposito:R$ {valor:.2f}\n'
            print('Deposito realizado com sucesso!')
        else:
            print('Operacao falhou! valor informado é insulficiente')
        return saldo, extrato

    def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > limite_saques

        if excedeu_saldo:
            print('Operacao falhou! voce nao tem saldo suficiente')
        elif excedeu_limite:
            print('operacao falhou! O valor do saque excedeu o limite. ')

        elif excedeu_saques:
            print('Operacao falhou! Numero maximo de saques excedidos ')

        elif valor > 0:
            saldo -= valor
            extrato += valor
            extrato = f'saque: r$ {valor:.2f}\n'
            numero_saques += 1
            print('saque realizado com sucesso!')

        else:
            print('Operacao falhou! O valor informado é invalido')

        return saldo, extrato

    def exibir_extrato(saldo, /, *, extrato):
        print('--------EXTRATO--------')
        print('Nao foram realizadas movimentacoes' if not extrato else extrato)
        print(f'sALDO: R$ {saldo:.2F}')
        print('/////////////////////////')

    def criar_usuario(usuarios):
        cpf = input('Didite o cpf(somente numero):')
        usuario =  filtrar_usuario(cpf, usuarios)

        if usuario:
            print('Ja existe usuario com esse cpf:')
            return

        nome = input("Didite o nome completo")
        data_nascimento = input('Didite a data de nascimento(dd-mm-aaaa):')
        endereco = input('Digite o endereço(logadouro, nro - bairro - cidade/ estado):')

        usuarios.append({'nome': nome, 'data_nascimneto':data_nascimento, 'cpf': cpf, 'endereço': endereco})
        print('Usuario criado com secesso!')

    def filtar_usuario(cpf, usuarios):
        usuario_filtardos = [usuario for usuario in usuarios if usuario['cpf']**cpf]
        return usuarios_filtrados [0] if usuarios_filtrados else None

    def criar_conta(agencia, numero_conta, usuarios):
        cpf = input('Digite o cpf do usuario:')
        usuario = filtar_usuario(cpf, usuarios)

        if usuario:
            print('Conta criada com sucesso')
            return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
        print('Usuario nao encontrado, operacao de criaçao de conta encerrado')

    def listas_contas(contas):
        for conta in contas:
            linha = f"""\
            agencia:{conta['agencia']}
            c/c:{conta['nimero_conta']}
            titular:{conta['usuario']['nome']}
        """
        print('=' * 100)

    def main():
        LIMITE_SAQUES = 3
        AGENCIA = '0001'
        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = []
        usuarios = []
        contas = []
        listar_contas = []

        while True:
            opcao = menu()

            if opcao == 'd':
                valor = float(input('Digite o valor do deposito:'))

                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "s":
                valor = float(input('Digite valor do saque:'))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )

            elif opcao == 'e':
                exibir_extrato(saldo, extrato=extrato)

            elif opcao == 'nu':
                criar_usuario(usuarios)
            elif opcao == 'nc':
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)

                elif opcao == 'lc':
                    listar_contas(contas)

                elif opcao == 'q':
                    break

                else:
                    print('OPERACAO INVALIDA, FAVOR SELECIONAR OUTRA OPCAO')

        main()
























