from django.contrib import admin
from catalog.models import Musician, Genre, Album, AlbumInstance

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'musician', 'year', 'display_genre')
    
admin.site.register(Album, AlbumAdmin)

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0
    
class MusicianAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
    
admin.site.register(Musician)

admin.site.register(Genre)

class AlbumInstanceAdmin(admin.ModelAdmin):
    list_display = ('album', 'status', 'sale_date', 'id')
    list_filter = ('status', 'sale_date')

    fieldsets = (
        (None, {
            'fields': ('album', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'sale_date')
        }),
    )

admin.site.register(AlbumInstance, AlbumInstanceAdmin)
