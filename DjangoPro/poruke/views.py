from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Article
from .forms import ArticleForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Vezbe 13'})
    else:
        return redirect('poruke:articles')


@login_required
def articles(req):
    tmp = Article.objects.all()
    return render(req, 'articles.html', {'articles': tmp})


@login_required
def article(req, id):
    tmp = get_object_or_404(Article, id=id)
    return render(req, 'article.html', {'article': tmp, 'page_title': tmp.title})


@permission_required('poruke.change_article')
def edit(req, id):
    if req.method == 'POST':
        form = ArticleForm(req.POST)

        if form.is_valid():
            a = Article.objects.get(id=id)
            a.title = form.cleaned_data['title']
            a.content = form.cleaned_data['content']
            a.save()
            return redirect('poruke:articles')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Article.objects.get(id=id)
        form = ArticleForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('poruke.add_article')
def new(req):
    if req.method == 'POST':
        form = ArticleForm(req.POST)

        if form.is_valid():
            a = Article(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            a.save()
            return redirect('poruke:articles')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = ArticleForm()
        return render(req, 'new.html', {'form': form})
