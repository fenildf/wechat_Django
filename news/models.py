from django.db import models

# Create your models here.


class News(models.Model):

    title = models.CharField(max_length=100)
    news_url = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)
    views = models.PositiveIntegerField(default=0)

    def _str_(self):
        return self.title

