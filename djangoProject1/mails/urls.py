from django.urls import path

from mails.views import DeleteMailView, IsReadPetView, CreateMailView, YourMailsListView, \
    MailReadView, UpdateMailView

urlpatterns = [
    path('inbox/', YourMailsListView.as_view(), name='mail inbox'),
    path('isread/<int:pk>', IsReadPetView.as_view(), name='mail read'),
    path('read/<int:pk>/', MailReadView.as_view(), name='read mail'),
    path('delete/<int:pk>/', DeleteMailView.as_view(), name='delete mail'),
    path('create/', CreateMailView.as_view(), name='send mail'),
    path('edit/<int:pk>', UpdateMailView.as_view(), name='edit mail'),
]
