'''
Programar las funciones ​ areaCirc ​ , ​ areaCuad ​ ​ y ​ areaNegra.
areaCirc ​ recibe como parámetro el ​ radio de un círculo y calcula y retorna el
área del mismo.
areaCuad ​ recibe como parámetro el ​ lado de un cuadrado y calcula y retorna
el área del mismo.
areaNegra ​ recibe como parámetro el ​ lado de un cuadrado de una figura
(como la dada a continuación) ​ y calcula y retorna el área negra resultante.
Luego utilizar las funciones en un programa que solicitará al usuario el lado
del cuadrado y mostrará por pantalla el valor correspondiente para el área de
color negra (​ Ver figura ) ​ y además indicará el porcentaje que éste área
representa con respecto al área total del cuadrado. ​ Notar que dado el lado del
cuadrado, la proporción de tamaño entre este y los círculos siempre es la
misma y esta proporción se debe deducir con los valores del ejemplo dado a
continuación.


Ingrese el lado: 12
El area negra es 68.60 y es un 47.64% del area total del cuadrado



'''
import math

def areaCirc(radio):
    area = math.pi * pow(radio,2)
    return area

def areaCuad(lado):
    area= pow(lado,2)
    return area

def calcularProporcion(lado,ratio):
    const= 3
    radioCir = ((lado / const) *  ratio) /2
#    print(radioCir)
    AreaCir = areaCirc(radioCir)
    return AreaCir

def porcentajeAreaNegra(lado):
    total = totalCirculos(lado) + areaNegra(lado)
    resultado= ((areaNegra(lado)) * 100) /total
    return resultado;

def totalCirculos(lado):
    '''calcula area total suma de todos los circulos'''
    AreaCirc_Grande = calcularProporcion(lado,2)
    AreaCirc_Chico= calcularProporcion(lado,1)
    AreaCirculos = AreaCirc_Grande + (AreaCirc_Chico * 2)
    
    return AreaCirculos
    

def areaNegra(lado):
   
    '''
    calcula el area negra resultante
    1-calcular area del cuadrado principal
    2- calcular los valores del area de los circulos internos
        ¿cual es la proporción entre el lado del cuadrado y el radio de los circulos?
        ratioCircGrande = 12/8 = 3 /2
        ratioCirculoChico = 12 /4 = 3 /1
        
        dividir el lado por el numerador y multiplicar  el resultado por el denominador
    3-restar  al area del cuadrado  el area de los circulos para obtener el area negra
    4-obtener el porcentaje del que representa el area negra del totala del cuadrado (si supercicie del cuadrado = 100 %, superficie del area sombreada = ?
    '''
    Acuad = areaCuad(lado) #area del cuadrado
    AreaCirculos = totalCirculos(lado)
    AreaSombra = Acuad -   AreaCirculos
    
    return AreaSombra

def main():
    print("Ingrese lado:", end='')
    lado = int(input())
    
    AreaNegra = float("{0:.2f}".format(areaNegra(lado)))
    Porcentaje=float("{0:.2f}".format(porcentajeAreaNegra(lado)))
   
    
    
    print ("El area negra es ", 
    AreaNegra ," y es un " , Porcentaje , "% del area total del cuadrado")

#    {0:.2f}".format(porcentajeAreaNegra(12)
    
    
main()
