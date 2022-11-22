from django.contrib import admin

# Register your models here.
from home.models import schedule,candidates
admin.site.register(schedule)
admin.site.register(candidates)