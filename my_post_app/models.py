from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_image')

    def __str__(self):
        return f'{self.image.url}'


class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    hashtag = models.ManyToManyField('HashTag', related_name='hash_post')

    def __str__(self):
        return self.name

class HashTag(models.Model):
    hash = models.CharField(max_length=250)


    def __str__(self):
        return f'{self.hash}'



