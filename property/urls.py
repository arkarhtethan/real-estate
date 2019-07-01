from django.urls import path
from .views import index

app_name = 'property'

urlpatterns = [
    path('', index, name="home")
]