from django.urls import path,include
from rest_framework.authtoken import views
from .views import home
#from api import category
urlpatterns = [
    path('',home,name="api.home"),
    path('category/',include('api.category.urls'))
]