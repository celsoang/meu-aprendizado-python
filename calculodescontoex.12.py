print('Calculadora de desconto')
produto = float(input('Camisa R$ '))

desconto = (produto * 5) / 100
preco_final = produto - desconto

print('Desconto de 5% !')
print('O preço final fica: R$ {:.2f} '.format(preco_final))
print('Você economizou ! R$ {:.2f}  '.format(desconto))

#correção

preco = float(input('Qqual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))






