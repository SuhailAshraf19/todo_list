from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import profile, List
from django.contrib import messages
from .forms import ListForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'index.html',{"user": request.user})
    else:
        return redirect(request,'login.html')  

    return render(request,"index.html")
def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) 

        if user is not None:
            login(request,user)
            return redirect("home")
    return render(request,"login.html")

def logout_user(request):
    logout(request)
    return redirect("login")
def signup_user(request):
    print(request)
    if request.method == 'POST':
        print("inside signup_user")
        print(f"POST Data: {request.POST}")
        username=request.POST.get('username')
        first_name = str(request.POST.get("first_name", "")).strip()
        last_name=str(request.POST.get('last_name'))
        email=request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        if password1 != password2:
            messages.error(request,"Passwods don't match")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already Taken")
            return redirect('signup')
       
        print("First Name:", request.POST.get('first_name'))  
        print("Type of First Name:", type(request.POST.get('first_name')))
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            email=email,
            last_name=last_name,
            password=password1,
          
        #     password="testpass",
        #     first_name="Test",
        #     last_name="User",
        #     email="test@example.com"
         )
        if phone_number:
            profile.objects.create(user=user, phone_number=phone_number)
       
        login(request, user)  # Logs in the user
        messages.success(request, "Signup successful!")
        return redirect("/home")   
    return render(request,"signup.html")

@login_required
def create_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid:
            new_list = form.save(commit=False)
            new_list.user=request.user
            new_list.save()
            return redirect('items' ,pk=new_list.pk)
    else:
        form=ListForm()
    return render(request,'create_list.html', {'form' : form})   
@login_required
def lists(request):
    all_lists=List.objects.filter(user=request.user) 
    return render(request,'lists.html',{'lists':all_lists})
def list_detail(request, pk):
    return render(request,"list_detail.html")    