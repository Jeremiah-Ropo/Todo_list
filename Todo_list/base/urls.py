from django.urls import path
from .views import TaskCreate, DeleteView, TaskDetail, TaskList, TaskUpdate

app_name = 'base'

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task_delete'),

]
