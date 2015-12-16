from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.views.generic import TemplateView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Category, Picture, Tag, SuperCategory


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

    def dispatch(self, request, *args, **kwargs):
        self.category = request.GET.get("category", None)
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
            # pictures = pictures.filter(tags=tags)
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


class LoginView(TemplateView):
    template_name = "login.html"


class CartView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pictures = Picture.objects
        context["pictures"] = pictures.all()
        context["total_price"] = pictures.aggregate(sum=Sum("price"))["sum"]
        return context
