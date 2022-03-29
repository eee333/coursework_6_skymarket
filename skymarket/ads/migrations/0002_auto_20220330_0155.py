# Generated by Django 3.2.6 on 2022-03-29 22:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['created_at'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AddField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='title',
            field=models.CharField(default=0, max_length=50, validators=[django.core.validators.MinLengthValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='ad',
            field=models.ManyToManyField(to='ads.Ad'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=0, max_length=400),
            preserve_default=False,
        ),
    ]
