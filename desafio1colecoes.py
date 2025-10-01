print("______________________desafio 1__________________")

num = ['1','2','3','4']
#FACEPALM é pra colocar os números SEM ASPAS SEU BURRO!!
print(num)

num.append('6')
print(num)

num.remove('2')
print(num)

num.remove('4')
num.append('40')
print(num)

num.sort(reverse=True)
print(num)
print("______________________desafio 1 - FIM__________________")

print("______________________desafio 1 - SOLUÇÃO__________________")

numero = [1, 2, 3, 4]
print(numero)
numero.append(6)
print(numero)
numero.remove(2)
print(numero)
posicao = numero.index(4)
print(posicao)
numero.insert(posicao, 40)
print(numero)
numero.remove(4)
print(numero) 
numero.sort(reverse=True)
print(numero)


print("______________________desafio 2__________________")
frutas = ('maça', 'banana', 'laranja', 'uva')
print(frutas)
print(type(frutas))

if 'banana' in frutas:
    print("a fruta está na lista")
else:
    print("a fruta NÃO está na lista")

frutas_lista = list(frutas)
frutas_lista.append('abacaxi')
frutas = tuple(frutas_lista)
print(frutas)
print(type(frutas))

print("______________________desafio 2 - FIM__________________")

print("______________________desafio 3 __________________")

aluno = {'nome':'Maria', 'idade':20, 'curso':'Engenharia'}
print(aluno)

aluno['nota']=9.5
print(aluno)

aluno['idade']=21
print(aluno)

#remover curso = FALHA
#aluno.pop['2']
#aluno.clear['curso']
#aluno.clear[2]
#print(aluno)

#SOLUCAO = use parenteses sua ANTA
aluno.pop('curso')
print(aluno)

aluno['cursos']=['adm', 'letras', 'med']
print(aluno)
