from django.shortcuts import render
from .models import ImageModel
from .forms import ImageForm
# Create your views here.
def home(request):
    if request.method=='POST':
        form=ImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
    form=ImageForm()
    img=ImageModel.objects.all()
    return render(request,'app1/hello.html',{'form':form,'img':img})