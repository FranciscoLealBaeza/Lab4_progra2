def contador_10_a_15():
    n = 10
    def siguiente():
        nonlocal n
        valor = n
        n +=1
        return valor
    return iter(siguiente,16)

cont = contador_10_a_15()
print(next(cont))#10
print(next(cont))#11
print(next(cont))#12
print(next(cont))#13
print(next(cont))#14
print(next(cont))#15
#print(next(cont)) StopIteration