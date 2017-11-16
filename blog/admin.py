from django.contrib import admin
from .models import Post #앞에서 만든 Post모델을 가져온다.
# Register your models here.
admin.site.register(Post)