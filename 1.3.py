'''
Desarrollar 
​
un programa que solicite el ingreso de dos números enteros. Luego
el programa deberá mostrar por pantalla el resultado de sumar, restar
multiplicar y dividir dichos números ingresados
Ingrese Numero 1:  
​
4
Ingrese Numero 2:  
​
2
Los resultados para 4 y 2 son:
La suma: 6
La resta: 2
La división: 2
La multiplicación:  8

'''

num1 = int(input("ingrese numero 1\n"))
num2 = int(input("ingrese numero 2\n"))


suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multi = num1 * num2

print("La suma es:" , suma)
print("La resta es:" , resta)
print("La division es:", int(division))
print("La multiplicaciòn es:", multi)
