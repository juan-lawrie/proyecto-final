from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html")

    from django.shortcuts import render
    from ejemplo.models import Familiar
    def monstrar_familiares(request):
        lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})