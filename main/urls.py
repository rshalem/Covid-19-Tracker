from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='homepage'),
    path('countries/', views.country, name='countries'),
    path('countries/<name>', views.country_detail, name='country-detail'),
]
