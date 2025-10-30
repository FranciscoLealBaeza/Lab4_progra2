class cuadrados:
    def __iter__(self):# definimos la funcion __iter__ par que las instancias de la clase sean iterables
        for numero in range(1,11):
            yield numero * numero#entrega los cuadrados de los numeros


for i in cuadrados():
    print(i)