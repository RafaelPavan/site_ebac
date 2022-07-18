from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'), # views do blog
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),

]