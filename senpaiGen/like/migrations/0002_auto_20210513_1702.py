# Generated by Django 3.1.7 on 2021-05-13 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210420_0100'),
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Likes', to='post.post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
