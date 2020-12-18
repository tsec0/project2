from django.urls import path

from mails.views import DeleteMailView, IsReadMailView, CreateMailView, YourMailsListView, \
    MailReadView, UpdateMailView, CreateOrderView

urlpatterns = [
    path('inbox/', YourMailsListView.as_view(), name='mail inbox'),
    path('isread/<int:pk>', IsReadMailView.as_view(), name='mail read'),
    path('read/<int:pk>/', MailReadView.as_view(), name='read mail'),
    path('delete/<int:pk>/', DeleteMailView.as_view(), name='delete mail'),
    path('create/', CreateMailView.as_view(), name='send mail'),
    path('order/', CreateOrderView.as_view(), name='send order'),
    path('edit/<int:pk>', UpdateMailView.as_view(), name='edit mail'),
]
