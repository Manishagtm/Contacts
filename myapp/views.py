from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from myapp.templatetags import extras


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email1']

        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for error input

        if len(username) > 15:
            messages.error(request, " Your username must be under 15 characters")
            return redirect('sign')

        if not username.isalnum():
            messages.error(request, " Username should only contain letters and numbers")
            return redirect('sign')
        if pass1 != pass2:
            messages.error(request, " Passwords do not match")
            return redirect('sign')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('log/')

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("log/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def sign(request):
    return render(request, 'sign.html')


def home(request):
    return render(request, "home.html")


def index(request):
    return render(request, 'form.html')


def two(request):
    return render(request, 'two.html')


def log(request):
    return render(request, 'login.html')


def userprofile(request):
    return render(request, 'userprofile.html')


def edit(request):
    return render(request, 'edit.html')


def feedback(request):
    return render(request, 'feedback.html')


# def contact(request):
#   return render(request, 'contacts.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
            return redirect('/')

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
            return redirect('/')

    return render(request, "contacts.html")
