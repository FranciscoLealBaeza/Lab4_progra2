from functools import reduce

# Lista de entrada
nums = [2, 3, 4]

# reduce aplica una función acumuladora que multiplica dos valores a la vez
producto_total = reduce(lambda a, b: a * b, nums)

# Resultado esperado: 24
print(producto_total)