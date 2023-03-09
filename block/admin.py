from django.contrib import admin
from block.models import MyUser,slider,team,blog
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(blog)
@admin.register(slider)
class sliderAdmin(admin.ModelAdmin):
    

    list_filter = ('caption',)
    list_display = ("caption", "image")
    search_fields = ['caption']
@admin.register(team)
class teamAdmin(admin.ModelAdmin):
    

    list_filter = ('name',)
    list_display = ("name", "image")
    search_fields = ['name']
# admin.site.register(MyUser,UserAdmin)
# UserAdmin.fieldsets +=("Custom",{'fields':('mobile_number','birth_date','otp')}),
# Register your models here.
