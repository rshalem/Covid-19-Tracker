from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [

    path('', views.home, name='homepage'),
    path('news/', views.news, name='news'),

    path('countries/', views.country, name='countries'),
    path('countries/<name>', views.country_detail, name='country-detail'),

]
