from django.contrib.auth import views as auth_views, login
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.views import generic as views
# Create your views here.

from accounts.forms import SignUpForm, UserProfileForm
from accounts.models import UserProfile


class UserProfileView(views.UpdateView):
    template_name = 'accounts/user_profile.html'
    form_class = UserProfileForm
    model = UserProfile
    success_url = reverse_lazy('current')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.get_object().user
        # context['cart'] = self.get_object().cart_set.all() # should create cart
        # context['mails'] = self.get_object().cart_set.all() # should create mails
        # context['userfeedback'] = self.get_object().userfeedback_set.all() # should create userfeedback
        return context


class SignInView(auth_views.LoginView):
    template_name = 'accounts/sign_in.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('current')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # auth не трябва да се бърка горе
        return valid


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('welcome')
