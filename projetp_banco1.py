menu = """""

[d]
[s]
[e]
[q]

=> """

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
limites_saques = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('qual valor sera digitado:'))

        if valor > 0:
            saldo += valor
            extrato += f'deposito: R$ {valor:.2f}\n'

        else:
            print('operacoes falhou! o valor informado e invalido')

    elif opcao == 's':
        valor = float(input("informe o valor de saque"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limites_saques

        if excedeu_saldo:
            print('operacao falhou! voce nao tem saldo')

        elif excedeu_limite:
            print('falhou! valor de saques excedidos')

        elif excedeu_saques:
            print('falhou! numero de saques excedidos ')

        elif valor > 0:
            saldo -= valor
            extrato += f'saque: R$ {valor:.2f}\n'
            numero_saque += 1

        else:
            print('Operacao falhou! valor e invalido')

    elif opcao == "e":
        print('extrato')
        print('nao ha movimentacoes.' if not extrato else extrato)
        print(f'saldo:R$ {saldo:.2f}')

    elif opcao =="q":
        print('operacao invalida, por favor escolha outra operacao')
