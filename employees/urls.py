from django.urls import path
from employees import views
 
urlpatterns = [
    path('get_emptaskdata', views.get_emptaskdata, name="get_emptaskdata"),
    path('updatetask/<id>', views.update_task, name="update_task"),
    path('getemployeetasks/<id>', views.getemployeetasks, name="getemployeetasks"),
    path('getstatuswise_task/<status>', views.getstatuswise_task, name="getstatuswise_task"),
]