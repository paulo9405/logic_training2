from django.urls import path
from .views import double_list, double_create


urlpatterns = [
    path('', double_list, name='double_lst'),
    path('double_create', double_create, name='double_create'),
]
