from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from TestApp.forms import SignUpFrom

from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')
@login_required
def java_page_view(request):
    return render(request,'testapp/javaexams.html')
@login_required
def python_page_view(request):
    return render(request,'testapp/pythonexams.html')
@login_required
def aptitude_page_view(request):
    return render(request,'testapp/aptitudeexams.html')

def Logout_view(request):
    return render(request,'testapp/logout.html ')

def Sign_Up_View(request):
    form = SignUpFrom()
    #algorithm: pbkdf2_sha256 iterations:
    if request.method=="POST":
        form = SignUpFrom(request.POST)
        #we can use form.is_valid()
        #if form.is_valid():
        #form.save()

        #form.save() if we directly save like this pasword wont be encrepted
        user=form.save()
        user.set_password(user.password) #this method encrepting our password
        user.save()

        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signUp.html',{'form':form})
