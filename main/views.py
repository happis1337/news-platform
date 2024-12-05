from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import *

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        top5_categories = [
            Article.objects.filter(category__name='Jahon'),
            Article.objects.filter(category__name='Iqtisodiyot'),
            Article.objects.filter(category__name='Jamiyat'),
            Article.objects.filter(category__name='Sport'),
            Article.objects.filter(category__name='Fan-texnika'),
        ]
        context = {
            "top4_articles": Article.objects.filter(published=True).order_by('-views')[:4],
            'popular_news': Article.objects.filter(published=True).order_by('-views')[:6],
            "top9_articles": Article.objects.filter(published=True).order_by('-views')[:9],
            'lastest_articles': Article.objects.filter(published=True).order_by('-created_at')[:4],
            'top5_categories': top5_categories,
            'top5_category_names': ['Jahon', 'Iqtisodiyot','Jamiyat', 'Sport', 'Fan-texnika'],
            'categories': categories,
        }

        return render(request, 'index.html', context)
    def post(self, request):
        email = request.POST.get('email')
        if email is not None:
            NewsLetter.objects.create(email=email)
        return redirect('home')


class DetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        tags = Tag.objects.all()[:8]
        two_might_articles = Article.objects.filter(category=article.category).filter(published=True).order_by('-created_at')[:2]
        popular_articles = Article.objects.filter(published=True).order_by('-views')[:4]
        context = {
            "article": article,
            'two_might_articles': two_might_articles,
            'popular_articles': popular_articles,
            'categories': Category.objects.all(),
            'tags': tags,
        }
        return render(request, 'detail-page.html', context)

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        if full_name and email and text:
            Comment.objects.create(full_name=full_name, email=email, text=text, article=article)
            return redirect('detail', slug=article.slug)


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Contact.objects.create(name=name, email=email, phone_number=phone, message=message, subject=subject,)
            return redirect('home')
        else:
            return render(request, 'contact.html', {'error': 'All fields are required'})


class AllArticlesView(View):
    def get(self, request):
        articles = Article.objects.filter(published=True).order_by('-created_at')
        context = {
            "articles": articles,
        }
        return render(request, 'all_articles.html', context)