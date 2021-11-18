from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_allposts, name="all_posts"),
    path('detail/<int:pk>/', views.detail_post, name='detail')
]