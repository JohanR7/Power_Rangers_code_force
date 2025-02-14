from django.shortcuts import render
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dotenv import load_dotenv
load_dotenv()
@csrf_exempt
def get_gemini_suggestions(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt_text = data.get("prompt")

            if not prompt_text:
                return JsonResponse({"error": "Missing prompt"}, status=400)

            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={os.getenv('GEMINI_API_KEY')}"
            payload = {"contents": [{"parts": [{"text": prompt_text}]}]}
            
            response = requests.post(url, json=payload)
            return JsonResponse(response.json())

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
def home(request):
    return render(request, "home.html")

def location(request):
    return render(request, "location.html")

def earth(request):
    return render(request, "earth.html")

def form(request):
    if request.method == "POST":
        data = request.POST
        print("Form Data:", data)
    return render(request, "form.html")
def analytics(request):
    return render(request, "analytics.html")