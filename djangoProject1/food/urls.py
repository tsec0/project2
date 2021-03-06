from django.urls import path

from food.views import FoodDetailsView, FoodListView, CommentFoodView, CreateOrderFoodView

urlpatterns = [
    path('', FoodListView.as_view(), name='list food'),
    path('detail/<int:pk>/', FoodDetailsView.as_view(), name='food details'),
    path('comment/<int:pk>/', CommentFoodView.as_view(), name='comment food'),
    path('order/<int:pk>', CreateOrderFoodView.as_view(), name='send food order'),
]
