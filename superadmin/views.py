import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from superadmin.models import *
from datetime import datetime
from superadmin.serializers import *


# Create your views here.
@csrf_exempt
def emp_reg(request):
    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        employee_email = request.POST.get('employee_email')
        job_position = request.POST.get('job_position')
        employee_contactno = request.POST.get('employee_contactno')
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = "employee"
        status = "active"
        
        # Insert into user_auth table       
        userAuth = user_auth.objects.create(
            username=username,
            password=password,
            role=role,
            status=status,
            )
        
        # Insert into employee_data table with foreign key reference
        employee_data.objects.create(
            emp_name=employee_name,
            emp_email=employee_email,
            emp_position=job_position,
            emp_contactno=employee_contactno,
            auth_id=userAuth.id,
            emp_date=datetime.now()
        )
                
        return JsonResponse({'message': 'registered successfully!'}, status=201)
    
@csrf_exempt
def work_reg(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectname')
        
        # Insert into employee_data table with foreign key reference
        work_data.objects.create(
            project_name=project_name,
        )
                
        return JsonResponse({'message': 'registered successfully!'}, status=201)
    
@csrf_exempt 
def get_workdata(request):
    if request.method == "GET":
        # userid = request.session['loginid']
        workDataDetails = work_data.objects.all() 
        serializer = workDataSerializer(workDataDetails, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt 
def get_employeedata(request):
    if request.method == "GET":
        # userid = request.session['loginid']
        employeeDataDetails = employee_data.objects.all() 
        serializer = employeeSerializer(employeeDataDetails, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def add_task(request,id=0):
    if request.method == 'POST':
        work = request.POST.get('work')
        employee = request.POST.get('employee')
        task = request.POST.get('projecttask')
        due_date = request.POST.get('due_date')
        status="pending"
        
        # Insert into employee_data table with foreign key reference
        work_task.objects.create(
            task_details=task,work=work_data.objects.get(id=work),emp=employee_data.objects.get(auth=employee),due_date=due_date,status=status
        )
                
        return JsonResponse({'message': 'registered successfully!'}, status=201)
    
    elif request.method == "DELETE":
        tasklist = work_task.objects.get(id=id)
        tasklist.delete()
        
        return JsonResponse({"success":True})
    
@csrf_exempt
def getsearchwise_task(request, workId, employeeId):
    if request.method == 'GET':
        print(workId)
        print(employeeId)
        worktaskDetails = work_task.objects.filter(work=workId,emp=employeeId) 
        print(worktaskDetails)
        serializer = workTaskSerializer(worktaskDetails, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def gettaskby_id(request, id):
    if request.method == 'GET':
        print(id)
        worktaskDetails = work_task.objects.filter(id=id) 
        print(worktaskDetails)
        serializer = workTaskSerializer(worktaskDetails, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)
    
@csrf_exempt
def update_task(request,id=0):
    if request.method == "POST":
        work = request.POST.get('work')
        employee = request.POST.get('employee')
        task = request.POST.get('projecttask')
        print(task)
        due_date = request.POST.get('due_date')
        status="pending"
        
        tasklist = work_task.objects.get(id=id)
        
        tasklist.task_details = task
        tasklist.work = work_data.objects.get(id=work)
        tasklist.emp = employee_data.objects.get(id=employee)
        tasklist.due_date = due_date
        
        tasklist.save()
        
        return JsonResponse({"success":True})