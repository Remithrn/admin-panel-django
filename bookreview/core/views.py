from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, Register
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    qs = request.GET.get("qs")

    if qs:
        books = Book.objects.filter(name__icontains=qs)
    else:
        books = Book.objects.all()
    form = BookForm()

    if request.method == "POST":
        print("pst")
        form = BookForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "core/index.html", {"books": books, "form": form})


@login_required(login_url="login")
@never_cache
def detail_view(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "core/detail.html", {"book": book})


@login_required(login_url="login")
@never_cache
def delete_view(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("home")


@login_required(login_url="login")
@never_cache
def edit_view(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid:
            form.save()

            return redirect("home")
    return render(request, "core/edit.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("user")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hello {user.username} ")
            return redirect("home")
        else:
            messages.error(request, "incorrrect username or password ,try again")
            return render(request, "core/login.html")

    return render(request, "core/login.html")


def register(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)
        
        if form.is_valid():
            is_staff = form.cleaned_data.get('is_staff', False)
            
            
            if is_staff:
                user = form.save(commit=False)
                user.is_staff = True
                user.is_superuser = True
                print(user)
                user.save()
                
                messages.success(request, "Successfully created an account")
                return redirect("login")
            else:
                form.save()
                messages.success(request, "Successfully created an account")
                return redirect("login")
        else:
            form = Register(request.POST)
            messages.error(request, form.errors)
            return render(request, "core/register.html", {"form": form})

    return render(request, "core/register.html", {"form": form})


@login_required(login_url="login")
@never_cache
def logout_view(request):
    logout(request)
    return redirect("login")


def admin_view(request):
    qs = request.GET.get("qs")

    if qs:
        users = User.objects.filter(username__icontains=qs)
    else:
        users = User.objects.all()

    return render(request, "core/admin.html", {"users": users})

@user_passes_test(lambda u: u.is_superuser,login_url='error')
@never_cache
def detail_user(request, pk):
    user1 = User.objects.get(pk=pk)
    return render(request, "core/user_detail.html", {"user": user1})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="login")
@never_cache
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    form = Register(instance=user)
    if request.method == "POST":
        form = Register(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully created an account")
            return redirect("user")
        else:
            form = Register(request.POST)
            messages.error(request, form.errors)
            return render(request, "core/register.html", {"form": form})
    return render(request, "core/register.html", {"form": form})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="login")
@never_cache
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.success(request, "account deleted successfully")
    return redirect("user")


def error_page(request):
    messages.error(request,'only super users can access that functionality')
    return redirect('user')

