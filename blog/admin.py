from django.contrib import admin
from .models import Article, Category
# .models 는 같은 경로에 있는 models.py에서 가져올것임

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)