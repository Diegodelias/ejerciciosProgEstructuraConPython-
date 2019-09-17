"""
numeros primos inneficiente
num=79865656565
contPrim= 0

for i in range(1 , (num + 1)):
#    print("for 1" ,i)
   
        if (num % i == 0):
#            print("jota" , j)
#            print("modulo" , (num % j))
            contPrim = contPrim + 1

print (contPrim)
"""
"""NUMERO COMPUESTO
Sabemos que si un número es divisible o múltiplo de otro, entonces cualquier producto de ese número también lo és.
Por esto si dividimos por un número compuesto (que es el producto de al menos un primo), será divisible también por este primo, por eso:

Para saber si un número es primo basta con mirar si es divisible entre algún primo hasta el número.

"""
            
import math

num = 79865656565
def esPrimo(num):
    for i in range(2, int(math.sqrt(num)+1)):
        #print( int(math.sqrt(num)))
        #print(i)
#        print( int(math.sqrt(num)))
       # print (num)
        if num % i == 0:
            return False
    return True

print(esPrimo(num))


