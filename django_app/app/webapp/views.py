from django.shortcuts import render, get_object_or_404

from .models import Extension, Reservante, Reserva

def index(request):
    context = {'extensiones': Extension.objects.all()}
    return render(request, 'webapp/salas.html', context)

def login(request):
    return render(request, 'webapp/login.html')

def registrarse(request):
    return render(request, 'webapp/register.html')

def reservas(request):
    if request.method == 'POST':
        try:
            reservante = Reservante(
                nombre=request.POST['propietario'],
                email=request.POST['email'],
                numero_telefono=int(request.POST['numero']),
                extension=Extension.objects.get(pk=request.POST['extension'])
            )
            reservante.save()
            reserva = Reserva(
                propietario=get_object_or_404(Reservante, pk=reservante.id),
                clave=request.POST['password'],
                fecha_reserva=request.POST['fecha_reserva'],
                hora_inicio=request.POST['hora_inicio'],
                hora_fin=request.POST['hora_fin']
            )
            reserva.save()
        except Exception as error:
            reservante = Reservante.objects.get(nombre=request.POST['propietario'])
            reservante.delete()
            data = {'error_message': error}
            return render(request, 'webapp/reservas.html', data)
    context = {
        'reservas': Reserva.objects.all()
    }
    return render(request, 'webapp/reservas.html', context)
