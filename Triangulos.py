def triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        print('As retas {}, {} e {} formam um triangulo'.format(a, b, c))
        if a == b and a == c and b == c:
            print('As retas {}, {} e {} formam um triangulo equilatero'.format(a, b, c))
        elif a == b or a == c or b == c:
            print('As retas {}, {} e {} formam um triângulo isósceles'.format(a, b, c))
        else:
            print('As retas {}, {} e {} formam um triângulo escaleno'.format(a, b, c))
    else:
        print('As retas não forma um triangulo')


a = int(input('Digite o valor da reta 1: '))
b = int(input('Digite o valor da reta 2: '))
c = int(input('Digite o valor da reta 3: '))
triangulo(a, b, c)
