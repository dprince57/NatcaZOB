from django.db import models
from datetime import datetime
from django.db.models.fields.files import ImageField

# Create your models here.


class HAWCUser(models.Model):
    full_name = models.CharField(max_length=60)
    AREA_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('TMU', 'TMU'),
        ('Training', 'Training'),
        ('Other', 'Other'),
    )
    area = models.CharField(
        max_length=12,
        choices=AREA_CHOICES,
        default='Other',
    )
    email = models.EmailField()
    phone = models.IntegerField()
    paid = models.DateField(default="2018-01-01")

    def __str__(self):
        return self.full_name


class BlogPosts(models.Model):
    poster = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    image = ImageField(upload_to='blog-pic')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "BlogPosts"
