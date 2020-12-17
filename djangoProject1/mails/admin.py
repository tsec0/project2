from django.contrib import admin


# Register your models here.
from mails.models import Mail, IsRead


class ReadInLine(admin.TabularInline):
    model = IsRead


class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver')
    list_filter = ('sender', 'receiver')
    inlines = (
        ReadInLine,
    )


admin.site.register(Mail, MailAdmin)
admin.site.register(IsRead)