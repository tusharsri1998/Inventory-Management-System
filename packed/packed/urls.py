"""packed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.conf.urls import include
from calculate import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('packaging/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('packaging/after_login',views.after_login,name='after_login'),
    path('packaging/data_test',views.data_test,name='data_test'),
    path('packaging/new_project',views.new_project,name='new_project'),
    path('packaging/add_project',views.add_project,name='add_project'),
]
