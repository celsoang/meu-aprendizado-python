while True:
    frase = input('Digite uma frase: ').lower().strip()
    if any(numeros.isdigit() for numeros in frase):
        print('Números são inválidos!')
        continue
    break

nova = frase.replace('á', 'a').replace('à', 'a').replace('â', 'a').replace('ã', 'a')

letra_a = nova.count('a')

if letra_a == 0:
    print('A frase não possuia letra "a".  ')
else:
    print(f'A frase possui {nova.lower().count("a")} letras a. ')
    print(f'A primeira letra a aparece na casa {nova.lower().find("a")}.')
    print(f'A última letra a aparece na casa {nova.lower().rfind("a")}')

#correção
frases = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra A aparece {frases.count("a")} vezes na frase')
print(f'A primeira letra A apareceu na posição {frases.find("a")}')
print(f'A última letra a apareceu na posição {frases.rfind("a")}')