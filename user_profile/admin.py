from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import Profile,District
from django.utils.safestring import mark_safe
from django.db.models.functions import Lower


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    title = "Profile Info"
    verbose_name = "Profile Info"

#user with profile
admin.site.unregister(User)
@admin.register(User)
class UserAdmin(AuthUserAdmin):
    inlines = [
        ProfileInline,
    ]
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
    list_display = ('profile_image','profile','profile_email','user_sub_level','is_staff','is_active',)
    list_filter = ('profile__level','profile__sub_level','profile__district','is_staff','is_active','is_superuser',)
    search_fields = ['profile__name','profile__district__name','profile__sub_level__name','profile__level__name',]
    list_display_links =('profile_image','profile',)
    ordering = ('profile__name',)
    list_per_page = 25


    # profile_email
    def profile_email(self, obj):
        return obj.profile.email

    profile_email.short_description = 'Email'

    # profile_email
    def user_level(self, obj):
        return obj.profile.level

    user_level.short_description = 'Level'

    # profile_email
    def user_sub_level(self, obj):
        return obj.profile.sub_level

    user_sub_level.short_description = 'Sub->Level'

    # profile pic
    def profile_image(self,obj):
        if(obj.profile.profile_pic_url != None and obj.profile.profile_pic_url != "" ):
            return mark_safe('<img src="%s" width="50" height="50" />' % (obj.profile.profile_pic_url))
        else:
            return mark_safe('<img src="/static/img/user_icon.png" width="50" height="50" />')

    profile_image.short_description = 'Profile Image'
    
    


# Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_image','name','email','phone','address','level','district')
    list_display_links =('profile_image','name',)
    list_filter = ('level','district',)
    search_fields = ('name','level__name','district__name','address')
    list_per_page = 25

admin.site.register(District)