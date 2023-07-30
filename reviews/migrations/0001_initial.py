# Generated by Django 3.2.20 on 2023-07-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]