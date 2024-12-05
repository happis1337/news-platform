from random import choice
import requests
from datetime import datetime


from .models import *


def base_context(request):
    galleries = Gallary.objects.all()[:6]
    categories = Category.objects.all()
    last2_articles = Article.objects.filter(published=True).order_by('-created_at')[:2]
    base_top5_articles = Article.objects.filter(published=True).order_by('-views')[:5]
    base_top5_random_articles = choice(base_top5_articles)

    hafta_kunlari = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
    hafta_kuni = hafta_kunlari[datetime.now().weekday()]
    weather_data = requests.get('https://api.weatherapi.com/v1/current.json?q=Fergana&key=17a6ee6a36bf40a2b4d122900242911').json()
    temperature = {
        'temp_c': weather_data.get('current').get('temp_c'),
        'location': weather_data.get('location').get('name'),
        'icon': weather_data.get('current').get('condition').get('icon'),
    }

    context = {
        'base_top5_random_articles': base_top5_random_articles,
        'categories': categories,
        'weekday': hafta_kuni,
        'today': str(datetime.today().strftime('%d-%m-%Y')).replace('-', ''),
        'temperature': temperature,
        'last2_articles': last2_articles,
        'galleries': galleries,
    }
    return context