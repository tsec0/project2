from django.urls import path

from userfeedback.views import UserFeedBackListView, CreateUserFeedBackView

urlpatterns = [
    path('', UserFeedBackListView.as_view(), name='list feedbacks'),
    path('create/', CreateUserFeedBackView.as_view(), name='create feedback'),
]
