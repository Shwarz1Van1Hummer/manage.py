# Generated by Django 4.0.6 on 2023-02-02 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_description_news_description_new'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-id',)},
        ),
    ]
