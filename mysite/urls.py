"""mysite URL Configuration

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
from django.urls import include, path
from django.shortcuts import redirect
from django.views.generic.base import RedirectView



#points the root URLconf at the polls.urls module

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('go-to-django/', RedirectView.as_view(url='')),
    path('', HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]




def fixed_polls(request):
    ...
    return redirect('polls/')

def redirect_view(request):
  return HttpResponseRedirect('polls/')