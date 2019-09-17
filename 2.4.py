'''
2.4.
Programar una función ​ aleatorio que reciba como parámetros 2 números
naturales y retorne un número natural al azar comprendido entre estos 2
números (​ inclusive ) ​ , pasados por parámetro. Debe asumirse que esta función
será invocada de manera que el primer parámetro representa el límite inferior
del intervalo y el segundo el límite superior.
En un programa solicitar al usuario el ingreso de los límites del intervalo e
invoque a la función ​ aleatorio​ tres veces de la siguiente manera:
a. Invocarla con los extremos del intervalo ingresados por el usuario y
mostrar en pantalla el valor generado.
b. Invocarla como en el punto anterior (a), pero usando como extremo
inferior el valor generado en el punto anterior (a).
c. Invocarla como en el punto anterior (b), pero usando como extremo
superior el valor generado en el punto anterior (b).
Ingrese el limite inferior (numero natural): 14
Ingrese el limite superior (numero natural): 31
1-Límite inferior 14, limite superior 31. Numero generado: ​ 25
2-Límite inferior​ 2
5​ , limite superior 31. Numero generado:​ ​ 27
3-Límite inferior 2
5​ , limite superior 2
7​ . Numero generado: 25
'''
import random

def aleatorio(num1,num2):
    '''  '''
    res = 0
    
    for i in range(0,3):
        if (res > 0 and i ==1) :
            restemp= res
            res=random.randint(res, num2)
            print(i+1 ,"-Limite inferior" , restemp , "limite superior", num2 , "numero generado" , res)
        elif(res>0 and i ==2):
            suptemp= res
             
            res=random.randint(restemp, suptemp)
            print(i+1 ,"-Limite inferior" , restemp , "limite superior", suptemp, "numero generado" , res)
        elif(res==0):
            res=random.randint(num1,num2)
            print(i+1 ,"-Limite inferior" , num1 , "limite superior", num2 , "numero generado" , res)
        

    
    return res 



def main():
    
    
     
    print("Ingrese el limite inferior (numero natural):" ,end="")
          
    num1 = int(input())
    
    
    print("Ingrese el limite inferior (numero natural):" ,end="")
    
    num2 = int(input())
    
    
    aleatorio(num1,num2)
    
    
    
   
    
    
    
    
main()    
