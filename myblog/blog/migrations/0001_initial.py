# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=224, verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=224, verbose_name='Заголовок')),
                ('boby', models.TextField(max_length=1300, verbose_name='Текст')),
                ('date', models.DateTimeField()),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': 'Статьи',
                'verbose_name': 'Статия',
            },
        ),
    ]
