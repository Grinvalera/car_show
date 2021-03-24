from django.contrib import admin
from .models import Car, User, Image


class CarInstanceInline(admin.TabularInline):
    model = Car


class ImageInstanceInline(admin.TabularInline):
    model = Image


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = ('brand', 'model', 'body_type', 'year_issue')
    list_filter = ('brand', 'year_issue')

    inlines = [ImageInstanceInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name')
    inlines = [CarInstanceInline]


admin.site.register(Image)
