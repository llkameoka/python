#retorne o maior valor
import numpy as np
matriz = np.array(np.arange(35))
matriz.shape = (5,7)
maior = 0
for i in matriz:
  for j in i:
  	#comparacao para obter o maior numero
    if j >= maior:
      maior = j
#usando numpy para obter o maior numero
maior1 = matriz.max()
print('Maior numero da matriz usando for: {}'.format(maior))
print('Maior numero da matriz usando numpy: {}'.format(maior1))