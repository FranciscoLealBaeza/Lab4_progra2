# Lista de temperaturas en Celsius
celsius = [0, 10, 20, 30]

# Fórmula F = C * 9/5 + 32 aplicada con map y lambda
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

# Uso / salida esperada
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0]