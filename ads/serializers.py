from rest_framework.serializers import ModelSerializer

from ads.models import Ads, Comment


class AdsSerializer(ModelSerializer):
    class Meta:
        model = Ads
        exclude = ('author',)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('author', 'ad')
