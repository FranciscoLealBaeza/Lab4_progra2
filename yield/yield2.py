numeros= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]#lista de numeros

def numeros_impares(lista):#se entrega una lista
    for i in lista: #se recorre la lista entregada
        if i%2 != 0:#si el numero deja residuo al ser dividido en 2, es impar
            yield i #entrega el numero

for n in numeros_impares(numeros): # recorre la lista numeros
    print(n) # imprime los numeros que pasen el booleano