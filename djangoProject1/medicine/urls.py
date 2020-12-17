from django.urls import path

from medicine.views import MedicineDetailsView, MedicineListView

urlpatterns = [
    path('', MedicineListView.as_view(), name='list medicine'),
    path('detail/<int:pk>/', MedicineDetailsView.as_view(), name='medicine details'),
]
