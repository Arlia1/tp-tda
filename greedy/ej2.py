import random
import time

MAXIMA_DISTANCIA = 7

def calcular_mejor_distancia(distancias):
    t1 = time.time()
    i = 0
    largo = len(distancias)
    lista_con_resultados = list()
    while(i < largo):
        auxiliar = 0
        while(i < largo and auxiliar + distancias[i] <= MAXIMA_DISTANCIA):
            auxiliar += distancias[i]
            i += 1
        lista_con_resultados.append(i-1)
    
    lista_con_resultados.append(i)
   
    t2 = time.time()
    print(lista_con_resultados)
    print("Tiempo de ejecución:", t2 - t1)

    return lista_con_resultados

if __name__ == "__main__":

    with open("mil_distancias.txt", "r") as f:
        mil_distancias = list(map(int, f.readlines()))

    with open("diezmil_distancias.txt", "r") as f:
        diezmil_distancias = list(map(int, f.readlines()))
    
    with open("cienmil_distancias.txt", "r") as f:
        cienmil_distancias = list(map(int, f.readlines()))
    
    with open("quinientosmil_distancias.txt", "r") as f:
        quinientosmil_distancias = list(map(int, f.readlines()))
    
    with open("unmillon_distancias.txt", "r") as f:
        unmillon_distancias = list(map(int, f.readlines()))

    print("Resultado para mil distancias:", calcular_mejor_distancia(mil_distancias))
    print("Resultado para diezmil distancias:", calcular_mejor_distancia(diezmil_distancias))
    print("Resultado para cienmil distancias:", calcular_mejor_distancia(cienmil_distancias))
    print("Resultado para quinientosmil distancias:", calcular_mejor_distancia(quinientosmil_distancias))
    print("Resultado para un millón de distancias:", calcular_mejor_distancia(unmillon_distancias))
