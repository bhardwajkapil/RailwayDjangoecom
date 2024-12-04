from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<int:pk>',views.product,name="product"),
    path('search_product/',views.search_product,name="search_product"),
    path('register/',views.register,name="register"),
    path('login/',views.login_user,name="login"),
    path('logout_user/',views.logout_user,name="logout"),
    path('update_user/',views.update_user,name="update_user"),
]