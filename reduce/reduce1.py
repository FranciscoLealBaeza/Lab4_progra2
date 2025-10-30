from functools import reduce

# Lista de entrada
nums = [5, 10, 15, 20]

# reduce aplica una función acumuladora que suma dos valores a la vez
suma_total = reduce(lambda a, b: a + b, nums)

# Resultado esperado: 50
print(suma_total)