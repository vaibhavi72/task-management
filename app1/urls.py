from django.contrib import admin
from django.urls import path
from app1.views import home , login , signup , add_Task , signout , delete_task , change_task



urlpatterns = [
    path('', home , name='home'),
    path('login/', login , name='login'),
    path('signup/', signup), 
    path('add-Task/', add_Task),
    path('delete-task/<int:id>', delete_task),
    path('change-status/<int:id>/<str:status>', change_task),
    path('logout/', signout),
]