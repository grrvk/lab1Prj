"""lab1Prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from lab1p import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('lab1p/', include('lab1p.urls')),
    path('admin/', admin.site.urls),

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)

# urlpatterns += staticfiles_urlpatterns()     --- if all works - delete
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



