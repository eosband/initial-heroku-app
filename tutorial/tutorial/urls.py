"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#
# from django.contrib import admin
# from django.urls import include, path
#
# urlpatterns = [
#     path('quickstart/', include('quickstart.urls')),
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.urls import include, path
from rest_framework import routers
from quickstart import views
import random

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



class Home(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, CSC630!')

class Personal(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("This did not work correctly.")

    def returnName(request, name):
        return HttpResponse("<h2>Hello, %s</h2>" % name)

class Random(View):

    def profile(request):
        data = {
            'number': random.randint(0,1000000000)
        }
        return JsonResponse(data)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('personal/<str:name>', Personal.returnName, name='personal'), #from https://docs.djangoproject.com/en/2.1/intro/tutorial03/
    path('random/', Random.profile, name='random')
]
