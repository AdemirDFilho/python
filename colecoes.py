print("olá mundo")
print("__________LISTAS__________")
# frutas = fr
fr = ['maçã', 'melancia', 'banana', 'uva', 'pera', 'abacaxi']
print(fr)
print("____________________")
#tipo
print(type(fr))
#retorno itens do intervalo
print(fr[0:2])
#conta os itens
print(len(fr))
#retorna o item
print(fr[2])
#conta itens
print(fr.count('uva'))
#informa indice item
print(fr.index('banana'))
print("____________________")
if 'uva' in fr:
    print("uva está em frutas")
else:
    print("uva não está em frutas")
print("__________INPUT__________")
fr_pedido = input("digite uma fruta >bobo< ")
fr.insert(7, fr_pedido)
print(fr)

print(fr.index('abacaxi'))
print(fr.index('bobo'))

print("________REMOVE POP____________")
fr.remove('bobo')
print(fr)

fruta_removida = fr.pop(0)
print(f"a fruta {fruta_removida} foi removida.")
print(fr)

#12MIN