from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Gallery, Message, Contact, Profile
from django.views.generic import ListView, DetailView
from blog.form import MessageForm


# Create your views here.
content = {}

class PostListView(ListView):
	content['posts'] = Post.objects.all()
	model = Post
	template_name = 'pub.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class GalListView(ListView):
	content['gal'] = Gallery.objects.all()
	model = Gallery
	template_name = 'gallery.html'
	context_object_name = 'gal'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def cont(request):
	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			form = MessageForm()
			#content['form'] = form
			messages.success(request, f' Tua mensagem foi enviada com sucesso !')
			return redirect('cont')
	else:
		content = {'contact': Contact.objects.all(),
					'prof': Profile.objects.all()}
		form = MessageForm()
		content['form'] = form
		return render(request, 'contact.html', content) 		

def home(request):
	content = {'prof': Profile.objects.all()}
	return render(request, 'profile.html', content)
def bio(request):
	content = {'prof': Profile.objects.all()}
	return render(request, 'bio.html', content)
def pesq(request):
	# content['posts'] = ost.objects.all()
	# return render(request, content)
	return redirect('home')

	
