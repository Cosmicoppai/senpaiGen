# Generated by Django 3.1.7 on 2021-05-22 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0012_auto_20210519_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(blank=True, default='Anon', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
