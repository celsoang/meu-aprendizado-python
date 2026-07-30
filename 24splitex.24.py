def main():
    while True:
        print('-----SEJA BEM VINDO-----')
        print('1. para testar a primeira maneira. ')
        print('2. para testar a segunda maneira. ')
        print('3. CORREÇÃO. ')
        print('0. para finalizar operação. ')

        opcao = input('Escolha uma opcao: ')

        if opcao == '1':
            primeiro_jeito()
        elif opcao == '2':
            outro_jeito()
        elif opcao == '3':
            correcao()
        elif opcao == '0':
            print('Encerrando operação. ')
            break
        else:
            print('Comando inválido tente novamente. ')

def primeiro_jeito():
    cidade = input('O nome da cidade começa com santo? Digite a cidade: ').strip()
    cidade0 = cidade.split()
    print('santos' in cidade0[0] or 'SANTOS' in cidade0[0] or 'Santos' in cidade0[0])
    if cidade0[0].startswith(('santos', 'SANTOS', 'Santos')):
        print('Começa com santos.')
    else:
        print('Não começa com santos. ')

def outro_jeito():
    while True:
        print('Outra maneira de fazer: ')
        cidade1 = input('O nome da cidade começa com Santos? ').strip()

        if not cidade1:
            print('Erro: Você não digitou nada tente novamente. ')
            continue

        if any(caractere.isdigit() for caractere in cidade1):
            print('Erro: Você digitou números, tente novamente. ')
            continue

        cidade2 = cidade1.split()

        print('santos' in cidade2[0].lower())

        if 'santos' == cidade2[0].lower():
            print('Começa com santos. ')
        else:
            print('Não começa com santos. ')
        break

def correcao():
    cid = str(input('Em que cidade você nasceu? ')).strip()
    print(cid[:5].upper() == 'SANTO')


main()

























