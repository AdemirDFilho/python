print("Disqus_Mbit")

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

    # Remove múltiplos underlines
    texto = re.sub(r'_+', '_', texto)

    # Remove underline no início ou final
    texto = texto.strip('_')

    return texto

texto = input('digite o texto ... ')
print(slugify(texto))

url = slugify(texto)
print(f"https://disqus.com/home/discussion/mbit/{url}")

#Obrigado chatGPT!