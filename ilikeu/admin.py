from django.contrib import admin
from .models import Post
from .models import Man
from .models import Woman
# Register your models here.

admin.site.register(Post)
admin.site.register(Man)
admin.site.register(Woman)