from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def panel(request):
    contexto = {
        'usuarios': 1711,
        'ventas': 2805,
    }
    return render(request, 'panel.html', contexto)