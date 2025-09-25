print("olá mundo")
print("listas e letras")

#letras = let
let = ['A','B','C','D','E']
print(let)
print(type(let))
print(len(let))

total = len(let)
print(f"a lista tem {total} letras")

print(let[0])
print(let[4])

let.append('Y')
print(let)
total = len(let)
print(f"a lista tem {total} letras")

let.remove('A')
print(let)
total = len(let)
print(f"a lista tem {total} letras")

print(let[0])
print(let[4])

#let.isert = input("digite uma letra ")
#print(let)

#INSERE UMA LETRA
pedido = input("digite uma letra ")
let.append(pedido)
print(let)
total = len(let)
print(f"a lista tem {total} letras")

#REMOVE UMA LETRA
remove = input("escolha uma letra para remover ")
let.remove(remove)
print(let)
total = len(let)
print(f"a lista tem {total} letras")

print("____________fim do codigo_____________")

