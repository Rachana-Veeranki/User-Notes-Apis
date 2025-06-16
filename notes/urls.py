from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_view, login_view, NoteViewSet


router = DefaultRouter()
router.register('notes', NoteViewSet, basename='note')

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', include(router.urls)),
]

