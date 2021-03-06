from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/posts/{}'.format(self.slug)

    def get_edit_url(self):
        return f'/posts/{self.slug}/update'

    def get_delete_url(self):
        return '/posts/{}/delete'.format(self.slug)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    cellphone_num = models.IntegerField()

    def __str__(self):
        return self.user.username
