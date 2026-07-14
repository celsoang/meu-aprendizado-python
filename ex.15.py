print('Calculando valor de aluguel de carro')
#O valor do dia é  R$60 e o valor do km é R$0.15

dias = int(input('Dias alugados: '))
km = float(input('Km rodado: '))

valor_dia = 60 * dias
valor_km = 0.15 * km

print('O total a pagar é de R${:.2f}'.format(valor_dia + valor_km))

#correção

dias = int(input('Quanto dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))


