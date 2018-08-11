from django.shortcuts import render
from facebook.models import Article, Comment

# Create your views here.
def play(request):
    return render(request, 'play.html')


def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles': articles})


def detail_feed(request, number):
    article = Article.objects.get(pk=number)

    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST["nickname"],
            text=request.POST["reply"],
            password=request.POST["password"]
        )

    return render(request, 'detail_feed.html', {'feed': article})


def new_feed(request):

    if request.method == 'POST':
        content = request.POST['content'] + ' 추신'
        Article.objects.create(
            author=request.POST['author'],
            password=request.POST['password'],
            title=request.POST['title'],
            text=content
        )

    return render(request, 'new_feed.html')


def edit_feed(request, number):
    article = Article.objects.get(pk=number)

    if request.method == 'POST':
        article.author = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()

    return render(request, 'edit_feed.html', {'feed': article})


def remove_feed(request, number):
    article = Article.objects.get(pk=number)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()

    return render(request, 'remove_feed.html', {'feed': article})
