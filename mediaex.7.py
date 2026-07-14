print('Média de notas')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

resultado = (nota1 + nota2) / 2

print('A média da nota é: {} '.format(resultado))

#correção

n1 = float(input('primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media =  (n1 + n2 ) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))