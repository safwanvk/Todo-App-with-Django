from django.urls import path

from account import views

urlpatterns = [

    path('', views.home, name='home'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete')
]