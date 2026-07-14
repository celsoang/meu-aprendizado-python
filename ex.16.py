print('Arredondando números para mais ou para menos')

import math
num = float(input('Digite um número: '))

num_arredondado = math.floor(num) #Aqui posso usar floor ou seil , isso arredonda o numero pra mais e pra menos

print('O numero é {:.3f}'.format((num_arredondado)))

#correção
#A função "trunc" apenas tira os números decimais
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#Outra maneira de resolver
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

