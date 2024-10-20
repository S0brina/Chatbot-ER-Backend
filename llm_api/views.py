from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from services.services import user_stories
from data.data import greet_msg
from services.LLaMa import generate_llm_response

@csrf_exempt
def generate_message(request):
    if not hasattr(generate_message, 'greeted'):
        generate_message.greeted = False 

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('user_input', '').lower()          
            if user_input == 'hola':
                response = greet_msg
                generate_message.greeted = True  
            elif generate_message.greeted:  
                response_llm = generate_llm_response(user_input)
                response = user_stories(response_llm)  
            else:
                response = "Enviar mensaje válido" 
            return JsonResponse({"response": response}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)
