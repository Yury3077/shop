from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('cart/', CartView.as_view()),
    path('contact/', ContactView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('category/<str:category>', CategoryView.as_view(), name='category'),
    path('single_product/<int:product_id>', SingleProduct.as_view()),
    path('accounts/login/', LoginUserView.as_view(), name="login"),
    path(r'^accounts/register/$', RegisterUserView.as_view(), name="register"),
    path('accounts/logout/', LogoutUserView.as_view(), name="logout"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)