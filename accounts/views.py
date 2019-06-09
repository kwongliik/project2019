from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .forms import SignUpForm, UserInformationUpdateForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, 'Successful signup!')
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'my_account.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myImage = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myImage.name, myImage)
        messages.info(request, 'Successful import image!')
        uploaded_image_url = fs.url(filename)
        return render(request, 'upload_image.html', {
            'uploaded_image_url': uploaded_image_url
        })
    return render(request, 'upload_image.html')
