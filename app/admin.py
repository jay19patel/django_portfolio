from django.contrib import admin
from .models import*


admin.site.register(Project)
admin.site.register(Gallery)

@admin.register(Message)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("sender_name","sender_email", "full_description","sender_phone_no")