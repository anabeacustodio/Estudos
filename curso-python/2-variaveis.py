# Variáveis e tipos de dados “basicos”
# Uma variável é um espaço na memória onde armazenamos um valor.

# <nome da var> = <valor>

nome = 'Beatriz'    # variável do tipo string (texto), sempre entre aspas ('' OU "")
idade = 24          # var do tipo inteiro (núm sem casas decimais)
altura = 1.60       # var do tipo float (núm com casas decimais)
dev = True          # var do tipo booleana, valores lógicos (true/false)

# print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")
# f= format, pq vamos formatar uma frase utilizando variaveis

nome = input("Digite seu nome: ")               # entrada de texto
idade = int(input("Digite sua idade: "))        # entrada de testo convertida para inteiro
altura = float(input("DIgite sua altura: "))    # entrada convertida para float

print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")