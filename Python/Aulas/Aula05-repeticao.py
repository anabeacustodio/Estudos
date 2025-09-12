# Laços de Repetição (for e while)

# Imagine que você precisa pedir para alguém contar de 1 a 100 e escrever cada número em um papael. Fazer isso manualmente seria muito cansativo e demorado, né?

# Agora, imagine que um programa pode fazer essa contagem automaticamente, sem precisar repetir o mesmo comando 100 vezes. É exatamente isso que os laços de repetição fazem!

# Os laços de repetição são usados para executar um bloco de código várias vezes, até que uma condição seja atingida.

# Python tem dois tipos principais de laços:

# for ➡️ Quando sabemos quantas vezes queremos repetir algo.
# while ➡️ Quando queremos repetir algo até que uma condição se torne falsa.

#-------------------------------------------------------------
# FOR

# O FOR é usado quando sabemos quantas vezes queremos repetir um bloco de código.
# Ele percorre uma sequência de valores, como uma lista, um intervalo de números ou até mesmo letras de uma palavra.

# Estrutura:

# for variável in sequência:
#     # Código a ser repetido

# EX.1: Contando de 1 a 5 com o FOR

# for numero in range(1, 6):
#     print(numero)

# O range(a, 6) gera números de 1 a 5, o último numero range não é incluído

# EX.2: Percorrendo uma lista de compras

# compras = ['Arroz', 'Feijão', 'Leite', 'Ovos']

# for item in compras:
#     print(f'Comprar: {item}')

# EX.3: Percorrendo as letras de uma palava

# palavra = 'Python'

# for letra in palavra:
#     print(letra)

#-------------------------------------------------------------
# WHILE

# O WHILE é usado quando não sabemos quantas vezes a repetição vai acontecer, mas sabemos a condição que deve ser atendida para continuar.

# while condição:
#     # Código a ser repetido enquanto a condição for verdadeira

# obs: Cuidado com loops infinitos!
# Se a condição nunca mudar para false, ocóigo nunca para de rodar.

# EX.1: Contagem regressiva

# contador = 5

# while contador > 0:
#     print(contador)
#     contador -= 1 # Diminui 1 do contador de cada repetição

# print("🚀 Fogo!")

# EX.2: Pedindo senha até acertar

senha_correta = '1234'
senha = ''

while senha != senha_correta:
    senha = input('Digite a senha: ')

print('Acesso permitido!')