# Simulando um caixa eletrônico

# O usuário tem um saldo inicial de R$500 e pode fazer saques até zerar o saldo ou encerrar.

saldo = 500  # Saldo inicial do usuário
saque = 0   

while saldo > 0:
    saque = float(input('Informe o valor do saque (ou digite 0 para sair): '))

    if saque == 0:
        break
    
    if saque > saldo:
        print('Saldo insuficiente! Saque não efetuado')
    else:
        saldo -= saque
        print(f'Saque efetuado! Novo saldo: R${saldo:.2f}')

print('Operação finalizada!')