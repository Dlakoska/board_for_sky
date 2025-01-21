from django.db import models

from users.models import User


class Ads(models.Model):
    title = models.CharField(max_length=30, verbose_name='название товара')
    price = models.PositiveIntegerField(verbose_name='цена товара')
    description = models.TextField(verbose_name='описание товара')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор объявление')
    created_at = models.DateTimeField(auto_now=True, verbose_name='время и дата создания объявления')

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор комментария')
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE, verbose_name='объявление, под которым оставлен отзыв')
    created_at = models.DateTimeField(auto_now=True, verbose_name='время и дата создания отзыва')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author.email} - {self.ad.title}'
