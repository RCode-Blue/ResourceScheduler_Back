from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

# Register your models here.
from .models import User

class UserAdmin(BaseUserAdmin):
  add_fieldsets = (
    (None, {
      "fields": (
        "email", 
        "username", 
        "middle_name", 
        "preferred_name", 
        "dob", 
        "photo", 
        "password1", 
        "password2")
    }),
    ("Permissions", {
      "fields": ("is_superuser")
    })
  )

  fieldsets = (
    (None, {
      "fields": (
        "email", 
        "username", 
        "middle_name", 
        "preferred_name", 
        "dob", 
        "photo", 
        "password")
    }),
    ("Permissions", {
      "fields": ("is_superuser",)
    })
  )

  list_display = ["email", "username", "middle_name", "preferred_name", "dob", "photo"]
  # list_display = ["email", "username"]
  search_fields = ("email", "username")
  ordering = ("email",)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)