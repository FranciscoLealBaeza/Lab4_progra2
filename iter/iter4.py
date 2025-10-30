class MayusIterator:
    def __init__(self, lista_cadenas):
        # almacenamos la lista y el índice inicial
        self._lista = lista_cadenas
        self._i = 0

    def __iter__(self):
        # el iterador devuelve a sí mismo
        return self

    def __next__(self):
        # si se acaban los elementos, señalamos StopIteration
        if self._i >= len(self._lista):
            raise StopIteration
        # obtenemos la cadena actual, incrementamos el índice y devolvemos la versión en mayúsculas
        s = self._lista[self._i]
        self._i += 1
        return s.upper()

# Uso
frases = ["hola", "mundo", "python"]
for s in MayusIterator(frases):
    print(s)