#user/models.py
from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    class Meta:
        db_table = "category"

    category_name = models.CharField(max_length=256, null=False)
    category_description = models.TextField()


# ArticleModel을 밑에 써야 하는 이유 : CategoryModel을 참조하기 때문
class ArticleModel(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=256, null=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)  # Category 없어지면 같이 삭제
    content = models.TextField()
