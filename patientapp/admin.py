from django.contrib import admin
from .models import UserRegister,Userfeedback
# Register your models here.
class UserRegisterAdmin(admin.ModelAdmin):
        list_display=['uid','userfname','usermname','userlname','useraddress','usercity','userarea','userpincode','usercontactno']

admin.site.register(UserRegister,UserRegisterAdmin)
admin.site.register(Userfeedback)