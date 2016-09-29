from django import template
from blog.models import Category


register = template.Library()

@register.inclusion_tag("sidebar.html")

def sidebar():
	category = Category.objects.all().order_by("name")
	return {'cat':category}