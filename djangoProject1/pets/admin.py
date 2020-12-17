from django.contrib import admin

# Register your models here.
from pets.models import Pet, Like, Sell, Comment


class LikeInline(admin.TabularInline):
    model = Like


class SellInline(admin.TabularInline):
    model = Sell


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'name', 'age', 'price')
    list_filter = ('animal', 'age', 'price', 'like')
    inlines = (
        LikeInline,
        SellInline,
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pet_id')


admin.site.register(Pet, PetAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
admin.site.register(Sell)
