import re
greet_msg = """🌟 ¡Bienvenido al Asistente de Historias de Usuario! 🌟

Hola, soy tu chatbot personal diseñado para ayudarte a transformar tus procesos actuales en historias de usuario para el futuro.

¿Cómo puedo ayudarte hoy?

Ingresa un proceso actual (As-Is): Proporcióname detalles sobre cómo funciona tu proceso manualmente.
Generación de historias de usuario (To-Be): Con tu información, crearé historias de usuario adaptadas a un nuevo software que optimizará tu flujo de trabajo.

✨ ¡Comencemos a transformar tus ideas en soluciones efectivas! Envíame tu proceso As-Is. ✨"""

def filter_us(text):
    historias_usuario = []
    lineas = text.strip().splitlines()
    
    # Patrón para capturar líneas que cumplan con el formato de historias de usuario
    patron = re.compile(r'\bComo\b.*\b(quiero|deseo)\b.*?(\.|\n)', re.IGNORECASE)

    for linea in lineas:
        match = patron.search(linea)
        if match:
            # Agregar la línea hasta el primer punto encontrado
            historias_usuario.append(match.group(0).strip())
    
    return historias_usuario

# Método que recibe el input del usuario y llama a filter_us para filtrar historias de usuario
def generate_llm(user_input):
    # Llama a filter_us para filtrar las historias de usuario del input
    historias_filtradas = filter_us(user_input)

    # Capitalizar la primera letra y numerar cada historia
    historias_numeradas = []
    for i, historia in enumerate(historias_filtradas, start=1):
        historia_capitalizada = historia[0].upper() + historia[1:]  # Capitalizar la primera letra
        historias_numeradas.append(f"{i}. {historia_capitalizada}")  # Numerar y agregar a la lista
    
    # Unir las historias numeradas en un solo string con saltos de línea
    return "\n".join(historias_numeradas)