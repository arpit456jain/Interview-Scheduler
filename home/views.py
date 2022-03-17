from django.shortcuts import render,redirect
from home.models import schedule
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        interviewerName = request.POST['interviewerName']
        interviewerEmail = request.POST['interviewerEmail']
        intervieweeName = request.POST['intervieweeName']
        intervieweeEmail = request.POST['intervieweeEmail']
        intervieweStartTime = request.POST['intervieweStartTime']
        intervieweEndTime = request.POST['intervieweEndTime']
        
        print(interviewerName,interviewerEmail,intervieweeName,intervieweeEmail,intervieweStartTime,intervieweEndTime)
        entry = schedule(interviewerName=interviewerName,interviewerEmail=interviewerEmail,intervieweeName=intervieweeName,intervieweeEmail=intervieweeEmail,user=request.user,intervieweStartTime=intervieweStartTime,intervieweEndTime=intervieweEndTime)
        entry.save()
        print("true")
    return render(request,'index.html')

def task(request):
    print(request.user.id)
    if request.user.id == None:
        print("login needed")
    else:
        allschedule = schedule.objects.filter(user=request.user)
        context = {"allschedule":allschedule}
        print(allschedule)
        return render(request,'task.html',context)
    return render(request,'task.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = user = User.objects.create_user(username, 'email', password)
        user.save()
    else:
        print("get")
        
    return render(request,"signup.html")

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            print("invalid")
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect('/')

def deletetask(request,slug):
    if request.method=="GET":
        print("get")
        slug=int(slug)
        print(slug,type(slug))
        # x = Task.objects.filter(id=id).delete()
        x = schedule.objects.get(id = slug)  
        print(x)
        try:
            x.delete()
            # messages.success(request,'task is successfully deleted!')
            return redirect('/task/')
        except:
            messages.error(request,'Some error occured!!')
    else:
        print('not get')
    return HttpResponse('del')

def edittask(request,slug):
    task = schedule.objects.get(id = slug) 
    if request.method == "POST":
        print("post")
        interviewerName = request.POST['interviewerName']
        interviewerEmail = request.POST['interviewerEmail']
        intervieweeName = request.POST['intervieweeName']
        intervieweeEmail = request.POST['intervieweeEmail']
        intervieweStartTime = request.POST['intervieweStartTime']
        intervieweEndTime = request.POST['intervieweEndTime']
        
        print(interviewerName,interviewerEmail,intervieweeName,intervieweeEmail)
        task.interviewerName = interviewerName
        task.interviewerEmail = interviewerEmail
        task.intervieweeName = intervieweeName
        task.intervieweeEmail = intervieweeEmail
        task.intervieweStartTime = intervieweStartTime
        task.intervieweEndTime = intervieweEndTime
        task.save()
        return redirect('/task/') 
    context = {"interviewerName":task.interviewerName,"interviewerEmail":task.interviewerEmail,"intervieweeName":task.intervieweeName,"intervieweeEmail":task.intervieweeEmail,"intervieweStartTime":task.intervieweStartTime,"intervieweEndTime":task.intervieweEndTime}
    print(context)
    return render(request,'edit.html',context)

