from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home$', views.HomeView.as_view(),  name='home'),
    url(r'^pictures$', views.PictureLoadingView.as_view(), name='pictures'),
    url(r'^picture/(?P<pk>\d+)$', views.PictureDetailView.as_view(), name='picture')
]
