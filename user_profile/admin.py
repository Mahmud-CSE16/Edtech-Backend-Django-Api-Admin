from django.contrib import admin
from .models import Profile,District

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_image','name','email','phone','address','level','district')
    list_display_links =('profile_image','name',)
    list_filter = ('level','district',)
    search_fields = ('name','level__name','district__name','address')
    list_per_page = 25
# admin.site.register(Profile, ProfileAdmin)
admin.site.register(District)