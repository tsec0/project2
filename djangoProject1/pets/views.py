from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from core.clean_up import clean_up_files
from pets.comments_form import CommentForm
from pets.models import Pet, Like, Sell
from pets.forms import PetForm


class PetsListView(views.ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'


class YourPetsListView(views.ListView):
    model = Pet
    template_name = 'pets/pet_user.html'
    context_object_name = 'pets'

    def get_object(self, query=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.get_object().user
        context['pets'] = self.get_object().pet_set.all()
        return context


class PetDetailsView(views.DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context[self.context_object_name]
        context['form'] = CommentForm()
        context['can_edit'] = self.request.user == pet.user.user
        context['can_delete'] = self.request.user == pet.user.user
        context['can_like'] = self.request.user != pet.user.user
        context['has_liked'] = pet.like_set.filter(user_id=self.request.user.userprofile.id).exists()
        context['can_comment'] = self.request.user != pet.user.user
        context['can_edit'] = self.request.user == pet.user.user
        context['comments'] = list(pet.comment_set.all())
        context['can_sell'] = self.request.user == pet.user.user
        context['is_sold'] = pet.sell_set.filter(user_id=self.request.user.userprofile.id).exists()
        # context['can_send_message'] = self.request.user != pet.user.user
        return context


class LikePetView(views.View):

    def get(self, request, **kwargs):
        user_profile = request.user.userprofile
        pet = Pet.objects.get(pk=kwargs['pk'])

        like = pet.like_set.filter(user_id=user_profile.id).first()
        if like:
            like.delete()
        else:
            like = Like(
                user=user_profile,
                pet=pet,
                like='like'
            )
            like.save()
        return redirect('pet details', pet.id)


class SellPetView(views.View):

    def get(self, request, **kwargs):
        user_profile = request.user.userprofile
        pet = Pet.objects.get(pk=kwargs['pk'])

        sell = pet.sell_set.filter(user_id=user_profile.id).first()
        if sell:
            sell.delete()
        else:
            sell = Sell(
                user=user_profile,
                pet=pet,
                sell='sell'
            )
            sell.save()
        return redirect('pet details', pet.id)


class CommentPetView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user.userprofile
        comment.pet = Pet.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('pet details', self.kwargs['pk'])


class CreatePetView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'pets/pet_create.html'
    model = Pet
    form_class = PetForm

    def get_success_url(self):
        url = reverse_lazy('pet details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user.userprofile
        pet.user_id = self.request.user.userprofile.id
        pet.save()
        return super().form_valid(form)


class UpdatePetView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'pets/pet_edit.html'
    model = Pet
    form_class = PetForm

    def get_success_url(self):
        url = reverse_lazy('pet details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        # for cycle
        old_image = self.get_object().image
        old_image_one = self.get_object().image_one
        old_image_two = self.get_object().image_two
        old_image_three = self.get_object().image_three
        old_image_four = self.get_object().image_four
        old_image_five = self.get_object().image_five
        image_list = [old_image, old_image_one, old_image_two, old_image_three, old_image_four, old_image_five]
        for image in image_list:
            if image:
                clean_up_files(image.path)
        return super().form_valid(form)


class DeletePetView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Pet
    template_name = 'pets/pet_delete.html'
    success_url = reverse_lazy('list pets')

    def dispatch(self, request, *args, **kwargs):
        pet = self.get_object()
        if pet.user_id != request.user.userprofile.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
