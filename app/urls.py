from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('',views.HomeView,name='home'),
    path('shop.html',views.ShopView,name='shop'),
    path('about.html',views.AboutView,name='shop'),
    path('contact.html',views.ContactView,name='shop'),
    path('shop-single.html',views.ShopSingleView,name='shop'),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)