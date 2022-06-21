from django.urls import path
from .views import WomanAPIView, DetailWoman


urlpatterns = [
    path('', WomanAPIView.as_view()),
    path('<int:pk>/', DetailWoman.as_view()),
]
