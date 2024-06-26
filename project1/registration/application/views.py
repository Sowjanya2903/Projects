from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from application.models import Person,todoapp
from django.views.decorators.csrf import requires_csrf_token

def fun(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        first_name=request.POST.get('full_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('Confirm_Password')
        if password==confirm_password:
            User.objects.create_user(username=username,password=password,email=email,first_name=first_name)    
            messages.info(request,"'Registration Successful!' 'You can login now.'")
            return redirect('signin')
        else:
            messages.info(request,"password do not match.Please try again!")
            return redirect('register')
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,"Login Successful !")
            return redirect('task')
        else:
            messages.info(request,"password do not match.Please try again!")
            return redirect('signin')
    return render(request,'signin.html')

@login_required(login_url='signin')
def task(request):
    if request.method=='POST':
        todo_item=request.POST.get('todo_item')
        date=request.POST.get('date')
        det=todoapp(task=todo_item,date=date,user_id=request.user.id)
        det.save()
        messages.info(request,"You have entered task Successfully")
    data=todoapp.objects.filter(user_id=request.user.id)
    return render(request,'display.html',{'data':data})

def edit(request,id):
    if request.method == 'POST':
        todo_item=request.POST.get('todo_item')
        date=request.POST.get('date')
        todoapp.objects.filter(id=id).update(task=todo_item,date=date) 
        messages.info(request,"You have edited task Successfully") 
        return redirect('task')
    return render(request,'display.html')

def delete(request,id):
    todoapp.objects.filter(id=id).delete()
    messages.info(request,"You have deleted the task Successfully")
    return redirect("task")

def finished(request,id):
    get_todo=todoapp.objects.get(user=request.user,id=id)
    get_todo.status = True
    get_todo.save()
    messages.info(request,"You have finished the task successfully")
    return redirect('task')

def searchbar(request):
    query = request.GET.get('search') 
    if query: 
        data = todoapp.objects.filter(user_id=request.user.id, task=query)
    else:
        data = todoapp.objects.filter(user_id=request.user.id)

    return render(request, 'display.html', {'data': data})
