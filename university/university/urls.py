from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from library import views

router = routers.DefaultRouter()
router.register(r'genres', views.GenreViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'books-list', views.BookListViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
