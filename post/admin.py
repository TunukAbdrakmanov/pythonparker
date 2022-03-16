from django.contrib import admin

# Register your models here.
# здесь регистрируются можели для их оторб
from post.models import Post,Comment

admin.site.register(Post)
admin.site.register(Comment)