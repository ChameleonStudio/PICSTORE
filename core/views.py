from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, FormView, CreateView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Category, Picture, Tag, SuperCategory, Cart
from .forms import RegistrationForm, LoginForm


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


CATEGORY_COUNT = 5
PER_PAGE = 20


class HomeView(TemplateView):
    template_name = "home.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tag = ""
        self.category = None
        self.page = 1
        self.tags = None

    def dispatch(self, request, *args, **kwargs):
        self.category = request.GET.get("category", None)
        self.tags = request.GET.get("search")
        if self.tags:
            self.tags = self.tags.split()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["super_categories"] = SuperCategory.objects.all()
        context["category"] = self.category
        tags = "[{}]".format(", ".join(list(map(lambda x: "'" + x.name + "'", Tag.objects.all()))))
        pictures = Picture.objects
        if self.category:
            pictures = pictures.filter(category__super_category__name=self.category)
        if tags:
            pictures = pictures.filter(tags=tags)
            pass
        context["pictures"] = pictures.all()
        context["all_tags"] = tags
        return context


class PictureDetailView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["picture"] = Picture.objects.get(pk=kwargs["pk"])
        context["tags"] = list(context["picture"].tags.all())
        # TODO: find similar
        context["similar_pictures"] = Picture.objects.all().exclude(pk=kwargs["pk"])[:4]  # .exclude(pk__in_)
        return context


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "home"

    def form_valid(self, form):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        else:
            return super().form_invalid(form)
        return super().form_valid(form)


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = RegistrationForm
    success_url = "login"

    def form_valid(self, form):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        email = self.request.POST.get("email")
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect("home")


class CartView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pictures = Picture.objects.filter(
            pk__in=Cart.objects.filter(user=self.request.user, payed=False).values_list("picture_id", flat=True)
        )
        context["pictures"] = pictures.all()
        context["originals"] = list(map(lambda x: x.picture.url, context["pictures"]))
        context["total_price"] = pictures.aggregate(sum=Sum("price"))["sum"]
        return context


class HistoryView(TemplateView):
    template_name = "history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pictures = Picture.objects.filter(
            pk__in=Cart.objects.filter(user=self.request.user, payed=True).values_list("picture_id", flat=True)
        )
        context["pictures"] = pictures.all()
        return context


class UploadView(TemplateView):
    template_name = "upload.html"


class AddToCartView(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        picture_pk = request.data.get("picture_pk")
        # user_pk = request.data.get("user_pk")
        Cart.objects.create(user=request.user, picture=Picture.objects.get(pk=picture_pk))
        return Response()


class BuyCartView(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        Cart.objects.filter(user=request.user, payed=False).update(payed=True)
        return Response()
