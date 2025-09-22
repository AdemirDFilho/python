print("_________________EXERCIO-1___________")
#preco = 5
#saldo = float(input("quanto dinheiro você tem? "))
#if preco <= saldo:
#          print("compra do PÃO realizada com sucesso!!")
#else:
#    print("saldo insuficiente para comprar PÃO :-(")
#print(".........FIM..........")


print("_________________EXERCIO-2___________")

#temperatura = 990
#print(f"temperatura atual {temperatura}ºC")
#
#if temperatura <= 10:
#    print("frio")
#elif temperatura < 26:
#    print("normal")
#elif temperatura < 35:
#    print("quente")
#elif temperatura < 100:
#    print("inferno")
#elif temperatura > 100:
#    print("fim do mundo")
#print(".........FIM..........")
#
print("_________________EXERCIO-3___________")

#hora = 24
#print(f"hora atual é {hora} hora(s)")
#
#if hora <=6:
#    print("Deus ajuda quem cedo Madruga!")
#elif hora <=12:
#    print("bom dia")
#elif hora <=18:
#    print("boa tarde")
#elif hora <= 24:
#    print("boa noite")
#
#print(".........FIM..........")


print("_________________EXERCIO-4___________")
#as condições devem ser feitas em uma única estrutura!

# 18 a 35
idade = 30

#condicionamento fisico
fisico = False

#premissão médica
medico = False

print("Programa para validar a entrada do atleta na competição olímpica.")
print(f"Ficha do Atleta: {idade} anos; Cond. Fisico {fisico}; Perm. Médica {medico};")


if idade >= 18 and idade <= 35:
    if fisico or medico:
     print("O atleta está APTO à competição.")
    else:
     print("INAPTO")
else:
    print("O atleta NÃO está apto à competir.")

print(".........FIM..........")

print("_________________EXERCIO-4.melhoria___________")
#as condições devem ser feitas em uma única estrutura!

# 18 a 35
idade = 30

#condicionamento fisico
fisico = False

#permissão médica
medico = False

#cond =
#if fisico == True:
# cond = BOM
#else: cond = RUIM

#perm =
#if medico == True:
# perm = SIM
#else: perm = NÃO


print("Programa para validar a entrada do atleta na competição olímpica.")
print(f"Ficha do Atleta: {idade} anos; Cond. Fisico {fisico}; Perm. Médica {medico};")


if idade >= 18 and idade <= 35:
    if fisico or medico:
     print("O atleta está APTO à competição.")
    else:
     print("INAPTO")
else:
    print("O atleta NÃO está apto à competir.")

print(".........FIM..........")


print("_________________EXERCIO-4 [SOLUÇÃO DO MESTRE]___________")

# 18 a 35
idade = 40
#condicionamento fisico
fisico = True
#permissão médica
medico = True

print("Programa para validar a entrada do atleta na competição olímpica.")
print(f"Ficha do Atleta: {idade} anos; Cond. Fisico {fisico}; Perm. Médica {medico};")

if idade >=18 and idade <=35 and (fisico or medico):
    print("APTO!!")
else:
     print("INAPTO_FORA")

print(".........FIM..........")





























    

            
