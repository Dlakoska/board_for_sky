from django.urls import path
from ads.apps import AdsConfig
from ads.views import AdsCreateAPIView, AdsListAPIView, AdsDeleteAPIView, AdsDetailAPIView, AdsUpdateAPIView, \
    CommentCreateAPIView, CommentListAPIView, CommentDetailUpdateDeliteAPIView

app_name = AdsConfig.name

urlpatterns = [
    path('create/', AdsCreateAPIView.as_view(), name='ads-create'),
    path('list/', AdsListAPIView.as_view(), name='ads-list'),
    path('update/<int:pk>/', AdsUpdateAPIView.as_view(), name='ads-update'),
    path('delete/<int:pk>/', AdsDeleteAPIView.as_view(), name='ads-delete'),
    path('detail/<int:pk>/', AdsDetailAPIView.as_view(), name='ads-detail'),
    path('<int:ad_pk>/comment_create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('<int:ad_pk>/comment_list/', CommentListAPIView.as_view(), name='comment-create'),
    path('<int:ad_pk>/operations/<int:pk>/', CommentDetailUpdateDeliteAPIView.as_view(), name='comment_operations')

]
