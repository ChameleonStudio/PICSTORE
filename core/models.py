from django.db import models
from PIL import Image
import os

from online_store import settings
from tools.model_utils import humanize_verbose_names


@humanize_verbose_names
class SuperCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=511, null=True, blank=True)

    def __str__(self):
        return self.name


@humanize_verbose_names
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=511, null=True, blank=True)
    icon_class = models.CharField(max_length=100, default="", null=True, blank=True)
    super_category = models.ForeignKey(SuperCategory, null=True, blank=True)

    def display_icon(self):
        return '<span class="{}"></span>'.format(self.icon_class)
    display_icon.allow_tags = True

    def __str__(self):
        return self.name


@humanize_verbose_names
class Tag(models.Model):
    name = models.CharField(max_length=255, primary_key=True, db_index=True)

    def __str__(self):
        return self.name


@humanize_verbose_names
class Sale(models.Model):
    value = models.FloatField(default=1.0)
    description = models.CharField(max_length=511, null=True, blank=True)

    def __str__(self):
        return self.value


@humanize_verbose_names
class Picture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=511, null=True, blank=True)
    price = models.FloatField(default=0.0)
    tags = models.ManyToManyField(Tag)
    picture = models.ImageField(upload_to=settings.PICTURE_PATH)
    thumbnail = models.ImageField(upload_to=settings.THUMBNAIL_PATH)
    sale = models.ForeignKey(Sale, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)

    def display_thumbnail(self):
        return '<img width="200" src="{}">'.format(self.thumbnail.url)
    display_thumbnail.allow_tags = True

    def tag_list(self):
        return ", ".join(map(lambda x: "#" + x.name, self.tags.all()))

    def create_thumbnail(self):
        if not self.picture:
            return
        im = Image.open(self.picture.path)
        im.thumbnail(settings.THUMBNAIL_SIZE)
        file_name = os.path.basename(self.picture.path)
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, settings.THUMBNAIL_PATH)):
            os.makedirs(os.path.join(settings.MEDIA_ROOT, settings.THUMBNAIL_PATH))
        im.save(os.path.join(settings.MEDIA_ROOT, settings.THUMBNAIL_PATH, file_name), "JPEG")
        self.thumbnail = os.path.join(settings.THUMBNAIL_PATH, file_name)

    def save(self, *args, **kwargs):
        try:
            old_picture = Picture.objects.get(pk=self.pk)
            if old_picture.picture != self.picture:
                self.thumbnail = None
        except Picture.DoesNotExist:
            pass
        super().save(*args, **kwargs)
        if not self.thumbnail:
            self.create_thumbnail()
            self.save()

    def __str__(self):
        return self.name
