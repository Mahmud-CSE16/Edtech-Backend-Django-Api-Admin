from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import Profile,District

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    title = "Profile Info"
    verbose_name = "Profile Info"

#user with profile
admin.site.unregister(User)
@admin.register(User)
class UserAdmin(AuthUserAdmin):
    fieldsets = [
        (None,{
            'fields':('username','password',),
        }),
        ('Permissions',{
            'fields':('is_staff','is_superuser',),
        }),
        ('More Info',{
            'classes': ('collapse',),
            'fields':('is_active','last_login','date_joined',),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions',),
        }),
    ]
    inlines = [
        ProfileInline,
    ]


# Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_image','name','email','phone','address','level','district')
    list_display_links =('profile_image','name',)
    list_filter = ('level','district',)
    search_fields = ('name','level__name','district__name','address')
    list_per_page = 25

admin.site.register(District)