print('________DESAFIO 1 - CONTAR DE 1 A 10__________')

n = 1
while n <=10:
    print(n)
    n +=1

print('________DESAFIO 2 - TABUADA DE 1 A 10__________')

#COMENTADO A LINHA DE INPUT PARA NÃO ATRAPALHAR OS EXERCICIOS
""" n1 = int(input('DIGITE UM NUMERO ... ')) """
n1 = 3
print(f'TABUADA DE MULTIPLICAÇÃO DE: {n1}')
for t in range(1, 11):
    mult = n1 * t
    print(f'{n1} X {t} = {mult}')

#APENAS UMA IDÉIA [NÃO CONCLUIDA] PARA FAZER MULTIPLAS TABUADAS
""" print(f'TODAS AS TABUADAS DE {n1}')
for t in range(1, 11):
    soma = n1 + t
    print(f'{n1} + {t} = {soma}')
    subt = n1 - t
    print(f'{n1} - {t} = {subt}')
    mult = n1 * t
    print(f'{n1} X {t} = {mult}')
    divi = n1 / t
    print(f'{n1} ÷ {t} = {divi}')   """  

print('________DESAFIO 3 - CONTAR VOGAIS__________')

""" palavra = input('Digite uma palavra/frase (não use acentos) ... ') """
palavra = 'AROEIRAdias'
vogais = ['a','e','i','o','u','A','E','I','O','U']
conta_vogal = 0
for p in palavra:
    if p in vogais:
        print(p)
        conta_vogal +=1
    else:
        continue
print(f'a palavra/frase {palavra} tem {conta_vogal} vogais')


print('________DESAFIO 3 - CONTAR VOGAIS - solucao__________')

pal = 'AROEIRAdias'
vogais = 'AEIOUaeiou'
cont = 0
for p in pal:
    if p in vogais:
        print(p)
        cont +=1
print(f'a palavra {pal} tem {cont} vogais')



print('________DESAFIO 4 - tabuada de 1 a 100__________')

num = 2
for tt in range(1,101):
    tt_mult = num * tt
    print(f'{num} X {tt} = {tt_mult}')

print('________DESAFIO 4 - tabuada de 1 a 100 [SOLUÇÃO]__________')

for n in range(1,101):
    for m in range(1,11):
        res = n*m 
        print(f"{m} X {n} = {res}")


