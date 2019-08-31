
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from blog.views.register import RegisterView
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import url
urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:home')),
    path('register/', RegisterView.as_view(), name='register'),
    path('contact/',TemplateView.as_view(template_name='blog/contact.html'), name='contact'),
    path('profile/',TemplateView.as_view(template_name='blog/profile.html'), name='profile'),
    path('', include('django.contrib.auth.urls')),
    path('', include('blog.urls'), name='blog'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)