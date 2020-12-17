from django.urls import path

from toys.views import ToysDetailsView, ToysListView, LikeToysView, CommentToysView

urlpatterns = [
    path('', ToysListView.as_view(), name='list toys'),
    path('detail/<int:pk>/', ToysDetailsView.as_view(), name='toy details'),
    path('comment/<int:pk>/', CommentToysView.as_view(), name='comment toy'),
    path('like/<int:pk>/', LikeToysView.as_view(), name='like toy'),
]
