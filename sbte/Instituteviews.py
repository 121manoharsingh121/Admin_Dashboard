from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def InstituteDashboardView(request):
    return render(request,'instituteview.html')