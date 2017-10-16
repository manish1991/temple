from django.contrib import admin
from account.models import UserProfile

# Register your models here.

class AdminUserProfile(admin.ModelAdmin):
    list_display = ('user','phone_number')
    search_fields = ('phone_number',)


admin.site.register(UserProfile,AdminUserProfile)


