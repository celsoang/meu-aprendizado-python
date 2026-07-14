print('Cálculadora de conversão de temperatura')
celsius = float(input('Temperatura C°: '))
kelvin = celsius + 273.15
fahrenheit = (celsius * 1.8) + 32

print('{}°K '.format(kelvin))
print('{}°F '.format(fahrenheit))

#correção

c = float(input('Informe a temperatura em C° '))
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))