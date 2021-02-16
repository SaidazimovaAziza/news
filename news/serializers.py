from typing import Tuple
from django.utils.timezone import get_current_timezone
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import Author, News


class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model= Author
        fields: Tuple= ('author',)


class NewsSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(
        required=False, allow_null=True
    )

    class Meta:
        model = News
        fields: Tuple = (
            'text', 'author_id'
        )

    def validate(self, attrs):
        attrs['author_id'] = self.context.get('request').user.author.pk
        return attrs