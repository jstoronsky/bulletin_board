from rest_framework import serializers
from bulletin_board.models import Ad, Comment


class CommentsSerializer(serializers.ModelSerializer):
    """
    сериализатор для комментариев
    """

    class Meta:
        model = Comment
        fields = '__all__'


class CommentsCreateSerializer(serializers.ModelSerializer):
    """
    сериализатор для создания комментариев
    """

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'ad', 'author', 'created_at')
        read_only_fields = ('ad', 'author')


class CommentsUpdateSerializer(serializers.ModelSerializer):
    """
    сериализатор для обновления комментариев
    """

    class Meta:
        model = Comment
        fields = ('pk', 'text')


class AdCreateSerializer(serializers.ModelSerializer):
    """
    сериализатор для создания объявлений
    """

    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'description', 'author', 'created_at')
        read_only_fields = ('author', )


class AdUpdateSerializer(serializers.ModelSerializer):
    """
    сериализатор для обновления объявлений
    """
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'description')


class AdSerializer(serializers.ModelSerializer):
    """
    сериализатор для объявлений
    """
    comments = CommentsSerializer(source='comment_set', many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'description', 'author', 'created_at', 'last_modified', 'comments')
