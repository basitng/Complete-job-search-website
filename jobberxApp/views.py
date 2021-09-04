from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

from .forms import CreateUserForm, ProfileForm, DefaultProfileForm
from .models import JobPost

def homePage(request):
    return render(request, 'routes/index.html')

@login_required(login_url='/login')
def singlePage(request, pk):
    post = JobPost.objects.get(id=pk)
    context = {
        'posts': post
    }
    return render(request, 'routes/single.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('job')
        else:
            messages.error(request, "username or password is not correct")
    return render(request, 'routes/login.html')

    # kingsley landcruiser@222

def signupPage(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("job")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CreateUserForm()
    return render(request, 'routes/signup.html', context={"form":form})

@login_required(login_url='/login')
def jobPage(request):
    post = JobPost.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'routes/job.html', context)

@login_required(login_url='/login')
def savedJobsPage(request):
    post = JobPost.objects.filter()
    context = {
        'posts': post
    }
    return render(request, 'routes/saved-jobs.html', context)

# pass76ng346
@login_required(login_url='/login')
def profilePage(request):
    if request.method == 'POST':
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        d_form = DefaultProfileForm(request.POST, instance=request.user)

        if p_form.is_valid() and d_form.is_valid():
            p_form.save()
            d_form.save()
            messages.success(request, "Profile updated")
            return redirect('profile')
    else:
        messages.error(request, "Profile not created")
        p_form = ProfileForm(instance=request.user)
        d_form = DefaultProfileForm(instance=request.user.profile)

    context = {'p_form': p_form,'d_form': d_form}
    return render(request, 'routes/profile.html', context)

def forgotPasswordPage(request):
    return render(request, 'routes/forgot-password.html')

def logoutFunc(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')