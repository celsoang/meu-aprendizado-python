senha_salva = ''

def main():
    while True:

        print('-----BEM VINDO AO MENU PRINCIPAL-----')
        print('1. Para criar sua senha.')
        print('2. Para editar sua senha.')
        print('3 Mostrar senha: ')
        print('0. Para encerrar opereção.')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            gerar_senha()
        elif opcao == '2':
            editar_senha()
        elif opcao == '0':
            print('Encerrando operação!')
            break
        else:
            print('Erro! Opção inválida! escolha entre 0 e 2 ')






def gerar_senha():
    global senha_salva

    if senha_salva != '':
        print('Erro! Você já possui uma senha use a opçãp 2 para editar: ')
        return

    while True:
        senha = (input('Digite sua senha: (apenas numeros) '))

        if not senha:
            print('Erro! Você não digitou nada, tente novamente. ')
            continue

        if not senha.isdigit():
            print('Erro! Você digitou letras, tente novamente. ')
            continue
        break

    senha_salva = senha
    print('Senha criada com sucesso!')






def editar_senha():
    global senha_salva

    if senha_salva == '':
        print('Nenhuma senha cadastrada ainda, use a opção 1 primeiro. ')
        return

    senha_atual = input('Digite a sua senha atual para permitir a alteração:')

    if senha_atual != senha_salva:
        print('Erro! Senha incorreta operação cancelada por segurança! ')
        return

    while True:
        nova_senha = input('Digite sua nova senha: ')

        if not nova_senha:
            print('Erro! Você não dogitou nada, tente novamente. ')
            continue

        if not nova_senha.isdigit():
            print('Erro! Você digitou letras tente novamente. ')
            continue

        if nova_senha == senha_salva:
            print('Erro! A nova senha não pode ser igual a senha atual. ')
            continue

        break

    senha_salva = nova_senha
    print('Senha alterada com sucesso! ')

main()




















