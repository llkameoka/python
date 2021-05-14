#somar todas as linhas.
import numpy as np
matriz = np.array(np.arange(35))
matriz.shape = (5,7)
#axis = 1 se refere a linha
matriz.sum(axis=1)	