from django.contrib import admin
from .models import Student
@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','Uname','email','password']

