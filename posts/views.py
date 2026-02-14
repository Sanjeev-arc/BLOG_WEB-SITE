from django.shortcuts import render,redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
    posts=Post.objects.filter(is_deleted=False).order_by('-created_at')
    context={
        'posts':posts
    }
    return render(request,'posts/home.html',context=context)

@login_required
def dashboard(request):
    if request.method=='POST':
        title=request.POST.get('title', '').strip()
        content=request.POST.get('content', '').strip()
        image=request.FILES.get('image')
        
        # Validation
        if title and content:
            Post.objects.create(author=request.user,title=title,content=content,image=image)
        return redirect('dashboard')    
    posts=Post.objects.filter(author=request.user,is_deleted=False).order_by('-created_at')
    context={
        'posts':posts
    }
    return render(request,'posts/dashboard.html',context=context)

def post_delete(request,id):
    post=get_object_or_404(Post,id=id,author=request.user)      
    if request.method=='POST':
        post.is_deleted=True
        post.save()
        return redirect('dashboard')

def trash_view(request):
    deleted_posts=Post.objects.filter(author=request.user,is_deleted=True).order_by('-created_at')
    context={
        'deleted_posts':deleted_posts
    }
    return render(request,'posts/trash.html',context=context)

def restore_post(request,id):
    post=get_object_or_404(Post,id=id,author=request.user,is_deleted=True)
    if request.method=="POST":
        post.is_deleted=False
        post.save()
        return redirect('trash_view')

def permanent_delete(request, id):
    post=get_object_or_404(Post, id=id, author=request.user, is_deleted=True)
    if request.method == "POST":
        post.delete()
        return redirect('trash_view')
def post_detail(request,id):
    post=get_object_or_404(Post,id=id,is_deleted=False)
    context={
        'post':post
    }
    return render(request,'posts/post_detail.html',context=context)   

def post_edit(request,id):
    post=get_object_or_404(Post,id=id,author=request.user,is_deleted=False)
    if request.method=='POST':
        title=request.POST.get('title', '').strip()
        content=request.POST.get('content', '').strip()
        image=request.FILES.get('image')
        
        # Validation
        errors = []
        if not title:
            errors.append('Title is required')
        if not content:
            errors.append('Content is required')
        
        if errors:
            context={'post':post, 'errors':errors}
            return render(request,'posts/post_edit.html',context=context)
        
        post.title=title
        post.content=content
        if image:
            post.image=image
        post.save()
        return redirect('dashboard')
    context={'post':post}
    return render(request,'posts/post_edit.html',context=context)