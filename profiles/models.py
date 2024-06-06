from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField("auth.User", verbose_name=("İstifadəçi adı"), on_delete=models.CASCADE,  blank=True, null=True)
    lastname = models.CharField(max_length=20, verbose_name=("İstifadəçi soyadı"),  blank=True, null=True)
    age = models.IntegerField(verbose_name=("Yaşı"),  blank=True, null=True)
    country = models.CharField(max_length=30, verbose_name=("Ölkə"),  blank=True, null=True)
    skills = models.TextField(max_length=100, verbose_name=("Bacarıqlar"), blank=True, null=True)
    hobbies = models.TextField(max_length=100, verbose_name=("Hobilər"),  blank=True, null=True)
    fobbies = models.TextField(max_length=100, verbose_name=("Fobilər"),  blank=True, null=True)
    languages = models.TextField(max_length=100, verbose_name=("Dillər"),  blank=True, null=True)
    desiredcountry = models.CharField(max_length=30, verbose_name=("Getmək istədiyi ölkə"),  blank=True, null=True)
    favmeal = models.CharField(max_length=20, verbose_name=("Sevimli yeməyi"),  blank=True, null=True)
    favanimal = RichTextUploadingField(verbose_name = ("Sevimli heyvan fotosu"),  blank=True, null=True)
    