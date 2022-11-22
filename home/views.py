from tkinter.tix import Tree
from django.shortcuts import render,redirect
from home.models import schedule,candidates
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.
def checktime(start,end):
    print(start,end)
    startdate = start[0:10]
    enddate = end[0:10]
    if (startdate != enddate):
        return []
    starttime = start[11:]
    endtime = end[11:]
    starthour = starttime[0:2]
    endhour = endtime[0:2]

    startmin = int(starttime[3:])
    endmin = int(endtime[3:])
    print(starthour, endhour)
    print(startmin, endmin)
    if(starthour > endhour or startmin >= endmin):
        return []
    return [startdate , starttime , endtime] # date , starttime , endtime

def is_available(cur_user,cur_date,starttime,endtime):
    # i have to check if it has another interview at this date
    #find all interviews of cur user
    uid = User.objects.get(username=cur_user)
    allinterviews = candidates.objects.filter(candidate_name=uid.id)
    print(len(allinterviews)) 
    for i in allinterviews:
        #check if ith interviw is on same date
        interviewID = i.interview_id.id
        cur_interview = schedule.objects.get(id=interviewID)
        print("cur date",cur_interview.interviewDate ," ",cur_date)
        if(cur_interview.interviewDate != cur_date):
            return True
        
        #now check if time collapse or not
        if(int(starttime[0:2])>=int(cur_interview.intervieweStartTime[0:2]) or int(starttime[0:2])<=int(cur_interview.intervieweEndTime[0:2])):
            return False
        if(endtime[0:2]>=int(cur_interview.intervieweStartTime[0:3]) or endtime[0:2]<=int(cur_interview.intervieweEndTime[0:3])):
            return False
    return True
        


def home(request):
    if request.method == 'POST':
        interviewerName = request.POST['interviewerName']
        interviewerEmail = request.POST['interviewerEmail']
        intervieweeName = request.POST['intervieweeName']
        intervieweeEmail = request.POST['intervieweeEmail']
        intervieweStartTime = request.POST['intervieweStartTime']
        intervieweEndTime = request.POST['intervieweEndTime']
        some_var = request.POST.getlist('inlineCheckbox')
        allinterviewers = ""
        #checking the time entered is valid or not 
        date_and_time = checktime(intervieweStartTime,intervieweEndTime)
        if(len(date_and_time))>0 :
            pass
        else:
            messages.error(request, 'Incorrect date or time entered!!')
            return redirect('/')
        date = date_and_time[0]
        starttime = date_and_time[1]
        endtime = date_and_time[2]
       
        if len(some_var)>=1:
            for i in some_var:
                # check if ith candidate is availbe or not
                if(is_available(i,date,starttime,endtime)==False):
                    messages.error(request, f'{i} has a another interview on this date and time!!')
                    return redirect('/')
                allinterviewers = allinterviewers + i + " , "
            # print(interviewerName,interviewerEmail,intervieweeName,intervieweeEmail,intervieweStartTime,intervieweEndTime,some_var)
            entry = schedule(interviewerName=interviewerName,interviewerEmail=interviewerEmail,intervieweeName=intervieweeName,intervieweeEmail=intervieweeEmail,user=request.user,intervieweStartTime=intervieweStartTime,intervieweEndTime=intervieweEndTime,allinterviewers=allinterviewers,interviewDate=date)
            entry.save()
            
            for i in some_var:
                can_user = User.objects.get(username=i)
                can_entry = candidates(candidate_name=can_user,interview_id=entry)
                can_entry.save()

            # and update this interview in candidates table also
            
            messages.success(request, 'Interview scheduled successfully')
        else:
            messages.error(request, 'At Least one candidate is required!!')
            return redirect('/')
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
        email = request.POST['email']
        print(username, password)
        user = user = User.objects.create_user(username, email, password)
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

def del_candidates_by_schedule_id(del_schedule):
    candidates.objects.filter(interview_id=del_schedule).delete()
    

def deletetask(request,slug):
    if request.method=="GET":
        # x = Task.objects.filter(id=id).delete()
        try:
            del_schedule = schedule.objects.get(id = slug)
            #this will delete all objecs of candidates 
            del_candidates_by_schedule_id(del_schedule)
            del_schedule.delete()
            
            messages.success(request,'Deleted successfully!')
            return redirect('/task/')
        except:
            messages.error(request,'Some error occured!!')
    else:
        print('not get')
    return HttpResponse('del')

def edittask(request,slug):

    #first delete all the candidates of this schedule
    del_candidates_by_schedule_id(slug)

    task = schedule.objects.get(id = slug) 
    if request.method == "POST":
        print("post")
        interviewerName = request.POST['interviewerName']
        interviewerEmail = request.POST['interviewerEmail']
        intervieweeName = request.POST['intervieweeName']
        intervieweeEmail = request.POST['intervieweeEmail']
        intervieweStartTime = request.POST['intervieweStartTime']
        intervieweEndTime = request.POST['intervieweEndTime']
        some_var = request.POST.getlist('inlineCheckbox')
        allinterviewers = ""
        date_and_time = checktime(intervieweStartTime,intervieweEndTime)
        if(len(date_and_time))>0 :
            pass
        else:
            messages.error(request, 'Incorrect date or time entered!!')
            return redirect('/edittask/' + slug)
        date = date_and_time[0]
        starttime = date_and_time[1]
        endtime = date_and_time[2]
        if len(some_var)>=1:
            for i in some_var:
                # check if ith candidate is availbe or not
                if(is_available(i,date,starttime,endtime)==False):
                    messages.error(request, f'{i} has a another interview on this date and time!!')
                    return redirect('/edittask/' + slug)
                allinterviewers = allinterviewers + i + " , "
        
            task.interviewerName = interviewerName
            task.interviewerEmail = interviewerEmail
            task.intervieweeName = intervieweeName
            task.intervieweeEmail = intervieweeEmail
            task.intervieweStartTime = intervieweStartTime
            task.intervieweEndTime = intervieweEndTime
            task.allinterviewers = allinterviewers
            task.save()
            for i in some_var:
                can_user = User.objects.get(username=i)
                can_entry = candidates(candidate_name=can_user,interview_id=task)
                can_entry.save()
            messages.success(request, 'Interview Updated successfully')
            return redirect('/task/') 
        else:
            messages.error(request, 'At Least one interviewer required!!')
            return redirect('/edittask/' + slug)
    context = {"interviewerName":task.interviewerName,"interviewerEmail":task.interviewerEmail,"intervieweeName":task.intervieweeName,"intervieweeEmail":task.intervieweeEmail,"intervieweStartTime":task.intervieweStartTime,"intervieweEndTime":task.intervieweEndTime}
    print(context)
    return render(request,'edit.html',context)

