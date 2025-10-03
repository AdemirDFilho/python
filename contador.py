print("ola mundo")
#contador-03-10-2025

#n = 0
#target = 1000
n = int(input("contar do número ... "))
target = int(input(" ... até o número ... "))
limite = int(input("... defina o limite da contagem ... "))
print(f"conte de {n} até {target}, mas não ultrapasse {limite}!")
while n < target:
    n += 1
    print(f"loop: execução nº {n}/{target}")
    if n >= limite:
        break


    
