from django.shortcuts import render, redirect
from .models import ArticleModel, CategoryModel

# Create your views here.
# GET 요청으로 들어오면 form 태그 있는 html을 보여주고
# POST 요청으로 들어오면 request.POST 변수들을 받아서 글을 생성함
# GET 부분
# 새 글을 쓸 때 현재 CategoryModel에 존재하는 것만 사용자가 선택을 할 수 있어야 함 -> 모델 임포트하고, 카테고리모델 전부를 가져옴
# -> 가져온 카테고리 역시 렌더해서 보여줌  (왼쪽의 'categories'는 프론트에서 쓰는 변수명)
# POST 부분
# title, category1, content 변수에 input창에 적은 내용을 가져옴 ( 'title','category','content'는 프론트 html 태그 네임 )
# article = ArticleModel.objects.create(title=title, content=content, category=category1) 라고 쓰면 작동하지 않음
# 왜? category1은 외래키로 참조했기 때문에 글도 아니고, 숫자도 아니고, 리스트도 아닌 CategoryModel 오브젝트 그 자체!
# category2 로 모델에서 정한 필드명으로 받아 줘야 가져올 수 있음
# url을 'detail/' 로 쓰는 것과 'detail'로 쓰는 건 다른 것
# article.pk -> 'detail'과 함께 할당된 pk번호로 리다이렉트 해줌 (django는 자동으로 PK라는 필드를 만들어 줌(첫 게시글이면 1번 detail페이지로 가))

def new_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', None)
        category1 = request.POST.get('category', None)
        content = request.POST.get('content', None)

        category2 = CategoryModel.objects.get(category_name=category1)
        article = ArticleModel.objects.create(title=title, content=content, category=category2)
        return redirect('detail', article.pk)

    elif request.method == 'GET':
        categories = CategoryModel.objects.all()
        return render(request, 'new.html', {'categories': categories})


# 전체 카테고리를 다 보여주면 됨  ( 심화!!!! 카테고리 이름, 해당 카테고리 글 개수 넘겨줌 )
# 서버쪽에서 미리 개수를 뽑아서 {movie:2 , drama:1} 딕셔너리 형태로 보내주는게 좋음
def category_view(request):
    categories = CategoryModel.objects.all()
    infos = {}
    for category in categories:
        ArticleModel.objects.filter(category=category).count()
    return render(request, 'category.html', {'infos': infos})

# article은 그 카테고리에 맞는 article만 보여줘야 함
# 127.0.0.1/movie   -> name='movie' 라는 str으로 들어온 것
# articles = ArticleModel.objects.filter(category=name) 이라 쓰면 안됨! 외래키 참조하니까 위에 한줄 추가하고 그걸 받아야 함
def article_view(request, name):
    category = CategoryModel.objects.get(category_name=name)
    articles = ArticleModel.objects.filter(category=category)
    return render(request, 'article.html', {'article': articles})


# 127.0.0.1/detail/1  -> pk = 1 이라는 int
def detail_view(request, pk):
    article = ArticleModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'article': article})
