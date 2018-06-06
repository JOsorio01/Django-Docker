from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webapp/login.html')

def registrarse(request):
    return render(request, 'webapp/register.html')
