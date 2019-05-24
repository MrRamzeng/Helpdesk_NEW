from django.contrib import admin
from help.models import Ticket, Account, Manual
from django.contrib.auth.admin import UserAdmin

class TicketForAdmin(admin.ModelAdmin):
    readonly_fields = ('client', 'cabinet', 'priority', 'text', 'published_date', 'published_time')
    ordering = ('-status', 'priority', 'published_time')
    search_fields = ('tickettype', 'cabinet', 'datetime')
    list_filter = ('priority', 'status', 'published_date', 'published_time')
    list_display = ('client', 'cabinet', 'text', 'published_date', 'status')
    list_per_page = 10

admin.site.register(Ticket, TicketForAdmin)
admin.site.register(Account, UserAdmin)
admin.site.register(Manual)
