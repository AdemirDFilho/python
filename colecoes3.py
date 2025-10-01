print("tuple")

cores = ('azul','vermelho','amarelo', '1', '5')

print(type(cores))
print(f"a tuple de cores é {cores}")

#cores.append(branco)
#erro> AttributeError: 'tuple' object has no attribute 'append' (O objeto 'tuple' não possui o atributo 'append')

lista = list(cores)
print(lista)
lista.append('vermelho')
print(lista)

cores = tuple(lista)
print(cores)
print(type(cores))


print("________________________________________")
print("dicionario DICT")

cachorro = {'raça': 'pitbull', 'nome':'pipoca', 'idade':5}
print(cachorro)
print(type(cachorro))

print(cachorro['idade'])
print(f"o nome do cão é {cachorro['nome']}")

print(cachorro.get('peso', 'peso não encontrado'))

cachorro['peso'] = 40
print(cachorro)
print(cachorro.get('peso', 'peso não encontrado'))
