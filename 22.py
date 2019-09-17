'''

Desarrollar la función producto que recibe por parámetro dos números enteros
y natural de 3 cifras. El función será utilizada con fines
didácticos a fin de enseñar (mostrar) el método para obtener el
resultado de un producto de números.Se pide que la función muestre por
pantalla los pasos y cálculos intermediosde la multiplicación tal
como se hacen sobre una hoja de papel, respetando exactamente las
alineaciones y forma para la salida como bien se ilustra en el ejemplo
de salida. Utilizar la función en un programa que solicitará al usuario
el ingreso de dos números enteros y naturales, luego invocar a la función 
​producto  pasando por parámetro dichos números ingresados

Ejemplo de salida:
Ingrese el multiplicando: 123
Ingrese el multiplicador: 456
       123
x      456
----------
       738
+     615-
     492--
----------
     56088
     
     mportante
​
:
Investigar como python puede dar formatos específicos a un string.
Ir al sitio https://pyformat.info/ y estudiar el uso del método
​.format. 

entrada_: dos nuemeros enteros de e cifras


'''
def multiplicador(num1,num2):
    i = int(len(str(num2)))
    
    for x in range(i,0,-1):
        unidad = num2 % 10
        num2 = num2 // 10
        fila=unidad*num1
        if(x == 3):
            print('{:=10d}'.format(fila))
        elif (x==2):
              filastr = str(fila)
              filastr = filastr + "-" 
              print('+{:>9}'.format(filastr))
              #print('{:=+9d} '.format(fila,'-'))
        elif (x==1):
            filastr = str(fila)
            filastr = filastr + "--" 
            print('{:>10}'.format(filastr))
    

def producto(num1,num2):
    total = int(num1 * num2)
    print('{:=10d}'.format(num1))
    print('x','{:=8d}'.format((num2)))
    print('{:10}'.format('----------'))
    multiplicador(num1,num2)
    print('{:10}'.format('----------'))
    print('{:=10d}'.format(total))
    
def main():
    print("ingrese multiplicando:",end=" ")
    multiplicando = int(input())
    print("ingrese multiplicador:",end=" ")
    multiplicador = int(input())
   
    producto(multiplicando,multiplicador)
   
   
main()
    
    
