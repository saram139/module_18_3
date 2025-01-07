from django.shortcuts import render

def platform(request):
    return render(request, "third_task/platform.html")

def store(request):
    title = "Игры"
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {'title': title, 'games': games}
    return render(request, "third_task/store.html", context)

def cart(request):
    return render(request, "third_task/cart.html")
# Create your views here.
