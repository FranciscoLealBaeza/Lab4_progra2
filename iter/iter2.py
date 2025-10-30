class Impares1a20:
    def __iter__(self):
        # genera impares desde 1 hasta 19
        for n in range(1, 21, 2):
            yield n

# Uso
for i in Impares1a20():
    print(i)