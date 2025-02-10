from django.urls import path
from superadmin import views
 
urlpatterns = [
    path('emp_reg', views.emp_reg, name="emp_reg"),
    path('work_reg', views.work_reg, name="work_reg"),
    path('get_workdata', views.get_workdata, name="get_workdata"),
    path('get_employeedata', views.get_employeedata, name="get_employeedata"),
    path('add_task', views.add_task, name="add_task"),
    path('add_task/<id>', views.add_task, name="add_task"),
    path('getsearchwise_task/<workId>/<employeeId>', views.getsearchwise_task, name="update_task"),
    path('gettaskby_id/<id>', views.gettaskby_id, name="gettaskby_id"),
    path('update_task/<id>', views.update_task, name="update_task"),
]