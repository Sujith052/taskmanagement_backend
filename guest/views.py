from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from superadmin.models import *


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        # Parse the login data
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        # Check if login exists
        try:
            loginobj = user_auth.objects.get(username=username)
            print(username)
            
            # Validate password (if hashed, use check_password)
            if loginobj.password == password:  # Replace with `check_password(password, loginobj.password)` if hashed
                request.session['username'] = loginobj.username
                request.session['loginid'] = loginobj.id
                print("User ID:", request.session['loginid'])

                # Return role-based response
                return JsonResponse({'status': 'success','message': 'User login successful','role': loginobj.role,'username': loginobj.username,'loginid': loginobj.id,
                }, status=200)

                # If the account is inactive
            return JsonResponse({'status': 'error','message': 'Account is inactive',}, status=403)
        except loginobj.DoesNotExist:
            # If the username does not exist
            return JsonResponse({'status': 'error','message': 'Invalid username',}, status=404)

    # If the request method is not POST
    return JsonResponse({'status': 'error','message': 'Invalid request method',}, status=405)