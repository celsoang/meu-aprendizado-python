print('Calculadora de m² + tinta ')
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
demao = int(input('Quantas demãos: '))

m2 = altura * largura
litros = m2 * 0.50
tinta = demao * litros

print('{} M²' .format(m2))
print('{} litros de tinta'.format(tinta))

#correção

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede'))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta. '.format(tinta))

