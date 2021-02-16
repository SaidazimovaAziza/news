from news.models import News


def test_create_201(
        db, user, authenticated_author_client, author
) -> None:

    responce = authenticated_author_client.post(
        path='/api/news/',
        data={
            'text': 'text',
            'author': author.pk,
        },
        content_type='application/json'
    )
    assert responce.status_code == 201


def test_get_200(
        db, user, authenticated_author_client, author
) -> None:
    News.objects.create(
        author = author,
        text='text',
        created_at='2020-02-01'
    )

    responce = authenticated_author_client.get(
        path='/api/news/',
    )
    assert responce.status_code == 200



def test_delete_203(
        db, user, authenticated_author_client, author
) -> None:
    new = News.objects.create(
        author=author,
        text='text',
        created_at='2020-02-01'
    )
    responce = authenticated_author_client.delete(
        path=f'/api/news/{News.objects.last().pk}/',
        data={
            'text': 'text 123',
        },
        content_type='application/json'
    )
    assert responce.status_code == 204


def test_put_200(
    db, user, authenticated_author_client, author
):
    new = News.objects.create(
        author=author,
        text='text',
        created_at='2020-02-01'
    )
    responce = authenticated_author_client.put(
        path=f'/api/news/{News.objects.last().pk}/',
        data={
            'text': 'changed text',
        },
        content_type='application/json'
    )
    assert responce.status_code == 200

