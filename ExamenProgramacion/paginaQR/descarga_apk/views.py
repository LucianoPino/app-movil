from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class UserAgentView(View):
    def get(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', 'Desconocido')
        # user_agent = self.convert_user_agent(user_agent)
        res = self.convert_user_agent(user_agent)
        return res

    def convert_user_agent(self,usr):
        usr = usr.lower()
        if usr.find('windows') != -1:
            return 'Windows'
        elif usr.find('android') != -1:
            return 'Android'
        elif usr.find('iphone') != -1:
            return 'iPhone'
        else:
            return 'Desconocido'


def index(request):
    user_agent_class = UserAgentView()
    user_agent = user_agent_class.get(request)
    return render(request, 'descarga_apk/index.html', {'user_agent':user_agent})

def download(request):
    ruta_archivo = 'descarga_apk/static/apk/app-debug.apk'
    with open(ruta_archivo, 'rb') as archivo:
        response = HttpResponse(archivo.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="app-qr.apk"'
        return response