from django.shortcuts import render
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings

def home(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login') 
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}") 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/location/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
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
@login_required(login_url='login')
def location(request):
    return render(request, "location.html")
@login_required(login_url='login')
def earth(request):
    return render(request, "earth.html", {
        "mapbox_access_token": settings.MAPBOX_ACCESS_TOKEN,
    })
@login_required(login_url='login')
def form(request):
    if request.method == "POST":
        data = request.POST
        print("Form Data:", data)
    return render(request, "form.html")
@login_required(login_url='login')
def analytics(request):
    return render(request, "analytics.html")