import os
import tempfile

from django.db import models
from django.core.files.storage import FileSystemStorage

temp_storage = FileSystemStorage(tempfile.gettempdir())

ARTICLE_STATUS = (
    (1, 'Draft'),
    (2, 'Pending'),
    (3, 'Live'),
)

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    url = models.CharField('The URL', max_length=40)

    def __unicode__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=50, help_text='Use both first and last names.')

    def __unicode__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(max_length=50)
    slug = models.SlugField()
    pub_date = models.DateField()
    created = models.DateField(editable=False)
    writer = models.ForeignKey(Writer)
    article = models.TextField()
    categories = models.ManyToManyField(Category, blank=True)
    status = models.IntegerField(choices=ARTICLE_STATUS, blank=True, null=True)

    def save(self):
        import datetime
        if not self.id:
            self.created = datetime.date.today()
        return super(Article, self).save()

    def __unicode__(self):
        return self.headline

class ImprovedArticle(models.Model):
    article = models.OneToOneField(Article)

class ImprovedArticleWithParentLink(models.Model):
    article = models.OneToOneField(Article, parent_link=True)

class PhoneNumber(models.Model):
    phone = models.PhoneNumberField()
    description = models.CharField(max_length=20)

    def __unicode__(self):
        return self.phone

class TextFile(models.Model):
    description = models.CharField(max_length=20)
    file = models.FileField(storage=temp_storage, upload_to='tests')

    def __unicode__(self):
        return self.description

class ImageFile(models.Model):
    description = models.CharField(max_length=20)
    try:
        # If PIL is available, try testing PIL.
        # Checking for the existence of Image is enough for CPython, but
        # for PyPy, you need to check for the underlying modules
        # If PIL is not available, this test is equivalent to TextFile above.
        from PIL import Image, _imaging
        image = models.ImageField(storage=temp_storage, upload_to='tests')
    except ImportError:
        image = models.FileField(storage=temp_storage, upload_to='tests')

    def __unicode__(self):
        return self.description
