from django.contrib import admin

from account.models import User


@admin.register(User)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    search_fields = ("id", "username")
