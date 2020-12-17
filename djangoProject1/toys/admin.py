from django.contrib import admin


# Register your models here.
from toys.models import Toys, CommentsOfToys, Liked


class LikedInline(admin.TabularInline):
    model = Liked


class ToysAdmin(admin.ModelAdmin):
    list_display = ('toy_name', 'manufacturer', 'suitable_for')
    list_filter = ('toy_name', 'manufacturer', 'suitable_for')
    inlines = (
        LikedInline,
    )


class CommentsOfToysAdmin(admin.ModelAdmin):
    list_display = ('toy', 'text', 'user')


admin.site.register(Toys, ToysAdmin)
admin.site.register(CommentsOfToys, CommentsOfToysAdmin)
admin.site.register(Liked)
