# Generated by Django 5.0.6 on 2024-06-06 09:49

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Yaşı'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ölkə'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='desiredcountry',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Getmək istədiyi ölkə'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favanimal',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Sevimli heyvan fotosu'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favmeal',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Sevimli yeməyi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fobbies',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Fobilər'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hobbies',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Hobilər'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='languages',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Dillər'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='İstifadəçi soyadı'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Bacarıqlar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='İstifadəçi adı'),
        ),
    ]
