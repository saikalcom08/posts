from django.contrib import admin
from .models import Post, HashTag, Image


admin.site.register(Post)
admin.site.register(HashTag)
admin.site.register(Image)
