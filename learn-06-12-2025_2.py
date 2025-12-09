#https://www.learnpython.org/pt/Basic_Operators
#DESAFIO CAPITULO 
""" O objetivo deste exercício é criar duas listas chamadas x_list e y_list, 
que contêm 10 instâncias das variáveis x e y, respectivamente. 
Você também deve criar uma lista chamada big_list, que contém as variáveis x e y, 10 vezes cada, 
concatenando as duas listas que você criou. """

#-------------------COD DESAFIO ----------------------

""" x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!") """




#-------------MINHA TENTATIVA *ERRADA*----------------------------
""" x = object()
y = object()

# TODO: change this code
x_list = ([x]*10)
y_list = ([y]*10)
big_list = [x_list+y_list]

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

print("...............")
print(x_list)
print(y_list)
print(big_list) """

#--------------------SOLUÇÃO-----------------------------
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


print(x_list)
print(y_list)
print(big_list)
