print('Manipulando caracteres')
numero = input('Digite um nome entre 0 e 9999: ')

print(f'Unidade: {numero[3]}')
print(f'Dezena : {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar : {numero[0]}')


#Outra maneira de resolver usando zfill()
print('Outra maneira de resolver')
numerox = input('Digite um número: ')
numero1 = numerox.zfill(4)

print(f'unidade:{numero1[3]}')
print(f'dezena: {numero1[2]}')
print(f'centena {numero1[1]}')
print(f'milhar: {numero1[0]}')

#Invertendo palavras
palavra = input('Digite uma palavra: ')
palavra1 = palavra[::-1]
print(palavra1)

#Correção de atividade
num = int(input('Informe um número: '))
u = num// 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centana: {c}')
print(f'Dezena: {m}')







