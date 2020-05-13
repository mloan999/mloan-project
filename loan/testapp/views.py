from django.shortcuts import render,redirect
from django.conf import settings
from testapp.models import loan
from testapp.forms import loanform,UserForm
from testapp import forms
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def contact(request):
    return render(request,'testapp/contact.html')

def about(request):
    return render(request,'testapp/about.html')

def services(request):
    return render(request,'testapp/services.html')

def post(request):
    return render(request,'testapp/post.html')

def smile(request):
    return render(request,'testapp/smile.html')

# def form(request):
#     return render(request,'testapp/form.html')

def tanku(request):
    return render(request,'testapp/tanku.html')



#

def register(request):
    registered = False
    if request.method == 'POST':
        # user_form = UserForm(data=request.POST)
        profile_form = loanform(data=request.POST)
        if profile_form.is_valid():
            # user_form.save()
            # user.set_password(user.password)
            # user.save()
            profile = profile_form.save(commit=False)
            # profile.user = user
            if 'upload_bankstatement' and 'upload_aadhar' and 'upload_pan' in request.FILES:
                print('found it')
                profile.upload_bankstatement = request.FILES['upload_bankstatement']
                profile.upload_aadhar= request.FILES['upload_aadhar']
                profile.upload_pan= request.FILES['upload_pan']
            profile.save()
            return redirect("/tanku")
            registered = True
        else:
            print(profile_form.errors)
    else:
        # user_form = UserForm()
        profile_form = loanform()
    return render(request,'testapp/form.html',
                          {'profile_form':profile_form,
                           'registered':registered})

# def register(request):
#     form=forms.loanform()
#     if request.method=='POST':
#         form=forms.loanform(request.POST)
#         if form.is_valid():
#             if 'upload_bankstatement' in request.FILES:
#                 print('found it')
#                 form.upload_bankstatement = request.FILES['upload_bankstatement']
#             form.save()
#             return redirect("/tanku")
#         else:
#             print(form.errors)
#     else:
#         form=loanform()
#     return render(request,'testApp/form.html',{'form':form})
