def main():
    while True:
        print('-----BEM NINDO AO MENU-----')
        print('Escolha uma opção:')
        print('1. Para primeira maneira de resolver. ')
        print('2. Para segunda maneira de resolver usando zfill(). ')
        print('3. Para inverter palavras. ')
        print('4. Para correção de atividade. ')
        print('0. Para encerrar sessão. ')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            manipulando_caracteres()
        elif opcao == '2':
            outra_maneira()
        elif opcao == '3':
            invertendo_palavras()
        elif opcao == '4':
            correcao_atividade()
        elif opcao == '0':
            print('Finalizando sessão... ')
            print('Bye. ')
            break
        else:
            print('[ERRO] Tente novamente. ')


def manipulando_caracteres():
    print('Manipulando caracteres')
    numero = input('Digite um nome entre 0 e 9999: ')

    print(f'Unidade: {numero[3]}')
    print(f'Dezena : {numero[2]}')
    print(f'Centena: {numero[1]}')
    print(f'Milhar : {numero[0]}')

def outra_maneira():
#Outra maneira de resolver usando zfill()
    print('Outra maneira de resolver')
    numerox = input('Digite um número de até 4 digitos: ')
    numero1 = numerox.zfill(4)

    print(f'unidade:{numero1[3]}')
    print(f'dezena: {numero1[2]}')
    print(f'centena {numero1[1]}')
    print(f'milhar: {numero1[0]}')

def invertendo_palavras():
#Invertendo palavras
    palavra = input('Digite uma palavra: ')
    palavra1 = palavra[::-1]
    print(palavra1)

def correcao_atividade():
#Correção de atividade
    num = int(input('Informe um número de até 4 digitos: '))
    u = num// 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'Centana: {c}')
    print(f'Dezena: {m}')

main()





