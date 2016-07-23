from django.shortcuts import render
from django.shortcuts import render
from post.form import FormFromSomeModel as DetailForm
# Create your views here.


def posts(request):
    if request.method == "GET":
        return render(request, 'post/form.html', {'form': DetailForm})
    elif request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            print(form)
            return render(request, 'post/form.html', {'form': DetailForm})