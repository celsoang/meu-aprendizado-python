print('Embaralhando nomes')
import random

a = str(input('Nome: '))
b = str(input('Nome: '))
c = str(input('Nome: '))
d = str(input('Nome: '))

lista = [a, b, c, d]

random.shuffle(lista)

print('\n'.join(lista))

#Correção
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista1 = [n1, n2, n3, n4]
random.shuffle(lista1)
print('A ordem de apresentação será ')
print(lista)

#Outra maneira de resolver
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista2 = [n1, n2, n3, n4]
shuffle(lista2)
print('A ordem de apresentação será ')
print(lista)

