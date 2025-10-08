
# \n QUEBRA LINHA

for n in range(1, 2):
    print(f'loop - execução nº {n}')
    print('loop loop loop\n')
    
print('_____________________________')
soma = 0
for n in range(0, 10):
    soma += 1
print(f'a soma total é {soma}')

print('_____________________________')
frutas = ('banana', 'maçã', 'pera', 'uva')
for f in frutas:
    print(f)

print('_____________________________')
nome = "ADEMIR"
for L in nome:
    print(L)

""" ALT+SHIFT+A ATALHO PARA COMENTAR/DESCOMENTAR BLOCOS DE CODIGO! """
""" print('_____________________________')
contador = 0
while contador <= 10:
    print(f'o contador está em {contador}')
    contador +=1 """

print('___CTRL + K  +CTRL+C / CTRL+U _______')
while True:
    numero = int(input('digite um numero ... '))
    if numero % 2 == 0:
        print(f'o número digitado {numero} é PAR.')
        break
    else:
        print(f'o numero digitado {numero} é IMPAR!')
print('fim do loop - PAR.')

print('_____________________________')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for n in numeros:
    if n %2 != 0:
        continue
    else:
        print(f'o numero {n} é PAR.')

print('____________SOMA IMPARES_________________')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
soma_impares = 0
for n in numeros:
    if n %2 != 0:
        soma_impares +=n
        continue
    else:
        print(f'o numero {n} é PAR.\n a soma de impares é {soma_impares}.')

print('______________DICIONARIOS_______________')
dicionario = {'nome': 'ademir', 'idade':30, 'sexo':'masculino'}

""" print(dicionario) """

for c, v in dicionario.items():
    print(f'{c}: {v}')

for v in dicionario.values():
    print(f'valor {v}')

for c in dicionario.keys():
    print(f'chave {c}')


