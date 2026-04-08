from django.contrib import admin
from .models import Contact
from .models import EventRegistration

class EventAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'event', 'department', 'register_number', 'phone', 'submitted')
    search_fields = ('student_name', 'event')
    list_filter = ('event', 'department')
admin.site.register(EventRegistration, EventAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message_type', 'department','status', 'submitted')
    list_filter = ('status', 'message_type', 'department')
admin.site.register(Contact, ContactAdmin)

# Register your models here.
