from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from mails.forms import OrderForm
from mails.models import Mail
from toys.models import Toys, Liked
from toys.forms import CommentsOfToysForm


class ToysListView(views.ListView):
    model = Toys
    template_name = 'toys/toys_list.html'
    context_object_name = 'toys'


class ToysDetailsView(views.DetailView):
    model = Toys
    template_name = 'toys/toys_detail.html'
    context_object_name = 'toy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        toy = context[self.context_object_name]
        context['form'] = CommentsOfToysForm()
        context['has_liked_a_lot'] = toy.liked_set.filter(user_id=self.request.user.userprofile.id).exists()
        context['comments'] = list(toy.commentsoftoys_set.all())
        return context


class LikeToysView(views.View):

    def get(self, request, **kwargs):
        user_profile = request.user.userprofile
        toy = Toys.objects.get(pk=kwargs['pk'])

        liked = toy.liked_set.filter(user_id=user_profile.id).first()
        if liked:
            liked.delete()
        else:
            liked = Liked(
                user=user_profile,
                toy=toy,
                liked='liked'
            )
            liked.save()
        return redirect('toy details', toy.pk)  # toys list


class CommentToysView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = CommentsOfToysForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user.userprofile
        comment.toy = Toys.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('toy details', self.kwargs['pk'])
