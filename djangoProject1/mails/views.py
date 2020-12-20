from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

# Create your views here.
from mails.forms import MailForm, OrderForm, AnswerMailForm
from mails.models import Mail, IsRead


class YourMailsListView(views.ListView):
    model = Mail
    template_name = 'mails/mail_list.html'
    context_object_name = 'mails'

    def get_object(self, query=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.get_object().user
        context['mails'] = self.get_object().mail_set.all()
        return context


class SuccessMailSend(views.ListView):
    model = Mail
    template_name = 'mails/success_send.html'
    context_object_name = 'mails'


class MailReadView(views.DetailView):
    model = Mail
    template_name = 'mails/mail_read.html'
    context_object_name = 'mail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mail = context[self.context_object_name]
        context['is_read'] = mail.isread_set.filter(receiver_id=self.request.user.userprofile.id).exists()
        return context


class AnswerMailView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'mails/mail_edit.html'
    model = Mail
    form_class = AnswerMailForm

    def get_success_url(self):
        url = reverse_lazy('success mail send')
        return url

    def get_object(self, query=None):
        pk = self.kwargs.get('pk', None)
        r_mail = self.request.mail if pk is None else Mail.objects.get(pk=pk)
        return r_mail

    def form_valid(self, form):
        mail = form.save(commit=False)
        mail.save()
        return super().form_valid(form)


class CreateMailView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'mails/mail_create.html'
    model = Mail
    form_class = MailForm

    def get_success_url(self):
        url = reverse_lazy('mail inbox')
        return url

    def form_valid(self, form):
        mail = form.save(commit=False)
        mail.sender = self.request.user.username
        mail.save()
        return super().form_valid(form)


class DeleteMailView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Mail
    template_name = 'mails/mail_delete.html'
    success_url = reverse_lazy('mail list')

    def get_success_url(self):
        url = reverse_lazy('mail inbox')
        return url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class IsReadMailView(views.View):

    def get(self, request, **kwargs):
        user_profile = request.user.userprofile
        mail = Mail.objects.get(pk=kwargs['pk'])

        isread = mail.isread_set.filter(receiver_id=request.user.userprofile.id).first()
        if isread:
            isread.delete()
        else:
            isread = IsRead(
                receiver=user_profile,
                mail=mail,
                isread='isread'
            )
            isread.save()
        return redirect('read mail', mail.id)
