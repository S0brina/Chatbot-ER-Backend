from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def generate_message(request):
    if request.method == 'POST':
        try:
            # Leer el cuerpo de la solicitud y convertirlo de JSON a un diccionario de Python
            data = json.loads(request.body)  # Aquí se corrige el error
            
            user_input = data.get('user_input', '').lower()  # Obtener el input del usuario

            # Condicional para decidir qué respuesta enviar
            if user_input == 'hola':
                response = 'Hola'
            elif user_input == 'aea':
                response = 'aea'
            else:
                response = f"No se reconoce el input: {user_input}"  # Mensaje por defecto para otros inputs

            # Devolver la respuesta como JSON
            return JsonResponse({"response": response}, status=200)

        except Exception as e:
            # Manejar errores y devolver un mensaje de error
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
