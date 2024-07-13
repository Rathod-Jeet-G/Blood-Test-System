from django.contrib import admin

# Register your models here.
from laboratoryapp.models import Test_category,Name_category,Appointment,LaboratoryRegister

class LaboratoryRegisterAdmin(admin.ModelAdmin):
    list_display=['Lid','Laboratoryfname','Laboratorymname','Laboratorylname','Laboratoryaddress','Laboratorycity','Laboratoryarea','Laboratorypincode','Laboratorycontactno','Laboratoryphoto']

# admin.site.register(LaboratoryRegister,LaboratoryRegisterAdmin)
# admin.site.register(Name_category)

admin.site.register(LaboratoryRegister,LaboratoryRegisterAdmin)
admin.site.register(Name_category)

class Test_category_(admin.ModelAdmin):
    list_display = ['lab_name','Test_name']
admin.site.register(Test_category,Test_category_)
admin.site.register(Appointment)