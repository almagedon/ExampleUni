from django.contrib import admin
from .models import *
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    fields = ( 
        'user',
        'author',
        'title',
        'note',
        'created_date',
    )
    list_display = ( 
        'user',
        'author',
        'title',
        'note',
        'created_date',
    )
    '''list_filter = (
    		'author',
    		'title'
    )'''

admin.site.register(Notes, NotesAdmin)