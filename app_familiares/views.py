from django.http import HttpResponse
from django.template import loader
from app_familiares.models import familiar

def vista1(request):
    queryset = familiar.objects.all()
    dicc = {'familia': queryset}

    plantilla = loader.get_template("template1.html")
    
    documento = plantilla.render(dicc)
    
    return HttpResponse(documento)





