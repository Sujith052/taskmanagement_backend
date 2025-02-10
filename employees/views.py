import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from superadmin.models import *
from superadmin.serializers import *


# Create your views here.
@csrf_exempt 
def get_emptaskdata(request):
    if request.method == "GET":
       
        taskDetails = work_task.objects.select_related("work","emp") 
        serializer = workTaskSerializer(taskDetails, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt 
def getemployeetasks(request,id):
    if request.method == "GET":
       
        taskDetails = work_task.objects.select_related("work").filter(emp=id)
        print(taskDetails)
        serializer = workTaskSerializer(taskDetails, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def update_task(request, id):
    if request.method == 'GET':
        try:
            task = work_task.objects.get(id=id)
            status = task.status
            if status == 'pending':
                task.status = 'completed'
                task.save()
                return JsonResponse({'message': 'success'}, status=200)

            return JsonResponse({'error': 'Invalid status value'}, status=400)
        
        except work_task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def getstatuswise_task(request, status):
    if request.method == 'GET':
        print(status)
        worktaskDetails = work_task.objects.filter(status=status) 
        print(worktaskDetails)
        serializer = workTaskSerializer(worktaskDetails, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)