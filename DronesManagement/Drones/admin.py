from django.contrib import admin

# Register your models here.
from .models import Drone, Medication, Command, Transaction

admin.site.register(Drone)
admin.site.register(Medication)
admin.site.register(Command)
admin.site.register(Transaction)