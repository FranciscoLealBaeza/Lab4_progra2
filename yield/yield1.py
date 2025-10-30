def primeros_10_numeros_pares():
    numero = 0 #contador para dar fin al bucle while
    while numero < 10:
        yield 2 * numero #multiplia el numero actual por 2 para convertirlo en par
        numero += 1

for n in primeros_10_numeros_pares():#imprime mediante un ciclo for cada resultaddo.
    print(n)