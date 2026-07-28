cidade = input('O nome da cidade começa com santo? Digite a cidade: ')
cidade0 = cidade.split()
print('santos' in cidade0[0] or 'SANTOS' in cidade0[0] or 'Santos' in cidade0[0])
if cidade0[0].startswith(('santos', 'SANTOS', 'Santos')):
    print('Começa com santos.')
else:
    print('Nao começa com santos')



while True:
    print('Outra maneira de fazer: ')
    cidade1 = input('O nome da cidade começa com Santos? ')

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
        print('Não começa con santos. ')
    break





