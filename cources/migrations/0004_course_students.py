# Generated by Django 3.2.15 on 2022-09-11 16:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cources', '0003_auto_20220831_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='couses_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
