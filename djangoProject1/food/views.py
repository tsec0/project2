from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from food.models import Food
from food.forms import CommentsOfFoodForm


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
