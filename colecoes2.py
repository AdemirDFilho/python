print("ola mundo/ colecoes 2")

numeros = ['1','5','3','2']
print(numeros)

numeros.sort()
print(numeros)

numeros.sort(reverse = True)
print(numeros)


fr = ['maçã', 'melancia', 'banana', 'uva', 'pera', 'abacaxi','1','5','3','2']
print(fr)
fr.sort()
print(fr)
fr.sort(reverse=True)
print(fr)

print(f"as frutas são{fr} e os numeros são {numeros}")




print(type(numeros))

alfa = ('a', 'b', 'c')
print(alfa)
print(type(alfa))


print("____________________________________________________")
numeros_copia = numeros.copy()
print(f"numeros {numeros}")
print(f"copia de numeros {numeros_copia}")

numeros.remove('1')
numeros_copia.remove('5')

print(f"a- numeros {numeros}")
print(f"a- copia de numeros {numeros_copia}")

print("____________________________________________________")