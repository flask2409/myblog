from django.shortcuts import render
from django.http import Http404
from .models import Post,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def listpost(request):
	posts = Post.objects.filter(published=True)
	paginator = Paginator(posts, 5)

	page = request.GET.get('page')

	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		p = paginator.page(1)

	except EmptyPage:
		p = paginator.page(paginator.num_pages)

	return render(request, 'post/list.html', {'posts':p})



def detailpost(request,id):
	try:
		post = Post.objects.get(id=id)
	except Post.DoesNotExist:
		raise Http404
	return render(request, 'post/detail.html', {'post':post})



def category(request, id):
	category = Category.objects.select_related().get(id=id)
	posts = category.post_set.all()
	return render(request, 'post/category.html', {'posts':posts,'categories':category})