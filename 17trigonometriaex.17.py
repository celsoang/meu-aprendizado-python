print('Exercicio de trigonometria(Descobrindo hipotenusa')
import math

cateto_oposto = float(input('Digite o comprimento do cateto oposto : '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente : '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente )

print('Hipotenusa = {:.2f}'.format(hipotenusa))

#correção
#forma matemática de resolver
cateto_oposto1 = float(input('Comprimento do cateto oposto: '))
cateto_adjacente1 =float(input('Comprimento do cateto adjacente: '))
hipotenusa1 = (cateto_oposto1 ** 2 + cateto_adjacente1 ** 2) ** (1/2)
print('A hipotenusa vai medir{:.2f}'.format(hipotenusa1))

#forma de resolver usando biblioteca math
import math
cateto_oposto2 = float(input('Comprimento do cateto oposto: '))
cateto_adjacente2 = float(input('Comprimento do cateto adjacente: '))
hipotenusa2 = math.hypot(cateto_oposto2, cateto_adjacente2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa2))

#outra maneira de resolver importando somente a função hypot
from math import hypot
cateto_oposto2 = float(input('Comprimento do cateto oposto: '))
cateto_adjacente2 = float(input('Comprimento do cateto adjacente: '))
hipotenusa2 = hypot(cateto_oposto2, cateto_adjacente2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa2))


