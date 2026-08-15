from django.urls import path
from . import views


urlpatterns = [

    path('', views.todo_list, name='home'),

    path('add', views.add_todo, name= 'add_todo'),

    path('view/<int:id>/', views.view_todo, name='view_todo'),

    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),

    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),

]