def maximo (a, b):
    if a > b:
        return print("O número {} é o maior".format(a))
    elif a == b:
        return print("os números são iguais")
    else:
        return print("O número {} é o maior".format(b))

print ('teste 1')
valores = (10, 20)
print(f"valores utilizados: a= {valores[0]}, b= {valores[1]}")
maximo(valores[0], valores[1])
print("-" * 50 + "\n")

print ('teste 2')
valores = (100, 20)
print (f"valores utilizados: a= {valores[0]}, b= {valores[1]}")
maximo(valores[0], valores[1])
print("-"*50+"\n")

print ('teste 3')
valores = (50, 50)
print (f"valores utilizados: a= {valores[0]}, b= {valores[1]}")
maximo(valores[0], valores[1])
print("-"*50+"\n")






