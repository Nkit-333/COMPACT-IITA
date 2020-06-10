from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Teaches, Faculty
from .models import Announcement as Announce
from django.core.files.storage import FileSystemStorage

from .forms import AttendanceForm
from .models import attendance

from .forms import AssignmentForm
from .models import Assignments

from .forms import TimetableForm
from .models import Timetable

from django.contrib.auth.models import User, auth
import datetime
from django.utils.timezone import utc


def index(request):
    return render(request, 'index.html')


# sutdent ---------------------------------------------------

def StudentDash(request):
    Courses = Teaches.objects.all()
    return render(request,'Student.html',{'Courses': Courses, 'user' : request.user})

def student_profile(request):
    ROLL = request.user.get_username()
    branch = ROLL[0:3]
    sem = int(ROLL[3:7])

    if branch == "IIT":
        branch = "Information Technology (IT)"
    elif branch == "IEC":
        branch = "Electronics and Communication Engineering (ECE)"

    current_year = int(datetime.datetime.now().year)
    current_month = int(datetime.datetime.now().month)

    if current_month <= 6 :
        sem = (current_year - sem)*2
    else:
        sem = (current_year - sem)*2 + 1
        
    return render(request, 'student_profile.html', {'user' : request.user, 'branch' : branch, 'sem' : sem})

def view_Assignment(request):
    List = Assignments.objects.all()
    return render(request, 'view_Assignment.html', {'List' : List})

def view_timetable(request):
    List = Timetable.objects.all()
    return render(request, 'view_timetable.html', {'List' : List})

def view_Attendance(request):
    List = attendance.objects.all()
    return render(request, 'view_Attendance.html', {'List' : List})

def view_Announcement(request):
    List = Announce.objects.all()
    return render(request, 'view_Announcement.html',{'List' : List} )
    

# faculty ---------------------------------------------------

def facultyDash(request):
    Subs = Faculty.objects.filter(ProfID = request.user)
    return render(request,'fac_dashboard.html', {'Subs': Subs, 'user' : request.user})

def faculty_profile(request):
    return render(request, 'faculty_profile.html')

def update_Assignment(request):
    List = Assignments.objects.all()
    return render(request, 'update_Assignment.html', {'List' : List})

def upload_Assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('update_Assignment')
    else:
        form = AssignmentForm()
    return render(request, 'upload_Assignment.html', {'form' : form})

def delete_Assignment(request, pk):
    if request.method == 'POST':
        ele = Assignments.objects.get(pk=pk)
        ele.delete()
    return redirect('../update_Assignment')

def update_timetable(request):
    List = Timetable.objects.all()
    return render(request, 'update_timetable.html', {'List' : List})

def upload_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('update_timetable')
    else:
        form = TimetableForm()
    return render(request, 'upload_timetable.html', {'form' : form})

def delete_timetable(request, pk):
    if request.method == 'POST':
        ele = Timetable.objects.get(pk=pk)
        ele.delete()
    return redirect('../update_timetable')

def update_exam_schedule(request):
    return render(request, 'update_exam_schedule.html')

def Attendance(request):
    List = attendance.objects.all()
    return render(request, 'Attendance.html', {'List' : List})

def upload_Attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Attendance')
    else:
        form = AttendanceForm()
    return render(request, 'upload_Attendance.html', {'form' : form})

def delete_list(request, pk):
    if request.method == 'POST':
        ele = attendance.objects.get(pk=pk)
        ele.delete()
    return redirect('../Attendance')

def Announcement(request):
    if request.method == 'POST':
        announcement = request.POST['announcement']
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date,time = now.split(" ")
        A = Announce(Date=date, Time=time, Name=request.user.get_full_name(), Anno=announcement)
        A.save()

    List = Announce.objects.all()
    return render(request, 'Announcement.html', {'List' : List})


def FAQ(request):
    return render(request, 'FAQ.html')