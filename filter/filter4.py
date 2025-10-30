nums = [1,2,3,4,5,6,7,8,9,10]

# filter con lambda que deja solo los impares; convertimos a lista
impares = list(filter(lambda x: x % 2 != 0, nums))

# Uso
print(impares)  # [1, 3, 5, 7, 9]