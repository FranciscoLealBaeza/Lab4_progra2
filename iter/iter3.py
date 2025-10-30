class CuadradosLista:
    def __init__(self):
        # precomputamos los cuadrados y los guardamos en una lista
        self._cuadrados = [n * n for n in range(1, 11)]

    def obtener_todos(self):
        # devuelve la lista completa de cuadrados
        return self._cuadrados

# Uso
c = CuadradosLista()
print(c.obtener_todos())  # [1, 4, 9, ..., 100]