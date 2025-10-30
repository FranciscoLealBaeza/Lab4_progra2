# Lista de palabras; se corrige la entrada "Ç++" por "C++"
palabras = ["python", "java", "C++", "ruby"]

# Comprensión que toma la primera letra de cada palabra
primeras_letras = [p[0] for p in palabras]

# Uso
print(primeras_letras)  # ['p', 'j', 'C', 'r']