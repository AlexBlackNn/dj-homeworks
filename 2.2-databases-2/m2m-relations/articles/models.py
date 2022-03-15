from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']
    def __str__(self):
        return self.title


class Scope(models.Model):
    tag = models.TextField(verbose_name='tag', max_length=50)
    is_main = models.BooleanField()
    article = models.ManyToManyField(Article, related_name='scopes')

class ArticleScope(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='scopes1')
    scope = models.ForeignKey(
        Scope,
        on_delete=models.CASCADE,
        related_name='scopes1')