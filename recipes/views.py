from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Gustavo Pacheco'
    })


# Create your views here.
