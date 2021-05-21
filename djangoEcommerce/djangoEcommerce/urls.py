"""djangoEcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from core import views
from django.conf.urls.static import static
from . import settings
from djangoEcommerce import adminViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/', views.adminLogin, name="admin_login"),
    path('demo/', views.demoPage),
    path('demopage/', views.demoPageTemplate),
    path('admin_login_process/', views.admin_login_process, name="admin_login_process"),
    path('admin_logout_process/', views.admin_logout_process,
         name="admin_logout_process"),
    path('admin_home', adminViews.admin_home, name="admin_home"),
    path('category_list', adminViews.categoriesListView.as_view(), name="category_list"),
    path('category_create', adminViews.categoriesCreateView.as_view(),
         name="category_create"),
    path('category_update/<slug:pk>', adminViews.categoriesUpdateView.as_view(), name="category_update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



