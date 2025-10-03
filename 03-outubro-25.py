o = "olá"
m = "mundo"
print(type(o))
print(type(m))
print(o+" "+m)

#lista
semana = ['segunda', 'terça', 'quarta']
print(type(semana))
tp = type(semana)
print(f"semana é da {tp}, os dias da semana são {semana}")

if 'segunda' in semana:
    print("segunda está em semana")
else:
    print(f"verifique novamente {semana}")

#tuple
cores = ['azul', 'verde', 'branco']
Tcor = type(cores)
print(f"cores é da classe {Tcor}, as cores são: {cores}")

if 'azul' in cores and 'terça' in semana:
    print("azul e terça")
else:
    print("sem resultado-0")

if 'verde' in cores or 'quarta' in semana:
        print("verde e quarta")
else:
    print("sem resultado-1")


if 'branco' in cores and ('segunda' in semana or 'sexta' in semana):
         print("branco + segunda/sexta")
else:
    print("sem resultado-2")


num1 = int(input("digite um número "))
print(f"o numero digitado foi {num1}")

num2 = int(input("digite um numero "))
print(f"o segundo numero digitado foi {num2}")

print(type(num1))
print(type(num2))
soma = num1 + num2

print(f"a soma é {soma}")
