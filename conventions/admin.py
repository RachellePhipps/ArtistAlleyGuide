from django.contrib import admin
from .models import Convention, ConventionImage


class ConventionImageInline(admin.TabularInline):
    model = ConventionImage
    extra = 1  # Number of empty image fields displayed

class ConventionAdmin(admin.ModelAdmin):
    inlines = [ConventionImageInline]

admin.site.register(Convention, ConventionAdmin)


