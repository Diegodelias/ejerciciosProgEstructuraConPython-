'''
1.2.
Desarrollar un programa que solicite por teclado dos
lados de un rectángulo. Luego calcularel perímetro
y área del mismo. Mostrar los resultados dela siguiente forma:
Ingresar Lado 1: 
​
20
Ingresar Lado 2: 
​
10
Área:       200
Perímetro:   60
'''
lado1 = int(input("Ingresar lado 1 \n"))
lado2 = int(input("Ingresar lado 2 \n"))

perimetro =  2 * (lado1 + lado2)
area = lado1 * lado2

print("El perimetro del rectangulo es:" , perimetro)
print("EL area del rectangulo es :", area)
