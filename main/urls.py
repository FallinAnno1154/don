from django.contrib import admin
from django.urls import path, include
from main import views


from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),# главная страница
    path('blogs/', views.blogs, name='blogs'),#Блоги
    path('blogs/<int:blog_id>', views.blog, name='blog'),#Блог
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
