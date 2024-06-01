# myapp/urls.py

from django.urls import path
from .views import scrape_page

urlpatterns = [
    path('scrape/', scrape_page, name='scrape_page'),
]
