# Generated by Django 3.1.4 on 2021-01-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['position'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
    ]
