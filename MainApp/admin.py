from django.contrib import admin
from .models import Post, Profile
admin.site.register(Post)


@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ["user","image"]

    raw_id_fields = ['user']
# Register your models here.
