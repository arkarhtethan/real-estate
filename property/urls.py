from django.urls import path
from .views import PropertyHomeView

app_name = 'property'

urlpatterns = [
    path('', PropertyHomeView.as_view(), name="home")
]