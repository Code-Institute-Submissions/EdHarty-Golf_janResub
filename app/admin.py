from django.contrib import admin

from .models import Teetime, UserAccount


@admin.register(Teetime)
class TeetimeAdmin(admin.ModelAdmin):
    list_filter = ('status', 'teetime_time', 'teetime_date')
    readonly_fields = ('teetime_id')
    list_display = ('teetime_id', 'user', 'teetime_date', 'teetime_time',
                    'player_count', 'status', 'created_on')
    search_fields = ('teetime_id', 'user')
    actions = ['approve_teetime']

    def approve_teetime(self, queryset):
        queryset.update(approve_teetime=True)


@admin.register(UserAccount)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number')
    search_fields = ('user', 'phone_number')
