'''

un programa que solicite el ingreso de un número real. Luego el
programa deberá mostrar la descomposición  del número real en su parte
entera y su parte decimal, como bien muestra el ejemplo.
Ejemplo de pantalla de salida: 
Ingrese Numero:  
​
43.1418
Los resultados para 43.1418 son:
Parte entera: 43
Parte decimal: 0.1418

'''
print ("Ingrese numero", end=" ")
num = float(input())

entero = int(num)
decimal=abs(num) - abs(int(num))
print("parte entera" , entero)
print("parte decimal {0:.4f}".format(decimal))
