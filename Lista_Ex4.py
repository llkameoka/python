import numpy as np
matriz = np.array(np.arange(35))
matriz.shape = (5,7)
matriz2 = np.array(np.arange(25))
matriz2.shape= (5,5)
soma = matriz.sum() + matriz2.sum()
print(soma)