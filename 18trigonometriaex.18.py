print('Exercício de trigonometria (Descobrindo seno cosseno e tangente)')
import math
angulo = float(input('Digite o angulo : '))

seno = math.radians(angulo)
cosseno = math.radians(angulo)
tangente = math.radians(angulo)

seno_r = math.sin(seno)
cosseno_r = math.cos(cosseno)
tangente_r= math.tan(tangente)

print('Seno de {}: {:.2f}\nCosseno de {}: {:.2f}\nTangente de {}: {:.2f}'.format(angulo, seno_r, angulo, cosseno_r, angulo, tangente_r))

#correção
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

#Outra forma de resolver
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

