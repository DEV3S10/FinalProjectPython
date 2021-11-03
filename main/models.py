from django.db import models

# Create your models here.


class New(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField()
    short_description = models.TextField()
    full_description = models.TextField()
    image = models.ImageField(upload_to='new')
    link = models.URLField()
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ImageNews(models.Model):
    image = models.ImageField(upload_to='news')
    news = models.ForeignKey(New, on_delete=models.CASCADE,
                             related_name='images')


LAW_TYPE = (
    (1, 'Действуйщее законодательство'),
    (2, 'Проекты нормативных актов'),
    (3, 'Международные документы'),
)


class Law(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = models.TextField()
    publication_date = models.DateTimeField()
    file = models.FileField(upload_to='files')
    type = models.IntegerField(choices=LAW_TYPE, default=1)

    def __str__(self):
        return self.title


PUBLICATION_TYPE = (
    (1, 'Публикации ICNL'),
    (2, 'Другие Публикации'),
)


class Publication(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    full_description = models.TextField()
    publication_date = models.DateTimeField()
    file = models.FileField(upload_to='files')
    type = models.IntegerField(choices=PUBLICATION_TYPE,
                               default=1)

    def __str__(self):
        return self.title
