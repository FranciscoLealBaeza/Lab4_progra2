from functools import reduce

# Lista de cadenas; se corrige y normaliza la entrada para evitar errores
cadenas = ["Hola", " ", "Mundo", "!"]

# reduce concatena las cadenas en orden
concatenado = reduce(lambda a, b: a + b, cadenas)

# Resultado esperado: "Hola Mundo!"
print(concatenado)