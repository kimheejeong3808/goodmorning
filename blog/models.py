#user/models.py
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.TextField()


# ArticleModel을 밑에 써야 하는 이유 : CategoryModel을 참조하기 때문?
class Article(models.Model):
    title = models.CharField(max_length=256, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Category 없어지면 같이 삭제
    content = models.TextField()
