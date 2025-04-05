import random
import time

MAXIMA_DISTANCIA = 7

def generar_datos(n, semilla):
    random.seed(semilla)
    return [random.randint(0, MAXIMA_DISTANCIA) for _ in range(n)]

def calcular_mejor_distancia(distancias, resultado):
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
   
    archivo_resultado.write("\n".join(map(str, lista_con_resultados)))
    t2 = time.time()
    print("Tiempo de ejecución:", t2 - t1)

if __name__ == "__main__":
    with open("mil_distancias.txt", "w") as f:
        f.write("\n".join(map(str, generar_datos(1000, 1))))
    
    with open("diezmil_distancias.txt", "w") as f:
        f.write("\n".join(map(str, generar_datos(10000, 2))))
    
    with open("cienmil_distancias.txt", "w") as f:
        f.write("\n".join(map(str, generar_datos(100000, 3))))
    
    with open("quinientosmil_distancias.txt", "w") as f:
        f.write("\n".join(map(str, generar_datos(500000, 4))))
    
    with open("unmillon_distancias.txt", "w") as f:
        f.write("\n".join(map(str, generar_datos(1000000, 5))))

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

    with open("resultado_mil.txt", "w") as archivo_resultado:
        calcular_mejor_distancia(mil_distancias, archivo_resultado)

    with open("resultado_diezmil.txt", "w") as archivo_resultado:
        calcular_mejor_distancia(diezmil_distancias, archivo_resultado)

    with open("resultado_cienmil.txt", "w") as archivo_resultado:
        calcular_mejor_distancia(cienmil_distancias, archivo_resultado)
    
    with open("resultado_quinientosmil.txt", "w") as archivo_resultado:
        calcular_mejor_distancia(quinientosmil_distancias, archivo_resultado)
    
    with open("resultado_unmillon.txt", "w") as archivo_resultado:
        calcular_mejor_distancia(unmillon_distancias, archivo_resultado)
        