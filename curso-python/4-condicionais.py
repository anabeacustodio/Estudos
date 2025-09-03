#CONDICIONAIS

# São estruturas que permitem ao nosso programa tomar decisões com base em determinadas condições. Ou seja, o programa pode executar ações diferentes dependendo de uma situação específica.

# Exemplo:

# Você está em uma cafeteria e está com pouca grana.
# O cappucino custa 10 reais, café com leite 7 e o café expresso 4.

# Se você tiver 10 reais ou mais na carteira, pode pedir o cappucino
# Se você tiver 7 reais ou mais, pode pedir o café com leite.
# Se não, pede o café expresso.

# Sintaxe básica no Python!

# if = "se"
# else = "senão"
# elif = se + se não

# if condição: 
    # Código a ser executado se a condição for verdadeira
# elif outra_condição:
    # Código executado se a primeira condição for falsa, mas essa for verdadeira
# else:
    # Código executado se nenhuma das condições anteriores forem verdadeiras
    # condição default = se nada certo, vai acontecer isso

# EXEMPLOS

# 1 - Verificando a idade para entrada em um evento (18 ANOS)

# idade = int(input("Digite sua idade: ")) # Usuário digita a idade

# if idade >= 18:
#     print("Você pode entrar no evento!")
# else:
#     print("Desculpe, você ainda não tem idade suficiente para entrar.")

# 2 - Verificando a nota de um aluno

nota = float(input("Digite sua nota: ")) # usuário insere a nota

if nota >= 7:
    print("Parabéns! Você passou de ano!")
elif nota >=5:
    print("Você está de recuperação. Estude mais e tente novamente.")
else:
    print("Infelizmente, você foi reprovado. Tente novamente no próximo ano.")