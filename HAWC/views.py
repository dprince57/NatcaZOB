from django.shortcuts import render, redirect
from django.forms import modelform_factory
from HAWC.models import HAWCUser, BlogPosts

# Create your views here.


def index(request):
    UserForm = modelform_factory(HAWCUser, fields=('full_name', 'email', 'phone', 'paid', 'area'))
    if request.method == "POST":
        lform = UserForm(request.POST)
        if lform.is_valid():
            lform.save()
            return redirect('/')

    else:
        lform = UserForm()

    return render(request, 'HAWC/index2.html', {'form': lform})


def showall(request):

    show = HAWCUser.objects.all()

    context = {
        'title': 'Current ZOB HAWC Users',
        'users': show
    }

    return render(request, 'HAWC/admin/showall.html', context)


def blogpost(request):
    form = modelform_factory(BlogPosts, fields=('poster', 'title', 'body', 'image'))
    if request.method == 'POST':
        blog = form(request.POST, request.FILES)
        if blog.is_valid():
            blog.image = blog.cleaned_data['image']
            blog.save()
            return redirect('/blogpost')
    else:
        blog = form()

    return render(request, 'blogposts.html', {'blogform': blog})


def main(request):
    blogs = BlogPosts.objects.all()[:3]

    context = {
        'title': 'Current NATCA News',
        'blogs': blogs
    }

    return render(request, 'build.html', context)


def detail(request, blog_id):

    context = {
        "blog": blog_id
    }

    return render(request, 'detail.html', context)
