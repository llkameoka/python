def triangulo(r1, r2, r3):
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        if r1 == r2 == r3:
            print('As retas podem formar um triangulo equilátero')
        elif r1 != r2 != r3 != r1:        
            print('As retas podem formar um triangulo escaleno')
        else:
            print('As retas podem formar um triangulo isósceles')
    else:
        print('As retas não podem formar um triangulo')

a = int(input('Digite o valor da reta 1: '))
b = int(input('Digite o valor da reta 2: '))
c = int(input('Digite o valor da reta 3: '))
triangulo(a, b, c)
