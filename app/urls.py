from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),


    path('gender/<slug:gender_slug>', views.ShopView.as_view(), name='shop'),
    path('cate/<slug:category_slug>', views.SportShop, name='shops'),
    path('category/<slug:category_slug>/<slug:gender_slug>', views.SportView.as_view(), name='shot'),
    path('shop.html', views.AllShop, name='shopp'),
    path('cate/<slug:category_slugs>', views.LuxShop, name='luxshop'),
    path('category/<slug:category_slugs>/<slug:gender_slugs>', views.LuxView.as_view(), name='luxgen'),
    path('about.html', views.AboutView, name='about'),
    path('contact.html', views.ContactView, name='contact'),
    path('<int:pk>/', views.ShopSingle.as_view(), name='shop-single'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
