from django.contrib import admin

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)



class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
