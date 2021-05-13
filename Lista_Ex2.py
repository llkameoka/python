'''
Crie um método que receba duas matrizes, some os valores total de cada matriz e
depois multiple o resultado delas e retorne o valor.
'''
def matrizes(mat1, mat2):
    cont1 = 0
    cont2 = 0
    #somando valores da matriz 2
    for linha in mat1:
        for coluna in linha:
            cont1 += coluna
    #somando valores da matriz 2
    for linha in mat2:
        for coluna in linha:
            cont2 += coluna
    #multiplicando resultado da soma das matrizes
    print(cont1 * cont2)


lista1 = [[1, 2], [3, 4], [5, 6]]
lista2 = [[7, 8], [9, 10], [11, 12]]
matrizes(lista1, lista2)
