#invertir BNUM
"""
FUNCION que recibe un numero entero y retorna el numero entero
en forma invertida
NO usar string
y ademas el numero no se tsabe la cant
idad de cifras





2-

es primo recibe un numero entero por parametro , retorna true es primo flase si
no lo es  (1,2,3,5,7,11,13,17,19)
hacer con while y optimizar cantidad de vueltas probar 1233333332 no tiene que tardar

esPrimo

Recibe un numero entero por paramtro,
retorna True si es primo, False si no lo es
1,2,3,5,7,11,13,17,19

1233333333332

"""


def invertirnumero(num):
  
    revertir = 0
    while num > 0:
            resto = num % 10 #contien el ultimo digito del numero
            #print("resto", resto)
            revertir = (revertir * 10) +resto #genrerando numero invertido agregar ultimo digito se mutliplica la variable revertido por 10
            #para que la columna de las unidades se convierta en la de la decenas, la de las deceneas en la de las centenas... a su vez en la columna de  unidad se le suam el ultimo numeor del resto
            #print("revertir" , revertir)
            num = num // 10  # floor division sin decimale dvide por 10 para sacar el ultimo digito y actualizar el numero para el proximo ciclo como . corre un lugar hacia la derecha "la coma"
            #print("numero", num)
    return revertir

        
    return  num #retorna cantidad digitos numero



def main():
    print(invertirnumero(25698659))
main()