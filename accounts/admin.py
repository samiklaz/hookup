from django.contrib import admin
from .models import Account, Profile, Data


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'city', 'phone_number')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_image', 'bio')


admin.site.register(Account, AccountAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Data)