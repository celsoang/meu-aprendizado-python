print('Cálculadora de aumento de salário')
print('15% de aumento')

salario = float(input('Salário: '))
aumento = (salario * 15) / 100
novo_salario = salario + aumento

print('Novo salário: R$ {:.2f}'.format(novo_salario))
print('Você teve R$ {:.2f} de aumento'.format(aumento))

#correção

salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))


