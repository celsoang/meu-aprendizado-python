print('Número anteccessor número sucessor')
numero = int(input('digite um numero: '))
print('Seu sucessor é {}'.format(numero + 1))
print('Seu antecessor é {}'.format(numero - 1))

#correção

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisado o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,a,s ))

#correção

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
