from typing import Tuple
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from .models import News
from .serializers import NewsSerializer


class NewViewSet(ModelViewSet):
    authentication_classes: Tuple = (TokenAuthentication,)
    http_method_names = ('post', 'get', 'put', 'delete')
    serializer_class = NewsSerializer
    queryset = News.objects.order_by('-id')
    permission_classes = (IsAuthenticated,)
