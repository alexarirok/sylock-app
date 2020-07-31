from django.urls import path  
from profiles import views 

urlpatterns = [
    # path('', views.login, name = 'login'),
    path('base/', views.base, name = 'base'),
    path('profile/', views.profile, name = 'profile')

]