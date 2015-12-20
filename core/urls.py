from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home$', views.HomeView.as_view(),  name='home'),
    url(r'^picture/(?P<pk>\d+)$', views.PictureDetailView.as_view(), name='picture'),
    url(r'^cart$', views.CartView.as_view(), name='cart'),
    url(r'^upload', views.UploadView.as_view(), name='upload'),
    url(r'^history', views.HistoryView.as_view(), name='history'),
    url(r'^login', views.LoginView.as_view(), name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^signup', views.SignUpView.as_view(), name='signup'),
    url(r'^add_to_cart', views.AddToCartView.as_view(), name='add_to_cart'),
    url(r'^buy', views.BuyCartView.as_view(), name='buy'),
    url(r'^toggle_like', views.ToggleLike.as_view(), name='toggle_like'),
]
