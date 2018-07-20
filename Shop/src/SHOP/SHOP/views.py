from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .forms import ContactForm, LoginForm, SignUpForm

def index(request):
    context = {
        "title":"Home",
        "content":" Hello this is homepage.",

    }
   
    return render(request, "index.html", context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Hello this is contact page.",
        "form": contact_form,
    }
    if request.method == "POST":
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact.html", context)


def cart(request):
    context = {
        "title":"Cart",
        "content":"Cart component isn't ready yet",
    }
    return render(request, "index.html", context)


User=get_user_model()
def user_sign_up(request):
    form = SignUpForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        User.objects.create_user(username, email, password)

    return render(request, 'sign_up.html', context)



def user_log_in(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Error")
    return render(request, 'log_in.html', context)


def user_log_out(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'log_in.html', context)
