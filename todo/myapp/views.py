from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import profile, List, Items
from django.contrib import messages
from .forms import ListForm
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,"index.html")
    return redirect("login")
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
        return redirect("home")   
    return render(request,"signup.html")

@login_required
def create_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid:
            new_list = form.save(commit=False)
            new_list.user=request.user
            new_list.save()
            print(List.name) 
            return redirect('list_detail',list_id=new_list.id)
    else:
        form=ListForm()
    return render(request,'create_list.html', {'form' : form})   
@login_required
def lists(request):
    all_lists=List.objects.filter(user=request.user) 
    return render(request,'lists.html',{'lists':all_lists})
def list_detail(request, list_id):
    # Fetch the list that belongs to the logged-in user
    list_obj = get_object_or_404(List, id=list_id, user=request.user)
    
    # Fetch related items
    items = list_obj.items.all()  # Works only if related_name='items' in the Item model

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)  # Save without committing to assign list manually
            item.list = list_obj  # Associate item with the list
            item.save()  # Now save the item
            return redirect("list_detail", list_id=list_obj.id)  # Redirect to the same page after adding

    else:
        form = ItemForm()  # Initialize an empty form

    return render(request, "list_detail.html", {'list': list_obj, 'items': items, 'form': form})

@login_required
def delete_list(request, list_id):
    list_obj = get_object_or_404(List, id=list_id, user=request.user)
    list_obj.delete()
    return redirect('lists')

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    list_id = item.list.id  # Get the list ID before deleting the item
    item.delete()
    return redirect('list_detail', list_id=list_id)
@login_required
def view_profile(request):
    if request.method == "POST":
        user = request.user
        profile = user.profile
        profile.photo = request.FILES.get('photo', profile.photo)
        profile.address = request.POST.get('address', profile.address)
        profile.phone_number = request.POST.get('phone', profile.phone_number)
        profile.description = request.POST.get('description', profile.description)
        user.email = request.POST.get('email', user.email)
        user.first_name, user.last_name = request.POST.get('full_name', "").split(" ", 1)
        user.save()
        profile.save()
        return redirect('profile')  # Redirect to refresh the page
    return render(request, "view_profile.html")