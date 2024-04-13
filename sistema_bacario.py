saldo = 0
numero_saques = 0
extrato = 0
LIMITE_SAQUES= 3
valor_total_saque_dia = 0

while True:

    operacao = input('Boa tarde! Qual operação você gostaria de realizar? (Deposito/Saque/Extrato/Sair)').lower().strip()

    if operacao == 'deposito':
        valor_depositado = float(input('Digite o valor a ser depositado: R$'))
        saldo += valor_depositado

    elif operacao == 'saque':
        valor_de_saque = float(input('Digite o valor a ser sacado: R$'))

        if valor_de_saque > saldo:
            print('Saldo insuficiente!')

        elif numero_saques >= LIMITE_SAQUES:
            print(f'Você atingiu o limite de {LIMITE_SAQUES} saques por dia.')

        elif valor_total_saque_dia + valor_de_saque > 500:
            print('O valor de saque excede o limite diário de R$500.')

        else:
            saldo -= valor_de_saque
            numero_saques += 1
            valor_total_saque_dia += valor_de_saque

    elif operacao == 'extrato':    
        extrato = saldo
        print(f'Boa Tarde! O seu extrato é de R${extrato:.2f}.')

    elif operacao == 'sair':
        break

   