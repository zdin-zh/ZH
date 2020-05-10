from django.shortcuts import render, redirect
from authentication.forms import PostForm
from smzedahapp.models import Post


# Create your views here.
def upload(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        form.save()
        return redirect("upload")

    context = {
        "form": PostForm(),
        "alldata": Post.objects.all()
    }
    return render(request, "home.html", context)    