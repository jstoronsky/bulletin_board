from datetime import datetime

from django.db import models


# Create your models here.
class Ad(models.Model):
    """
    модель объявления
    """
    title = models.CharField(max_length=60, verbose_name='название')
    price = models.IntegerField(verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='ads/', verbose_name='аватар пользователя', null=True, blank=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего обновления',
                                         null=True, blank=True)

    def save(self, *args, **kwargs):
        self.last_modified = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'


class Comment(models.Model):
    """
    модель комментария
    """
    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='автор')
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE, verbose_name='объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
