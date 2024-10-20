from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from controller.controler import greet_msg, generate_llm

@csrf_exempt
def generate_message(request):
    # Variable para almacenar el estado de si se envió el saludo
    if not hasattr(generate_message, 'greeted'):
        generate_message.greeted = False  # Inicializa la variable como False

    if request.method == 'POST':
        try:
            # Leer el cuerpo de la solicitud y convertirlo de JSON a un diccionario de Python
            data = json.loads(request.body)
            user_input = data.get('user_input', '').lower()  # Obtener el input del usuario

            # Condicional para decidir qué respuesta enviar
            if user_input == 'hola':
                response = greet_msg
                generate_message.greeted = True  # Actualiza el estado a True
            elif generate_message.greeted:  # Verifica si se ha enviado 'hola' antes
                response = generate_llm(user_input)  # Llama al método generate_llm
            else:
                response = "Enviar mensaje válido"  # Mensaje si no se ha saludado

            # Devolver la respuesta como JSON
            return JsonResponse({"response": response}, status=200)

        except Exception as e:
            # Manejar errores y devolver un mensaje de error
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
