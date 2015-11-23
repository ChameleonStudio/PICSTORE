from django.core.urlresolvers import reverse
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
        self.tag = request.GET.get("tag", "")
        self.page = request.GET.get("page", 1)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["pictures"] = Picture.objects.all()
        context["super_categories"] = SuperCategory.objects.all()
        context["all_tags"] = "[{}]".format(", ".join(list(map(lambda x: "'" + x.name + "'", Tag.objects.all()))))
        return context


class PictureLoadingView(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        tags = filter(None, request.data.get("tags", []))

        pictures = {
            "pictures": []
        }

        for i in list(Picture.objects.all()):
            pictures["pictures"].append(self._json_picture(i))

        return Response(pictures)

    def _json_picture(self, picture):
        return {
            "link": reverse("picture", kwargs={"pk": picture.pk}),
            "url": picture.thumbnail.url,
            "name": picture.name,
            "description": picture.short_description,
            "category": picture.category.name,
            "sale": picture.sale,
            "price": picture.price,
            "likes": picture.likes,
        }


class PictureDetailView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["picture"] = Picture.objects.get(pk=kwargs["pk"])
        context["tags"] = list(context["picture"].tags.all())
        # list(context["picture"].tags)
        # TODO: find similar
        context["similar_pictures"] = Picture.objects.all().exclude(pk=kwargs["pk"])[:3]
        return context
