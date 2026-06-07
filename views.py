import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Temporary database for simulation
url_database = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def shorten_url(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        short_code = generate_short_url()
        url_database[short_code] = long_url
        return render(request, "result.html", {"short_url": f"http://127.0.0.1:8000/{short_code}"})
    return render(request, "index.html")

def redirect_url(request, short_code):
    long_url = url_database.get(short_code)
    if long_url:
        return redirect(long_url)
    return HttpResponse("URL Not Found", status=404)
