# Genera cuadrados solo para n pares en el rango 1..20
cuadrados_pares = [n * n for n in range(1, 21) if n % 2 == 0]

# Uso
print(cuadrados_pares)