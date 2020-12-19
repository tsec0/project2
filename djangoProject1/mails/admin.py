from django.contrib import admin


# Register your models here.
from mails.models import Mail, IsRead


class ReadInLine(admin.TabularInline):
    model = IsRead


class MailAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'title', 'quantity', 'offer', 'content')
    list_filter = ('sender', 'receiver', 'title', 'quantity')
    inlines = (
        ReadInLine,
    )


admin.site.register(Mail, MailAdmin)
admin.site.register(IsRead)
