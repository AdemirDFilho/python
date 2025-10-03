print("_________________EXERCIO-COMPETICAO-OLIMPICA___________")
#TENTANDO MEHLORAR O STATUS IMPRESSO DO ATLETA

# 18 a 35
idade = 30
#condicionamento fisico
fisico = False
#permissão médica
medico = True

print("Programa para validar a entrada do atleta na competição olímpica.")
print(f"Ficha do Atleta")

print(f"Idade: {idade} anos")

if fisico == True:
    print(f"Condicionamento Fisico: BOM")
else:
    print(f"Condicionamento Fisico: RUIM")

if medico == True:
    print(f"TEM Permissão Médica;")
else:
    print(f"NÃO Permissão Médica;")


print(f"________________________RESULTADO__________________")
if idade >=18 and idade <=35 and (fisico or medico):
    print("APTO!!")
else:
     print("INAPTO")

print(".........FIM..........")
