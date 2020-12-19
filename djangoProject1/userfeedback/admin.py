from django.contrib import admin


# Register your models here.
from userfeedback.models import UserFeedBack


class UserFeedBackAdmin(admin.ModelAdmin):
    list_display = ('publisher', 'title', 'servicing', 'mailing', 'publishing', 'orders')
    list_filter = ('servicing', 'mailing', 'publishing', 'orders')


admin.site.register(UserFeedBack, UserFeedBackAdmin)
