from django.contrib import admin
from .models import Trial

class TrialAdmin(admin.ModelAdmin):

    list_display = ('year', 'month', 'temp', 'fall')

admin.site.register(Trial, TrialAdmin)
