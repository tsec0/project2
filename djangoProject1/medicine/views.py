from django.views import generic as views

from medicine.models import Medicine


class MedicineListView(views.ListView):
    model = Medicine
    template_name = 'medicine/medicine_list.html'
    context_object_name = 'meds'


class MedicineDetailsView(views.DetailView):
    model = Medicine
    template_name = 'medicine/medicine_detail.html'
    context_object_name = 'medicine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
