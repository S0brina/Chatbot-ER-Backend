import re

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\.\S+', '', text)
    allowed_chars = re.compile(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ .,!?;:\'\"()-]')
    text = allowed_chars.sub('', text)
    text = re.sub(r'\s+', ' ', text).strip()
    cleaned_text = text.lower()
    
    return cleaned_text

def filter_us(text):
    historias_usuario = []
    lineas = text.strip().splitlines()
    patron = re.compile(r'\bComo\b.*\b(quiero|deseo)\b.*?(\.|\n)', re.IGNORECASE)

    for linea in lineas:
        match = patron.search(linea)
        if match:
            historias_usuario.append(match.group(0).strip())
    return historias_usuario

def user_stories(user_input):
    historias_filtradas = filter_us(user_input)
    historias_unicas = list(set(historias_filtradas))

    historias_numeradas = []
    for i, historia in enumerate(historias_unicas, start=1):
        historia_capitalizada = historia[0].upper() + historia[1:]  
        historias_numeradas.append(f"{i}. {historia_capitalizada}") 
    
    return "\n".join(historias_numeradas)