from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Author(models.Model):
    user = models.OneToOneField(
        get_user_model(), verbose_name='Пользователь',
        on_delete=models.SET_NULL, null=True, related_name='author',
    )
    full_name = models.CharField(
        help_text=_('full_name'), verbose_name=_('full_name'),
        max_length=255, blank=True, default='',
    )

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('author')
        db_table = 'news.authors'


class News(models.Model):
    author = models.ForeignKey(
        to='news.Author', verbose_name=_('author'), null=True,
        on_delete=models.SET_NULL, related_name='news',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text=_('created_at'),
        verbose_name=_('created_at'),
    )
    text = models.CharField(
        help_text=_('text'), verbose_name=_('text'),
        max_length=512, blank=True,
    )

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
