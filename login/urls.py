from . import views
from django.urls import path


app_name = 'login'
urlpatterns = [
    path('login/<str:sid>/<str:pwd>/', views.grade, name='grade')
]