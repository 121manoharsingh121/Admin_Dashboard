from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def StudentDashboardView(request):
    return render(request,'student/studentview.html')