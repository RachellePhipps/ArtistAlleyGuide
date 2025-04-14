from django.contrib import admin
from .models import Convention, ConventionImage
from .models import Comment

class ConventionImageInline(admin.TabularInline):
    model = ConventionImage
    extra = 1  # Number of empty image fields displayed

# admin for convention model
class ConventionAdmin(admin.ModelAdmin):
    inlines = [ConventionImageInline]

# register convention
admin.site.register(Convention, ConventionAdmin)

# admin for comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'con', 'created_at', 'short_text')
    list_filter = ('created_at', 'con', 'user')
    search_fields = ('text', 'user__username', 'con__name')

    def short_text(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    short_text.short_description = 'Comment'

# register comment 
admin.site.register(Comment, CommentAdmin)
