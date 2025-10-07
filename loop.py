#for n in range(0, 100)


frutas = ['azul', 'amarelo', 'verde', 'branco']
for abc in frutas:
    print(f"fruta {abc}")

for n in range(0, 3):
    print(f"isso é um loop, execução nº: {n}")

#n = 10
#r = n%2 - RESTO DA DIVISÃO DE N POR 2
#print(r)

var = [1, 2, 3, 4 ,5 , 6, 7, 8, 9, 0]
#print(var)

print("______________________PARES______________________")
par = 0
for num in var:
    if num%2 == 0:
     print(f"{num} é par.")
     par +=1
     print(f"total de numeros pares é {par}")

print("______________________IMPARES______________________")
impar = 0
for num in var:
    if num%2 != 0:
     print(f"{num} é impar!")
     impar +=1
     print(f"total de numeros impares é {impar}")

print("fim do codigo")

