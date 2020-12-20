from django.urls import path

from mails.views import DeleteMailView, IsReadMailView, CreateMailView, YourMailsListView, \
    MailReadView, AnswerMailView, SuccessMailSend

urlpatterns = [
    path('inbox/', YourMailsListView.as_view(), name='mail inbox'),
    path('isread/<int:pk>', IsReadMailView.as_view(), name='mail read'),
    path('read/<int:pk>/', MailReadView.as_view(), name='read mail'),
    path('delete/<int:pk>/', DeleteMailView.as_view(), name='delete mail'),
    path('create/', CreateMailView.as_view(), name='send mail'),
    path('edit/<int:pk>', AnswerMailView.as_view(), name='edit mail'),
    path('success/', SuccessMailSend.as_view(), name='success mail send'),
]
