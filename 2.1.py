'''
Desarrollar un función ​ convertir
que recibe por parámetro un valor
numérico entero, el cual representa una cantidad expresada en segundos. La
función deberá convertir el valor en segundos a (​ días, horas minutos,
segundos ​ ); e imprimirlo como muestra el ejemplo.
Utilizar la función en un programa que solicitará al usuario el ingreso de un
números enteros y natural, que representa un valor en segundo; luego invocar
a ​ convertir​ para obtener el resultado como muestra el ejemplo.
Ejemplo:
Ingrese tiempo en segundos: 93714
1 dia(s), 2 hora(s), 1 minuto(s), 54 segundo(s).

1 dìa 24 horas   86400
1hora 60 minutos  3600
1 dia
1 minuto 60 segundo6


'''

def  convertir(segundos):
    
    res = []
    dias = segundos / 86400
    restodias = segundos % 86400
    horas = restodias / 3600
    restohoras = restodias % 3600
    minutos =  restohoras / 60
    segundosfin = restohoras % 60
    res.append(int(dias))
    res.append(int(horas))
    res.append(int(minutos))
    res.append(int(segundosfin))    
    return res
    
      
        
def main():
    segundos=int(input("ingrese tiempo en segundos:"))
    resultado = convertir(segundos)
    print(resultado[0] , "dia(s)", resultado[1],"hora(s)" , resultado[2],"minuto(s)",resultado[3],"segundos")



main()
