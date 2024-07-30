from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'mobile', 'is_active', 'is_superuser', 'is_staff', 'created', 'updated', 'last_login')
    list_display_links = ('email',)
    list_filter = ('is_active', 'is_staff', 'created')
    search_fields = ('email', 'mobile')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('mobile',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created', 'updated')}),
    )
    
    readonly_fields = ('created', 'updated', 'last_login')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('last_login',)
        return self.readonly_fields

# Alternatively, you can use:
# admin.site.register(Account, AccountAdmin)

