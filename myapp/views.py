from django.shortcuts import render
import random

def home(request):
    return render(request, "home.html")

def location(request):
    return render(request, "location.html")

def earth(request):
    return render(request, "earth.html")

def form_view(request):
    # Define image directory (inside /static/images/)
    image_dir = 'images/'  # No 'static/' prefix, Django handles it

    # List of available images
    image_list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']  # Add more if needed

    # Pick a random image
    selected_image = random.choice(image_list)

    # Pass image path to template
    return render(request, 'form.html', {'background_image': image_dir + selected_image})

def analytics(request):
    return render(request, "analytics.html")
