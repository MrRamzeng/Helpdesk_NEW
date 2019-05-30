from django.contrib import admin
from help.models import Ticket, Account, Manual
from django.contrib.auth.admin import UserAdmin
from django.contrib import auth
from .forms import CustomUserCreationForm, CustomUserChangeForm

class TicketForAdmin(admin.ModelAdmin):
    readonly_fields = ('client', 'cabinet', 'priority', 'text', 'published_date', 'published_time')
    ordering = ('-status', 'priority', 'published_time')
    search_fields = ('priority', 'cabinet', 'client__first_name')
    list_filter = ('priority', 'status', 'published_date')
    list_display = ('client', 'cabinet', 'text', 'published_date', 'status')
    list_per_page = 10

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ('last_name', 'first_name', 'email', 'is_staff')
    list_filter = ('last_name', 'first_name', 'email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('last_name', 'first_name', 'email', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('last_name', 'first_name', 'email', 'password1', 'password2', 'is_staff')}
        ),
    )
    search_fields = ('last_name', 'first_name', 'email')
    ordering = ('is_staff', 'last_name')
    list_per_page = 10

admin.site.unregister(auth.models.Group)
admin.site.register(Ticket, TicketForAdmin)
admin.site.register(Account, CustomUserAdmin)
admin.site.register(Manual)
