# Generated by Django 5.0.3 on 2024-03-22 07:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_groupchatmsg_author_alter_groupchatmsg_group_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdeco',
            name='nickname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userdeco',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]