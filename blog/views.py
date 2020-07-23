from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import Post_form, Comment_form

#importamos decoradores para proteger las vista de post.
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})  

#este decorador limita el acceso a esta vista a menos que estes logeado
@login_required
def post_new(request):
    '''
    esta vista se encarga de agregar un nuevo post
    '''
    #hacemos uso de un metodo if que valida que el formulario es un POST
    if request.method == 'POST':
        #creamos nuestro formulario.
        form = Post_form(request.POST)
        #validamos el formulario
        if form.is_valid():
            #hacemos un save false
            post = form.save(commit=False)
            #asiganamos el autor por sistema
            post.author = request.user
           # post.published_date = timezone.now()
            post.save() #guardamos el post
            return redirect('post_detail', pk=post.pk)
    else:    
        form = Post_form()
    return render(request,'blog/post_edit.html',{'form':form})   


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method =='POST':
        form = Post_form(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
           # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)           

    else:
        form = Post_form(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    '''
    esta vista muestra los post no publicados
    '''
    #obtenemos un queryset que filtra y los post
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts}) 


@login_required
def post_publish(request, pk):
    '''
    esta funcion vista se encarga de publicar los post no publicados
    '''
    #obtenemos el post
    post = get_object_or_404(Post, pk=pk)
    #usamos el metodo publish
    post.publish()
    return redirect('post_detail', pk=pk) 


@login_required
def post_remove(request, pk):
    '''
    esta funcion vista se encarga de eliminar un post seleccionado
    '''
    #obtenemos el post con el id que pasa por parametro.
    post = get_object_or_404(Post, pk=pk)
    #eliniminamos el post
    post.delete()
    #redireccionamos a la vista post_list
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = Comment_form()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})       

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)  

@login_required
def comment_remove(request, pk):
    comment =  get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)      