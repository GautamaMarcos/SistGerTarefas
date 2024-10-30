# ger_tarefas/urls.py
from django.urls import path
from . import views
from .views import edit_task_view

urlpatterns = [
    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_detail),
    path('tasks/<int:pk>/edit/', edit_task_view, name='edit_task_view'),
    path('cadastrar/', views.signup, name='signup'),
    # path('tasks/<int:pk>/pendente/', views.mark_task_concluida, name='mark_task_concluida'),
    # path('tasks/<int:pk>/concluida/', views.mark_task_pendente, name='mark_task_pendente'),
    
]









# ger_tarefas/urls.py
# from django.urls import path
# from . import views
# # from .views import signup, task_list, task_detail, task_create, task_update, task_delete

# urlpatterns = [
#     path('tasks/', views.task_list, name='task_list'),
#     path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
#     path('cadastrar/', views.signup, name='signup'),
#     path('tasks/create/', views.task_create, name='task_create'),
#     path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
#     path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
# ]



# urlpatterns = [
#     path('tasks/', views.task_list, name='task_list'),
#     path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
#     path('cadastrar/', signup, name='signup'),
#     path('tasks/', task_list, name='task_list'),
#     path('tasks/', task_create, name='task_create'),
#     path('tasks/<int:pk>/', task_detail, name='task_detail'),
#     path('tasks/<int:pk>/', task_update, name='task_update'),
#     path('tasks/<int:pk>/', task_delete, name='task_delete'),
# ]