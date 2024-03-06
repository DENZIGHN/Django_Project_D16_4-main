# Generated by Django 4.2 on 2023-07-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_choice_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='PostCategory', through='news.PostCategory', to='news.category'),
        ),
    ]
