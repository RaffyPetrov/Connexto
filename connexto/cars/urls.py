from django.urls import path, include

from connexto.cars import views

urlpatterns = [
    path('add/', views.CarAddPage.as_view(), name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.CarDetailsPage.as_view(), name='pet-details'),
        path('edit/', views.CarEditPage.as_view(), name='edit-pet'),
        path('delete/', views.CarDeletePage.as_view(), name='delete-pet'),
    ]))
]
