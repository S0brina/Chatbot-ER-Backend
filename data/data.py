
greet_msg = """🌟 ¡Bienvenido al Asistente de Historias de Usuario! 🌟

Hola, soy tu chatbot personal diseñado para ayudarte a transformar tus procesos actuales en historias de usuario para el futuro.

¿Cómo puedo ayudarte hoy?

Ingresa un proceso actual (As-Is): Proporcióname detalles sobre cómo funciona tu proceso manualmente.
Generación de historias de usuario (To-Be): Con tu información, crearé historias de usuario adaptadas a un nuevo software que optimizará tu flujo de trabajo.

✨ ¡Comencemos a transformar tus ideas en soluciones efectivas! Envíame tu proceso As-Is. ✨"""
"""
MENSAJE DE BIENVENIDA
"""
process_params = {
        "temperature": 0.2,
        "top_k": 20,
        "top_p": 0.6,
        "max_new_tokens": 600,
        "length_penalty": 1
    }

proposal_params = {
        "temperature": 0.8,
        "top_k": 60,
        "top_p": 0.9,
        "max_new_tokens": 2000,
        "length_penalty": 1
    }

"""
HIPERPARAMETROS
"""
