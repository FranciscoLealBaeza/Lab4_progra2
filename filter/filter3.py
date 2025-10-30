nums = [10, 60, 30, 80, 50, 100]

# filter con lambda que selecciona valores estrictamente mayores que 50
mayores_50 = list(filter(lambda x: x > 50, nums))

# Uso
print(mayores_50)  # [60, 80, 100]