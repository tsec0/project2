from django.urls import path

from pets.views import PetDetailsView, UpdatePetView, LikePetView, \
    SellPetView, CommentPetView, DeletePetView, CreatePetView, \
    PetsListView, YourPetsListView, MailToPetOwnerView, Success

urlpatterns = [
    path('', PetsListView.as_view(), name='list pets'),
    path('yourpets/', YourPetsListView.as_view(), name='user pets'),
    path('detail/<int:pk>/', PetDetailsView.as_view(), name='pet details'),
    path('comment/<int:pk>/', CommentPetView.as_view(), name='comment pet'),
    path('like/<int:pk>/', LikePetView.as_view(), name='like pet'),
    path('sell/<int:pk>/', SellPetView.as_view(), name='sell pet'),
    path('edit/<int:pk>/', UpdatePetView.as_view(), name='edit pet'),
    path('delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),
    path('create/', CreatePetView.as_view(), name='create pet'),
    path('sendmail/<int:pk>', MailToPetOwnerView.as_view(), name='send mail to owner'),
    path('success/', Success.as_view(), name='success'),
]
