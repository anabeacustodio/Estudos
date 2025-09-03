# União de Conceitos

# TOdas as estruturas podem ser usadas separadamente, mas em um programa "real", vamos unindo todas as estruturas para criarmos os cenários que precisamos para resolver um problema

# Exemplo:

# Você quer saber se uma palavra contém a letra Y

palavra = "Python"

# for letra in palavra:
#     if letra == "Y":
#         print("Essa plavra tem a letra Y maiúscula!")
#     elif letra == "y":
#         print("Essa plavra tem a letra y minúscula!")

letraProcurada = "h"

for letra in palavra:
    if letra == letraProcurada:
        print("Essa palavra tem a letra", letraProcurada)