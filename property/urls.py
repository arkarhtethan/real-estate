from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('', views.PropertyHomeView.as_view(), name="home"),
    path('property-list/', views.PropertyListView.as_view(), name="list"),
]