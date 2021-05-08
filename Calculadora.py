def calculadora(n1,n2,operador):
	if operador == 1:
		soma = n1 + n2
		print('A soma de {} + {} é: {}'.format(n1,n2,soma))
	elif operador == 2:
		subtracao = n1 - n2
		print('A subtracao de {} - {} é: {}'.format(n1,n2,subtracao))
	elif operador == 3:
		multiplicacao = n1 * n2
		print('A multiplicacao de {} * {} é: {}'.format(n1,n2,multiplicacao))
	elif operador == 4:
		if n2 != 0:
			divisao = n1/n2
			print('A divisao de {} / {} é: {}'.format(n1,n2,divisao))
		else:
			print('Nao existe divisao por zero!')
	elif operador == 5:
		potenciacao = n1 ** n2
		print('A potenciacao de {} ** {} é: {}'.format(n1,n2,potenciacao))
print('Calculadora')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = int(input('''
Escolha uma das opções abaixo:
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Potencia
'''))
calculadora(n1,n2,opcao)