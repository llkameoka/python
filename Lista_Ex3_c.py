#somar todas as colunas
import numpy as np
matriz = np.array(np.arange(35))
matriz.shape = (5,7)
#axis = 0 se refere a coluna
matriz.sum(axis=0)