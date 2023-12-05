from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

def index(request):
    user_agent_class = UserAgentView()
    user_agent = user_agent_class.get(request)
    print(user_agent)
    return render(request, 'descarga_apk/index.html', {'user_agent':user_agent})

class UserAgentView(View):
    def get(self, request,):
        user_agent = request.META.get('HTTP_USER_AGENT', 'Desconocido')
        return user_agent

def download(request):
    ruta_archivo = 'descarga_apk/static/apk/app-debug.apk'
    with open(ruta_archivo, 'rb') as archivo:
        response = HttpResponse(archivo.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="app-debug.apk"'
        return response