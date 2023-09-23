from django.contrib import admin

from products.admin import BasketAdmin

from .models import Customuser, EmailVerification


@admin.register(Customuser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expirathion',)
    fields = ('code', 'user', 'expirathion', 'created')
    readonly_fields = ('created',)
