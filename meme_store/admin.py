

# Register your models here.
from django.contrib import admin
from .models import Meme, Giphy

@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'video')

@admin.register(Giphy)
class GiphyAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'video')
