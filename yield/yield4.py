def fibonacci(n):
    n1= 0 #primer numero
    n2= 1 #segundo numero
    contador = 0 
    while contador < n:
        yield n1 #entrega el valor actual
        n1 = n2 #el primer numero se convierte al valor del segundo
        n2 = n1+n2 #el segundo valor se suma con el primero
        contador +=1 

for i in fibonacci(10):
    print(i)