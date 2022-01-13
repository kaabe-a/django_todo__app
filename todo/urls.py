from django.urls import path
from . views import todo_list_view,todo_create_view,todo_detail_view,todo_delete_view,todo_update_view
app_name = 'todo'
urlpatterns = [
    path('',todo_list_view,name='todo_list'),
    path('todo/create/',todo_create_view,name='todo_create'),
    path('todo/<slug>/',todo_detail_view,name='todo_detail'),
    path('todo/<slug>/delete/',todo_delete_view,name='todo_delete'),
    path('todo/<slug>/update/',todo_update_view,name='todo_update'),
]