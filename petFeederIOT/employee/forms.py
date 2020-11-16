from django import forms
from employee.models import VoiceCommand,BowlWeight,FoodContainerWeight,FoodLevelMonitor

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = "__all__"

class VoiceCommandForm(forms.ModelForm):
    class Meta:
        model = VoiceCommand
        fields = "__all__"

class BowlWeightForm(forms.ModelForm):
    class Meta:
        model = BowlWeight
        fields = "__all__"

class FoodContainerWeightForm(forms.ModelForm):
    class Meta:
        model = FoodContainerWeight
        fields = "__all__"

class FoodLevelMonitorForm(forms.ModelForm):
    class Meta :
        model = FoodLevelMonitor
        fields = "__all__"
