#Disqus_Mbit.py
#Acessar comentários de posts do blog MeioBit.com via central de comentarios do Disqus.
#Útil para acessar comentários de posts antigos, cujos comentários disqus não "carregam" mais no site.

# Disqus_Mbit = https://disqus.com/home/discussion/mbit/titulo_do_artigo_em_minusculas_sem_caractere_especial
# Se não me falha a memória, casos em que link e título divergem, prevalece o título. 

# EXEMPLO:
# LINK POST: https://meiobit.com/434479/perseverance_envia_os_mais_incriveis_videos_de_marte/
# LINK DISQUS: https://disqus.com/home/discussion/mbit/perseverance_envia_os_mais_incriveis_videos_de_marte

#https://meiobit.com/467076/nasa-retorno-jared-isaacman-plano-infalivel-sean-duffy/
#NASA: sobre Jared Isaacman e planos infalíveis
#[NAO FUNCIONA - MAIUSCULAS] https://disqus.com/home/discussion/mbit/NASA_sobre_Jared_Isaacman_e_planos_infaliveis
#[FUNCIONA] https://disqus.com/home/discussion/mbit/nasa_sobre_jared_isaacman_e_planos_infaliveis

import re
import unicodedata

print("ola mundo - disqus mbit")

titulo = input("cole o título do artigo aqui...")
print(f"Titulo colado: '{titulo}'.")

#print(f"https://disqus.com/home/discussion/mbit/{titulo}")

#remove espaços do inicio e fim
titulo = titulo.strip()
print(titulo)

#converte tudo para minusculas 
titulo = titulo.lower()
print(titulo)

#remover acentos
import unicodedata
titulo = unicodedata.normalize('NFD', titulo)
titulo = ''.join(c for c in titulo if unicodedata.category(c) !='Mn')
print(titulo)

import re
#REMOVER CARACTERES ESPECIAIS
#titulo = re.sub(r'[^a-z0-9\s]',' ',titulo) #PROBLEMA: REMOVE LETRAS ACENTUADAS SEM SUBSTIUI-LAS. 
titulo = re.sub(r'[^a-z0-9\s]','',titulo)

