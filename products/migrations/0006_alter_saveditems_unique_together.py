# Generated by Django 3.2.20 on 2023-07-31 17:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20230731_1726'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='saveditems',
            unique_together={('user', 'saved_product')},
        ),
    ]
