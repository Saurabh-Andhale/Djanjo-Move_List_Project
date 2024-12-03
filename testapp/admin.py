from django.contrib import admin
from testapp.models import Movie

class movieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']
admin.site.register(Movie,movieAdmin)
