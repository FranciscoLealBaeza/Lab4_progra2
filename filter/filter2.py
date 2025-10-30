palabras = ["perro", "gato", "pato", "hamster"]

# filter con lambda que comprueba la primera letra (minúscula)
empiezan_p = list(filter(lambda s: s.startswith("p"), palabras))

# Uso
print(empiezan_p)  # ['perro', 'pato']