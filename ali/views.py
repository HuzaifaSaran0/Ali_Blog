from django.shortcuts import render, HttpResponse, redirect
from ali.models import Post, PostComment
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from ali.forms import EmailForm


def home(request):
    # all_posts = Post.objects.all()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['email']
            subject = "Thank you for subscribing!"
            message = "Welcome to our mailing list."
            from_email = settings.EMAIL_HOST_USER

            # Send the email
            send_mail(subject, message, from_email, [recipient_email])
            messages.success(
                request, "You have successfully subscribed to our mailing list.Chk your email for confirmation")
            # Redirect to a success page
            return render(request, 'ali/ali.html')
    else:
        form = EmailForm()
    all_posts = Post.objects.order_by(
        '-time_stamp')[:3]  # Get the latest 3 posts

    return render(request, "ali/ali.html", {'all_posts': all_posts, 'form': form})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        phone = request.POST['phone']
        # print(username, firstname, lastname, email, pass1, pass2, phone)
        # Create the user
        if User.objects.filter(username=username).exists():
            messages.error(
                request, f"This Username {username} is already registered for an account. Try another username.")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(
                request, f"This Email {email} is already registered for an account. Try another email.")
            return redirect('signup')
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('signup')
        if not username.isalnum():
            messages.error(
                request, "Username should only contain letters and numbers")
            return redirect('signup')
        if len(pass1) < 8:
            messages.error(request, "Password must be atleast 8 characters")
            return redirect('signup')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.phone = phone
        myuser.save()
        messages.success(
            request, "Your ALI account has been successfully created")
        return redirect('/signin/')

    return render(request, "blog/signup.html")


def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/signin')
    return render(request, "blog/signin.html")


def signout(request):
    # if request.method == "POST":
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/signin/')


def send_email_view(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['email']
            subject = "Thank you for subscribing!"
            message = "Welcome to our mailing list."
            from_email = settings.EMAIL_HOST_USER

            # Send the email
            # send_mail(subject, message, from_email, [recipient_email])
            print("Email sent")
            messages.success(request, "You have successfully subscribed to our mailing list.Chk your email for confirmation")
            # Redirect to a success page
            return render(request, 'ali/ali.html')
    else:
        form = EmailForm()
    print(form)
    return render(request, 'basic.html', {'form': form})

    # return render(request, "blog/logout.html")
