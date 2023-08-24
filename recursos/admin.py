from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('businessentityid', 'firstname', 'middlename', 'lastname', 'modifieddate')


admin.site.register(Person, PersonAdmin)