"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from employee import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('command', views.command),
    path('showCmd',views.showCmd),
    path('editCmd/<int:id>', views.editCmd),
    path('updateCmd/<int:id>', views.updateCmd),
    path('deleteCmd/<int:id>', views.destroyCmd),
    path('bowlweight', views.bowlweight),
    path('showBowlWght',views.showBowlWght),
    path('editBowlWght/<int:id>', views.editBowlWght),
    path('updateBowlWght/<int:id>', views.updateBowlWght),
    path('deleteBowlWght/<int:id>', views.destroyBowlWght),
    path('showError',views.showError),
]
