from django.db import models

# Create your models here.
class user_auth(models.Model):  # Renaming to PascalCase
    username = models.CharField((""), max_length=50)
    password = models.CharField((""), max_length=50)
    role = models.CharField((""), max_length=50)
    status = models.CharField((""), max_length=50)

    def __str__(self):
        return str(self.username) 

class employee_data(models.Model):
    emp_name=models.CharField((""), max_length=50)
    emp_email=models.CharField((""), max_length=50)
    emp_position=models.CharField((""), max_length=50)
    emp_contactno=models.BigIntegerField((""))
    auth=models.ForeignKey(user_auth, on_delete=models.CASCADE, related_name='user_auth')
    emp_date=models.DateTimeField((""), auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.emp_name
   
class work_data(models.Model):
    project_name=models.CharField((""), max_length=50)
   
    def __str__(self):
        return self.project_name
    
class work_task(models.Model):
    task_details=models.TextField((""))
    work=models.ForeignKey(work_data, on_delete=models.CASCADE, related_name='work_data')
    emp=models.ForeignKey(employee_data, on_delete=models.CASCADE, related_name='employee_data')
    due_date=models.DateField((""), auto_now=False, auto_now_add=False)
    status=models.CharField((""), max_length=50)
   
    def __str__(self):
        return self.task_details