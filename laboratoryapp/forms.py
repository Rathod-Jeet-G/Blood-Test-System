from django import forms
from laboratoryapp.models import Appointment,LaboratoryRegister, Test_category

class appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields='__all__'

class labregisterform(forms.ModelForm):
    class Meta:
        model = LaboratoryRegister
        fields='__all__'

class Testform(forms.ModelForm):
    class Meta:
        model = Test_category
        fields= '__all__'