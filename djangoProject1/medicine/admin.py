from django.contrib import admin


# Register your models here.
from medicine.models import Medicine


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'manufacturer', 'weight', 'weight_tag', 'suitable_for', 'ingredients')
    list_filter = ('medicine_name', 'manufacturer', 'weight_tag', 'suitable_for', 'ingredients')


admin.site.register(Medicine, MedicineAdmin)
