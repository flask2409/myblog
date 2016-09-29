#-*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import datetime
from ckeditor.fields import RichTextField


class Category(models.Model):
	name = models.CharField(max_length=224, verbose_name = "Категория")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'




class Post(models.Model):
	title = models.CharField(max_length=224, verbose_name = "Заголовок")
	body = RichTextField(max_length=1300, verbose_name = "Текст")
	date = models.DateTimeField(default=datetime.now)
	category = models.ForeignKey(Category, verbose_name = 'Категория')
	published = models.BooleanField(default=False, verbose_name = 'Публикация')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date']
		verbose_name = 'Статия'
		verbose_name_plural = 'Статьи'
