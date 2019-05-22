from django.contrib import admin
from help.models import Ticket, Account, Tutorial
from django.contrib.auth.admin import UserAdmin

admin.site.register(Ticket)
admin.site.register(Account, UserAdmin)
admin.site.register(Tutorial)
