from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from bulletin_board.serializers import (AdCreateSerializer, AdSerializer, AdUpdateSerializer,
                                        CommentsSerializer, CommentsCreateSerializer, CommentsUpdateSerializer)
from bulletin_board.models import Ad, Comment
from bulletin_board.permission import IsAdmin, IsOwner
from rest_framework import filters
from bulletin_board.paginators import AdsPaginator
# Create your views here.


class AdViewSet(viewsets.ModelViewSet):
    """
    вьюсеты для объявления, переопределены методы get_serializer_class, get_permissions и perform_create
    """
    queryset = Ad.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    pagination_class = AdsPaginator

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'destroy']:
            return AdSerializer

        elif self.action == 'create':
            return AdCreateSerializer

        elif self.action in ['update', 'partial_update']:
            return AdUpdateSerializer

    # def get_permissions(self):
    #     if self.action in ['create', 'retrieve']:
    #         self.permission_classes = [IsAuthenticated]
    #     elif self.action in ['update', 'partial_update', 'destroy']:
    #         self.permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
    #
    #     return super(AdViewSet, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MyAdsListAPIView(generics.ListAPIView):
    """
    эндпоинт для вывода своих объявлений
    """
    serializer_class = AdSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        author = self.request.user
        queryset = Ad.objects.filter(author=author)
        return queryset


class CommentsListAPIView(generics.ListAPIView):
    """
    эндпоинт для вывода списка комментариев для конкретного объявления
    """
    serializer_class = CommentsSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.filter(ad=self.kwargs['ad_pk'])
        return queryset


class CommentsRetrieveAPIView(generics.RetrieveAPIView):
    """
    эндпоинт для вывода комментария конкретного объявления
    """
    serializer_class = CommentsSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.filter(ad=self.kwargs['ad_pk'])
        return queryset


class CommentsCreateAPIView(generics.CreateAPIView):
    """
    эндпоинт для создания комментария к конкретному объявлению
    """
    serializer_class = CommentsCreateSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        ad_id = self.kwargs['ad_pk']
        ad = Ad.objects.get(pk=ad_id)
        serializer.save(ad=ad, author=self.request.user)


class CommentsUpdateAPIView(generics.UpdateAPIView):
    """
    эндпоинт для обновления комментария
    """
    serializer_class = CommentsUpdateSerializer
    # permission_classes = [IsAuthenticated, IsOwner | IsAdmin]

    def get_queryset(self):
        queryset = Comment.objects.filter(ad=self.kwargs['ad_pk'])
        return queryset


class CommentsDestroyAPIView(generics.DestroyAPIView):
    """
    эндпоинт для удаления комментария
    """
    # permission_classes = [IsAuthenticated, IsOwner | IsAdmin]

    def get_queryset(self):
        queryset = Comment.objects.filter(ad=self.kwargs['ad_pk'])
        return queryset
