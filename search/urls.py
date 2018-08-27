from . import views
from django.urls import path

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('grade/<str:sid>/<str:pwd>/', views.grade, name='grade'),
    path('table/<str:sid>/<str:pwd>/', views.time_table, name='time_table')
]
