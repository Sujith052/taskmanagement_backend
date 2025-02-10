from rest_framework import serializers
from superadmin.models import *
# from guest.serializers import *

class workDataSerializer(serializers.ModelSerializer):
    # time_slot_details = timeSlotSerializer(source='time_slot', read_only=True)  
    class Meta:
        model = work_data
        fields = '__all__'
        
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_data
        fields = '__all__'
        
class workTaskSerializer(serializers.ModelSerializer):
    workDetails = workDataSerializer(source='work', read_only=True)  
    empDetails = employeeSerializer(source='emp', read_only=True)

    class Meta:
        model = work_task
        fields = '__all__'