from django.contrib import admin
from .models import ArticleModel
from .models import CategoryModel

# Register your models here.
admin.site.register(ArticleModel)
admin.site.register(CategoryModel)