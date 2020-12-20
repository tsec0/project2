from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from food.models import Food
from food.forms import CommentsOfFoodForm
from mails.forms import OrderForm
from mails.models import Mail


class FoodListView(views.ListView):
    model = Food
    template_name = 'food/food_list.html'
    context_object_name = 'food'


class FoodDetailsView(views.DetailView):
    model = Food
    template_name = 'food/food_detail.html'
    context_object_name = 'foo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        food = context[self.context_object_name]
        context['form'] = CommentsOfFoodForm()
        context['comments'] = list(food.commentsoffood_set.all())
        return context


class CommentFoodView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = CommentsOfFoodForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user.userprofile
        comment.food = Food.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('food details', self.kwargs['pk'])


class CreateOrderFoodView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'mails/order_create.html'
    model = Mail
    form_class = OrderForm

    def get_object(self, query=None):
        pk = self.kwargs.get('pk', None)
        food = self.request.food if pk is None else Food.objects.get(pk=pk)
        return food

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
