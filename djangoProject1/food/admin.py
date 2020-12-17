from django.contrib import admin


# Register your models here.
from food.models import Food, CommentsOfFood


class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'manufacturer', 'weight', 'weight_tag', 'suitable_for',)
    list_filter = ('food_name', 'manufacturer', 'weight_tag', 'suitable_for',)


class CommentsOfFoodAdmin(admin.ModelAdmin):
    list_display = ('food', 'text', 'user')


admin.site.register(Food, FoodAdmin)
admin.site.register(CommentsOfFood, CommentsOfFoodAdmin)
