""" PROBLEMA 2
Juan Curuchet tiene planeando un rally por el Camino de las Altas Cumbres. Puede llevar
dos litros de agua y rodar 7 kilómetros antes de que se le agote. Tiene un mapa con lugares
donde puede repostar agua, y conoce la distancia entre cada uno. El objetivo de Juan es
detenerse la menor cantidad de veces que sea posible. Desarrollar un algoritmo Greedy que
determine en qué lugares detenerse a cargar agua, y mostrar si siempre encuentra el
óptimo o no. """

#Supuesto que la lista tiene solo numeros que son la distancia al anterior.
import time

ciudades_argentina = {
    0: ("Córdoba", 0),
    1: ("Villa Carlos Paz", 3),
    2: ("Mina Clavero", 3),
    3: ("Villa General Belgrano", 1),
    4: ("La Cumbre", 5),
    5: ("Capilla del Monte", 0),
    6: ("Alta Gracia", 5),
    7: ("Cosquín", 2),
    8: ("San Marcos Sierras", 6),
    9: ("Villa Dolores", 1),
    10: ("Río Cuarto", 2),
    11: ("Villa María", 1),
    12: ("San Francisco", 1),
    13: ("Jesús María", 5),
    14: ("Colonia Caroya", 1)
}

if __name__ == "__main__":
    t1 = time.time()
    i = 0
    lista_con_resultados = []
    lista_con_distancias = [ciudades_argentina[i][1] for i in range(len(ciudades_argentina))] #O(n)
    while i < len(ciudades_argentina):
        auxiliar = 0
        ultima_ciudad = None
        while i < len(lista_con_distancias) and auxiliar + lista_con_distancias[i] <= 7:
            auxiliar += lista_con_distancias[i]
            ultima_ciudad = ciudades_argentina[i][0]
            i += 1
        if ultima_ciudad:
            lista_con_resultados.append(ultima_ciudad) #O(n)
    
    print(lista_con_resultados)

    t2 = time.time()
    print(f"Tiempo de ejecución: {t2 - t1} segundos")
    #falta refactor hacer constantes y crear 2 o 3 sets mas largos, complejidad es O(2n)=O(n)
    #hacer que recorra una vez en vez de 2,

    #se usa diccionario con ciudad distancia a la anterior, y listas, el pseudocodigo lo agarramos del msj de wpp.

    #hacer sets de datos de 1000, 5000, 10000
    #si es optimo.
        

        