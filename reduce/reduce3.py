from functools import reduce

# Lista de entrada
nums = [7, 3, 9, 1, 5]

# reduce compara acumulador y siguiente elemento, devolviendo el mayor de ambos
maximo = reduce(lambda a, b: a if a >= b else b, nums)

# Resultado esperado: 9
print(maximo)