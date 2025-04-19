def backtracking(recorrido, n, indice, resultado, suma):
    if suma == n:
        if len(resultado) == 1 and len(resultado[0]) > len(recorrido):
            resultado.pop()
            resultado.append(recorrido[:])
        if len(resultado) == 0:
            resultado.append(recorrido[:])
        return
    #del or para adelatente es una condicion de poda que añadi
    if suma > n or len(resultado) != 0 and len(recorrido) > len(resultado[0]):
        return
    
    while len(recorrido) >= 1 and indice <= len(recorrido) - 1:
        longitud = len(recorrido) - 1
        if len(recorrido) == 1:
            suma = recorrido[indice] + recorrido[longitud]
            recorrido.append(suma)
            backtracking(recorrido,n,indice,resultado,suma)
            return resultado
        else:
            suma = recorrido[indice] + recorrido[longitud]
            recorrido.append(suma)
            if indice > 0:
                backtracking(recorrido,n,0,resultado,suma)
            else: 
                backtracking(recorrido,n,indice,resultado,suma)                   
            recorrido.pop()
            indice = indice + 1

def main():
    recorrido = [1]
    n = 7
    resultado = []
    suma = 0
    backtracking(recorrido, n, 0, resultado, suma)
    print(resultado) 

main()