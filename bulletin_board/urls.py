from bulletin_board.apps import BulletinBoardConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
# from bulletin_board.views import AdCreateAPIView, AdListAPIView
from bulletin_board.views import (AdViewSet, MyAdsListAPIView, CommentsListAPIView, CommentsRetrieveAPIView,
                                  CommentsCreateAPIView, CommentsUpdateAPIView, CommentsDestroyAPIView)


app_name = BulletinBoardConfig.name
router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ads')

urlpatterns = [
    path('ads/me/', MyAdsListAPIView.as_view(), name='my_ads'),
    path('ads/<int:ad_pk>/comments/', CommentsListAPIView.as_view(), name='comments'),
    path('ads/<int:ad_pk>/comments/<int:pk>/', CommentsRetrieveAPIView.as_view(), name='comment'),
    path('ads/<int:ad_pk>/comments/create/', CommentsCreateAPIView.as_view(), name='create_comment'),
    path('ads/<int:ad_pk>/comments/<int:pk>/upd/', CommentsUpdateAPIView.as_view(), name='comment_update'),
    path('ads/<int:ad_pk>/comments/<int:pk>/delete/', CommentsDestroyAPIView.as_view(), name='comment_delete')

] + router.urls
