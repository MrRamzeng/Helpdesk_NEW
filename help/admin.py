from django.contrib import admin
from help.models import Ticket, Account, Manual
from django.contrib.auth.admin import UserAdmin
from django.contrib import auth

class TicketForAdmin(admin.ModelAdmin):
    readonly_fields = ('client', 'cabinet', 'priority', 'text', 'published_date', 'published_time')
    ordering = ('-status', 'priority', 'published_time')
    search_fields = ('priority', 'cabinet', 'client__first_name')
    list_filter = ('priority', 'status', 'published_date')
    list_display = ('client', 'cabinet', 'text', 'published_date', 'status')
    list_per_page = 10

admin.site.unregister(auth.models.Group)
admin.site.register(Ticket, TicketForAdmin)
admin.site.register(Account, UserAdmin)
admin.site.register(Manual)
