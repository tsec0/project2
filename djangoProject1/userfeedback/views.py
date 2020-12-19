from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.
from userfeedback.forms import UserFeedBackForm
from userfeedback.models import UserFeedBack
from django.contrib.auth import mixins as auth_mixins


class UserFeedBackListView(views.ListView):
    model = UserFeedBack
    template_name = 'feedback/feedback_list.html'
    context_object_name = 'feedbacks'


class CreateUserFeedBackView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'feedback/feedback_create.html'
    model = UserFeedBack
    form_class = UserFeedBackForm

    def get_success_url(self):
        url = reverse_lazy('list feedbacks')
        return url

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.publisher = self.request.user.userprofile
        feedback.user_id = self.request.user.userprofile.id
        feedback.save()
        return super().form_valid(form)
