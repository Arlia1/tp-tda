import time

def backtracking(recorrido, n, indice, resultado, suma):
    if suma == n:
        if len(resultado) == 1 and len(resultado[0]) > len(recorrido):
            resultado.pop()
            resultado.append(recorrido[:])
        if len(resultado) == 0:
            resultado.append(recorrido[:])
        return
    if suma > n or len(resultado) != 0 and len(recorrido) > len(resultado[0]):
        return
    indice = len(recorrido) - 1
    while len(recorrido) >= 1 and indice <= len(recorrido) - 1 and indice >= 0:
        longitud = len(recorrido) - 1
        if len(recorrido) == 1:
            suma = recorrido[indice] + recorrido[longitud]
            recorrido.append(suma)
            backtracking(recorrido,n,len(recorrido) - 1,resultado,suma)
            return resultado
        else:
            suma = recorrido[indice] + recorrido[longitud]
            recorrido.append(suma)
            if indice > 0:
                backtracking(recorrido,n,len(recorrido) - 1,resultado,suma)
            else: 
                backtracking(recorrido,n,indice,resultado,suma)                   
            recorrido.pop()
            indice = indice - 1 

if __name__ == "__main__":   
    with open("set_de_datos.txt", "r") as f:
        for linea in f:
            n = int(linea.strip())
            resultado = []
            t1 = time.time()
            backtracking([1], n, 0, resultado, 0)
            t2 = time.time()
            print(t2 - t1)
            print(resultado[0][1:])