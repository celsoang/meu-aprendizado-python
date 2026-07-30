def main():
    while True:

        print('\n-----MENU-----')
        print('1. Para verificar se o nome possui Silva. ')
        print('2. Para ver a correção. ')
        print('0. Para encerrar sessão. ')

        opcao = input('Digite um número. ')

        if opcao == '1':
            silva()
        elif opcao == '2':
            correcao()
        elif opcao == '0':
            print('Encerrando operação... ')
            break
        else:
            print('Comando inválido! Tente novamente.')


def silva():
    print('Verificação se nome possui silva. ')
    while True:
        nome = input('Digite seu nome: ').strip()
        if not nome:
            print('Você não digitou nada! Tente novamente. ')
            continue
        if any(letra.isdigit() for letra in nome):
            print('[ERRO] Numeros são inaválidos! Tente novamente. ')
            continue
        print('silva' in nome.lower())
        if 'silva' in nome.lower():
            print('Seu nome possui silva!')
        else:
            print('Seu nome não possui silva!')
        break

    input('\nPressione Enter para voltar ao menu...')


def correcao():
    nomee = str(input('Qual o seu nome completo?')).strip()
    print(f'Seu nome possui silva? {"silva" in nomee.lower()}')

    input('\nPressione Enter para voltar ao menu...')


main()


