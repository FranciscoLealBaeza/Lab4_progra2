# Lista original
nums = [1,2,3,4,5,6,7,8,9,10]

# filter con lambda que deja solo los pares; convertimos a lista
pares = list(filter(lambda x: x % 2 == 0, nums))

# Uso
print(pares)  # [2, 4, 6, 8, 10]