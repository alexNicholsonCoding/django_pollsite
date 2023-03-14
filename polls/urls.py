from django.urls import include, path
from django.contrib import admin

from . import views


app_name = 'polls'

from polls import urls

urlpatterns = [
    path("", include(urls)),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path("", include(urls)),
]

