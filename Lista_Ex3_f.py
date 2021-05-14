#retorne o menor valor.
import numpy as np
matriz = np.array(np.arange(35))
matriz.shape = (5,7)
menor = matriz.min()
print(menor)