# devuelve None si la lista está vacía
primero_seguro = lambda lst: lst[0] if lst else None
print(primero_seguro([]))     # None