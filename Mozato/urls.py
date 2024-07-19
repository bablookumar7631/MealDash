from django.contrib import admin
from django.urls import path
from mozato_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage, name='index'),
    path('category/<str:cat_name>', views.categoryPage, name='category'),
    path('popup_add_cart/<food_id>', views.popupPage, name='popup_add_cart'),
    path('search', views.searchPage, name='search'),
    path('checkout', views.checkoutPage, name='checkout'),
    path('loadmore', views.loadmorePage, name='loadmore'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('signup', views.signupPage, name='signup'),
    path('addToCart', views.addToCartPage, name='addToCart'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
