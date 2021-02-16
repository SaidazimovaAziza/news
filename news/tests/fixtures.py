from django.contrib.auth.models import User
from django.test import Client
from pytest import fixture
from rest_framework.authtoken.models import Token

from news.models import Author


@fixture
def user(db):
    return User.objects.create_user(
        username='test', email='testchoco@chocofood.kz',
        password='test',
    )


@fixture
def author(db, user):
    return Author.objects.create(
        user=user,
        full_name='Test Tests',
    )


@fixture
def authenticated_author_client(
        author: Author, client: Client
) -> Client:
    token = Token.objects.get_or_create(user=author.user)[0].key
    client.defaults['HTTP_AUTHORIZATION'] = f'Token {token}'
    return client
