
from django.urls import path

from connexto.common import views


urlpatterns = (
    path('', views.HomePageView.as_view(), name='home page'),
    path('like/<int:photo_id>/', views.likes_functionality, name='like'),
    path('share/<int:photo_id>/', views.share_functionality, name='share'),
    path('comment/<int:photo_id>/', views.comment_functionality, name='comment')
)