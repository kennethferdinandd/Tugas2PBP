from django.urls import path
from todolist.views import register, login_user, show_todolist, create_task,trigger_is_finished,delete_task


app_name = "todolist"
urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', register, name="logout"),
    path('create-task/', create_task, name='create_task'),
    path('trigger-is-finished/<int:id>/', trigger_is_finished, name='trigger_is_finished'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
]