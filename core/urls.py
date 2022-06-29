from .views import double_save, double_list, double3
from django.urls import path


urlpatterns = [
    path('double_save', double_save, name='double_save'),
    path('double_list', double_list, name='double_list'),
    path('double_already_save', double_save, name='double_already_save'),
    path('', double3, name='double2'),
]