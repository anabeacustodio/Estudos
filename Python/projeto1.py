# Jogo de adivinhação

# No jogo, o usuário precisa adivinhar um número secreto.
# Ele pode tentar várias vezes até acertar.

numero_secreto = 19  # Número que o usuário precisa adivinhar
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe o número secreto (entre 1 e 20): "))
    
    if tentativa < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif tentativa > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você adivinhou o número secreto.")
# Fim do jogo