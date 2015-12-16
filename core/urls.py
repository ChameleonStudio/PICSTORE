from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home$', views.HomeView.as_view(),  name='home'),
    url(r'^picture/(?P<pk>\d+)$', views.PictureDetailView.as_view(), name='picture'),
    url(r'^cart$', views.CartView.as_view(), name='cart'),
    url(r'^login', views.LoginView.as_view(), name='login'),
]
