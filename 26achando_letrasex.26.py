frase = input('Digite uma frase: ')
print(f'A frase possui {frase.lower().count("a")} letras a. ')
print(f"A primeira letra a aparece na casa {frase.lower().find('a')}.")
print(f"A ultima letra a aparece na casa {frase.lower().rfind('a')}")