from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request,"index.html")
def login_user(request):
    return render(request,"login.html")

def logout_user(request):
    return render(request,"index.html")
def signup_user(request):
    return render(request,"signup.html")