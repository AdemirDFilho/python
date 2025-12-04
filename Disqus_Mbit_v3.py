print("Disqus_Mbit")

# Acessar comentários de posts do blog MeioBit.com via central de comentarios do Disqus.
# Útil para acessar comentários de posts antigos, cujos comentários disqus não "carregam" mais no site.

# Disqus_Mbit = https://disqus.com/home/discussion/mbit/titulo_do_artigo_em_minusculas_sem_caractere_especial
# Se não me falha a memória, casos em que link e título divergem, prevalece o título. 

# EXEMPLO:
# LINK POST: https://meiobit.com/434479/perseverance-envia-os-mais-incriveis-videos-de-marte/
# LINK DISQUS: https://disqus.com/home/discussion/mbit/perseverance_envia_os_mais_incriveis_videos_de_marte

import re
import unicodedata

def slugify(texto: str) -> str:
    # Converte para minúsculas
    texto = texto.lower()

    # Remove acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')

    # Mantém apenas letras, números e espaços
    texto = re.sub(r'[^a-z0-9\s-]', '', texto)

    # Substitui espaços por underline
    texto = re.sub(r'\s+', '_', texto)

    # Substitui HÍFENS por underline
    texto = re.sub(r'\-+', '_', texto)
    
    # Remove múltiplos underlines
    texto = re.sub(r'_+', '_', texto)

    # Remove underline no início ou final
    texto = texto.strip('_')

    return texto

while True:
    texto = input('Cole o título do artigo MeioBit ... ')
    #print(slugify(texto))

    url = slugify(texto)
    print(f"https://disqus.com/home/discussion/mbit/{url}")

#Obrigado chatGPT!

