from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from blogapp.models import Post
# Create your views here.
def Home(request):
    posts = Post.objects.all().order_by('-created_on')[::]
    context={
        'post_list':posts
    }
    return render(request,"home.html",context)

def addpost(request):
    print(request)
    if request.method=='POST':
        entry_title = request.POST['title']
        author = request.POST.get("author", "Guest (or whatever)")
        content = request.POST.get("content", "Guest (or whatever)")
        newPost = Post()
        newPost.title = entry_title
        newPost.author = author
        newPost.content = content
        newPost.save()
        return redirect("../")
    return render(request,"newpost.html")
def viewDetail(request,item):
    detailPost = Post.objects.all()[::-1][item-1]
    context={
        'post_detail':detailPost
    }
    return render(request,"detail_post.html",context)