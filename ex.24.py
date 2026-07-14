cidade = input('O nome da cidade começa com santo? Digite a cidade: ')
cidade0 = cidade.split()
print('santo' in cidade0[0])
if cidade0[0] == 'santo':
    print('tem')
else:
    print('Nao tem')




