"""EdInHi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from EdInHi import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^authentification/', include('registration.urls')),
    url(r'^skills/', include('skill.urls')),
    url(r'^', include('main_app.urls')),
    url(r'^profile/', include('profile.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^companies/', include('companies_app.urls')),
    url(r'^task/', include('tasks.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^spec/', include('specialization.urls')),
    url(r'^feedback/', include('feedback.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
