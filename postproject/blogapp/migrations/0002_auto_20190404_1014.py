# Generated by Django 2.0.7 on 2019-04-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateField(verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
