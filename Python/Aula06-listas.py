# Listas e Tuplas

# Tipos de dados que armazenam múltiplos valores, mas têm diferenças importantes:

# LISTAS:
#   - Modificável (pode adicionar, remover e alterar valores)
#   - Mais lenta
#   - Quando precisamos modificar dados

# TUPLAS:
#   - Não é modificável (uma vez criada, não pode ser alterada)
#   - Mais rápida
#   - Quando os dados não devem ser alterados

#--------------------------------------------------------------

# LISTAS
# Definida entre colchetes [] e pode armazenar diferentes tipos de dados

frutas = ['maça', 'banana', 'laranja']
numeros = [1, 2, 3, 4, 5]
misturada = ['Python', 3.14, True]

# ***Acessando elementos da lista

# print(frutas[0])    # 'maça'
# print(frutas[1])    # 'banana'
# print(frutas[2])    # 'laranja'
# print(frutas[-1])   # 'laranja'(índice negativo conta de trá para frente)

# ***Alterando um valor na lista
# print(frutas)

# frutas[1] = 'uva'
# print(frutas) # ['maça', 'uva', 'laranja']

# ***Adicionando elementos à lista

# append(): adiciona um item ao final
# insert(): adiciona um item em uma posição específica

# numeros = [1, 2, 3]
# print(numeros)

# numeros.append(4)
# print(numeros) # [1, 2, 3, 4]

# numeros.insert(1, 10) # (posição, valor)
# print(numeros) # [1, 10, 2, 3, 4] (inseriu o 10 na posição 1)

# ***Removendo elementos da lista

# remove(): remove um item pelo valor
# pop(): remove um item pelo índice (ou o último item se nenhum índice for passado)

# frutas = ['maça', 'banana', 'laranja', 'uva']
# frutas. remove('banana')
# print(frutas) # ['maça', 'laranja']

# frutas.pop(0)
# print(frutas) # ['laranja', 'uva']

# frutas.pop()
# print(frutas) # ['laranja']

#--------------------------------------------------------------

# TUPLAS
# TUplas são como listas, mas imutáveis. Elas são criadas com parênteses ()

cores = ('vermelho', 'azul', 'verde')
numeros = (1, 2, 3, 4, 5)

# ***Acessando elementos
# print(cores[0]) # 'vermelho''
# print(cores[-1]) # 'verde''

# ***Tentando modificar uma tupla (Erro!)
# cores[1] = 'amarelo' # ❌ Isso gera um erro, pois tuplas são imutáveis!

# ***Convertendo entre lista e tupla
# Podemoos converter uma tupla para uma lista e modificar os elementos

# tupla = (1, 2, 3)
# lista = list(tupla) # Converte para lista
# lista.append(4)
# tupla = tuple(lista) # Converte de volta para tupla
# print(tupla) # (1, 2, 3, 4)

# ***Qunado usar tuplas?
# - Quando queremos garantir que os valores não sejam alterados.
# Para armazenar dados fixos como coordenadas, meses do ano, dias da semana, etc.

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril')
print(meses[2]) # 'Março'