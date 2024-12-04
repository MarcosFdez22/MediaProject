from django.urls import path
from django.contrib import admin
from . import views

app_name = 'series'

urlpatterns = [
    path('', views.all_series, name='all_series'),  
    path('<int:serie_id>/', views.detail, name='detail'), 
    path('home/', views.home, name='home'), 
    path('admin/', admin.site.urls),
]
