from django.urls import path
from .views import home, delete_entry_by_name


urlpatterns = [
    path('', home, name='home'),
    path('delete/<str:entry_name>/', delete_entry_by_name, name='delete_entry_by_name'),

] 
