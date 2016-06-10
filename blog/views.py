from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.
def post_list(request):
	post_list = Post.objects.all()
	query = request.GET.get('query')
	if query:
		post_list = post_list.filter(text__icontains=query)
	return render_to_response('blog/post_list.html',{'post_list':post_list,
													 'query':query})
def post_detail(request, pk):
	post = Post.objects.get(id=pk)
	return render_to_response('blog/post_detail.html',{'post':post})
def about(request):
	return render_to_response('blog/about.html')
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = request.user
			post.create_date = timezone.now()
			post.save()
			return redirect('blog.views.post_list')
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html',{'form':form})
def post_edit(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = request.user
			post.create_date = timezone.now()
			post.save()
			return redirect('blog.views.post_list')
	else:
		form = PostForm(instance=post)
	return render(request,'blog/post_edit.html',{'form':form})
def todo(request):
	return render_to_response('blog/todo.html')