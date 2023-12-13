from django.shortcuts import render, redirect
from .forms import UploadImageForm
from .models import UploadImage
from django.views import View

def UploadImageView(request):
    files = UploadImage.objects.all()
    form = UploadImageForm(request.POST, request.FILES)
   
    if form.is_valid():
      img = request.FILES.getlist('file')
      for i in img:
        UploadImage.objects.create(file=i)
      return redirect('home')
    
    return render(request, 'index.html', {'form':form, 'files':files})