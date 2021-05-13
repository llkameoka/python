'''
Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,'hum', 'dois']. A ideia do exercício é
tirar a média de todos os valores contidos na lista, porém para fazer o cálculo
precisa remover as strings
'''

lista = [6,7,4,7,8,4,2,5,7,'hum', 'dois']
cont = 0
qtd = 0
for x in lista:
    qtd += 1
    #verifica se o elemento e um numero
    if isinstance(x,int) == True:
        cont += x
print(qtd)
print(cont)
print('Média dos números da lista é = {:.2f}'.format(cont/qtd))

