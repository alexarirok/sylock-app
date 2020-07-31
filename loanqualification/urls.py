from django.urls import path  
from loanqualification import views 

urlpatterns = [
    path('loanqualification/', views.loanqualification, name = 'loanqualification')

]