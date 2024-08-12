from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('about',views.about),
    path('dashboard',views.dashboard),
    path('save',views.save_file_in_db),
    path('getexp',views.get_expiry_date)
]