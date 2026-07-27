print('Dobro triplo e raiz quadrada ')
numero = float(input('Digite um número: '))
print('O dobro desse número é: {} '.format(numero * 2))
print('O triplo desse número é: {} '.format(numero * 3))
print('A raiz quadrada desse número é: {} '.format(numero **0.5))

#correção

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)
print('O dobro de {} vale {}.'.format(numero, dobro))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(numero, triplo, numero, raiz_quadrada))

#correção

numero = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(numero, (numero*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(numero, (numero*3), numero, (numero**(1/2))))

#correção
numero = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(numero, (numero*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(numero, (numero*3), numero, pow(numero, (1/2))))
