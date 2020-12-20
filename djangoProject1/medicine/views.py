from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from mails.forms import OrderForm
from mails.models import Mail
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


class CreateOrderMedicineView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'mails/order_create.html'
    model = Mail
    form_class = OrderForm

    def get_object(self, query=None):
        pk = self.kwargs.get('pk', None)
        medicine = self.request.medicice if pk is None else Medicine.objects.get(pk=pk)
        return medicine

    def get_success_url(self):
        url = reverse_lazy('mail inbox')
        return url

    def form_valid(self, form):
        mail = form.save(commit=False)
        mail.receiver = self.request.user.userprofile
        mail.receiver_id = self.request.user.userprofile.id
        mail.sender = 'SiteAdmin'
        mail.content = str(self.get_object())
        mail.title = 'Thank you for your order!'
        mail.save()
        return super().form_valid(form)

