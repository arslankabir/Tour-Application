from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth #auth will use as a login part 
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if User.objects.filter(username=username).exists():
            print("This User Name is Already exists.")
            messages.info(request,'Username_TAKKEN')
            return redirect('/accounts/signup2/')
        elif User.objects.filter(email=email).exists():
            print("This email is Already exists")
            messages.info(request,'email_TAKKEN')
            return redirect('/accounts/signup2/')
        elif password1!=password2:
            print("password didnt matched")
            messages.info(request,'Password_DID_NOT_MATCHED')
            return redirect('/accounts/signup2/')
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            print('\nUser created')
            messages.info(request,'USER_CREATED')
            return redirect('/accounts/login2/')
    else:
        return render(request, "signup2.html")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>login>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("You are loged in")
            return redirect('/')
        else:
            print("You are not loged in")
            return redirect('/accounts/login2/')
    else:
        return render(request,'login2.html')
    
#>>>>>>>>>>>>>>>>>>>logout>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def logout(request):
    auth.logout(request)
    return redirect('/')
