# Generated by Django 2.2.2 on 2019-10-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20191009_0044'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(to='articles.Article'),
        ),
    ]
