def calcular_fuerza(q, C=1):
    n = len(q)
    F = [0.0] * n

    def divide_conquista(inicio, fin):
        if fin - inicio <= 1:
            return

        medio = (inicio + fin) // 2

        # Resolver izquierda y derecha por separado
        divide_conquista(inicio, medio)
        divide_conquista(medio, fin)

        # Calcular las interacciones cruzadas entre mitades
        for i in range(inicio, medio):
            for j in range(medio, fin):
                distancia = j - i
                fuerza = C * q[i] * q[j] / (distancia * distancia)
                F[j] += fuerza    # i < j -> fuerza positiva
                F[i] -= fuerza    # j > i -> fuerza negativa

    divide_conquista(0, n)
    return F
if __name__ == '__main__':
    with open("mil_cargas.txt", "r") as f:
        mil_cargas = list(map(int, f.readlines()))

    with open("diezmil_cargas.txt", "r") as f:
        diezmil_cargas = list(map(int, f.readlines()))

    print("Resultado para mil cargas:", calcular_fuerza(mil_cargas))
    print("Resultado para diezmil cargas:", calcular_fuerza(diezmil_cargas))
