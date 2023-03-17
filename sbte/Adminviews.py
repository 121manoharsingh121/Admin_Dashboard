import random
import string
from tabulate import tabulate
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from sbte.forms import (
                        InstituteForm, InstituteAddForm,
                        ProgramForm, ProgramAddForm,
                        AcademicSessionForm,AcademicSessionAddForm,
                        UserForm,UserAddForm, 
                       )
from sbte.models import Institute,Program,AcademicSession,Student,User,Exams, CourseLe
from django.contrib.auth.hashers import make_password
from utils.helpers import *



'''--------------------------------------------------------------------------------------------'''
"""TABULAR REPORT"""
def TabularReportView(request):
	response = HttpResponse(content_type='text/plain')
	programsobj = Program.objects.all()
	examsobj = Exams.objects.all()
	semester = [1,2,3,4,5,6]

	if request.method == 'POST':
		sem = request.POST.get('semester_no')
		pcode = request.POST.get('program_code')
		aterm = request.POST.get('academic_term')
		rtype = request.POST.get('report_type')
		instcode = request.POST.get('institute')	
		examdetails = examsobj.filter(pk=aterm).first()
		programdetails = programsobj.filter(pk=pcode).first()
		icode = programdetails.code + str(examdetails.pk)
		institutedetails = Institute.objects.filter(code=icode).first()
		studobj = Student.objects.filter(institute=int(instcode),program=int(pcode)).all()
				
		if rtype == '1':
			response['Content-Disposition'] = 'attachment;filename = {}.txt'.format('Examination_Form_Verification_Report')
			initial_print = '''
			Examination Form Verification Report
			sem:\t{}
			exam:\t{}
			name of institute:\t{}
			institute code:\t{}
			name of branch:\t{}
			branch code:\t{}
			exam held:\t{}
			report time:\t{}
			'''.format(
				sem,
				examdetails.academic_term,
				institutedetails.name,
				icode,
				programdetails.name,
				programdetails.code,
				examdetails.exam_held,
				datetime.now())
			response.write(initial_print)
			response.writelines('\n')
			fields_names=['reg_no','first_name','middle_name','last_name','gender','modified_date','category','PaymentStatus']			
			response.write((tabulate(customQuerysetReportTable(studobj,fields_names), headers=fields_names, tablefmt='psql',)))
			return response

		if rtype == '2':
			response['Content-Disposition'] = 'attachment;filename = {}.txt'.format('Attendence_Sheet_Of_Students')
			initial_print='''
			Attendence sheet of students
			Name of Institute:{}
			Name of Branch:{}
			Name of Exam:{},held in {}
			'''.format(
				institutedetails.name,
				programdetails.name,
				examdetails.academic_term,examdetails.exam_held
			)
			response.write(initial_print)
			response.writelines('\n')
			fields_names = ['sr.','Roll Number, Name & Signature','Subject\nCode','Date of\nExam','Signature of Student/\nAbsent','Copy No.','Signature of Invigilator']
			table = []
			for value in studobj.values():
				sign = 'E:\WNC8\project\static\images\inner-image\sign.jpg'
				subject_code = '''123\n234\n345'''
				empty= '_'			
				table.append(['{}\n{}\n{}\n{}'.format(value['reg_no'], value['first_name'],'-'*len(fields_names[1]) ,sign),'{}\n '.format( subject_code),'{}\n '.format(subject_code),(empty*len(fields_names[4]) + '\n')*3,(empty*len(fields_names[5]) + '\n')*3,(empty*len(fields_names[6]) + '\n')*3])
			response.write((tabulate(table, headers=fields_names, tablefmt='grid',showindex=True,)))
			return response

	context = {
		'programsobj':programsobj,
		'examsobj':examsobj,
		'semester':semester,
		'instoj':Institute.objects.all(),
	}
	return render(request, 'report.html', context)



'''--------------------------------------------------------------------------------------------'''
"""ADMIN DASHBOARD"""
@login_required(login_url='/login/')
def DashboardView(request):    
    context =  {"name": request.user.first_name +" "+request.user.last_name}
    return render(request,'dashboard.html', context)


'''--------------------------------------------------------------------------------------------'''
"""INSTITUTE MANAGEMENT"""
##All Institute List View##
def InstituteListView(request):
    institutes = Institute.objects.filter(is_deleted=False)
    context = {
        'institutes':institutes,
    }
    return render(request,'institute/list.html',context)

##Institute Add View##
def InstituteAddView(request):
    if request.method == 'POST':
        form = InstituteAddForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('institutelist-view')
            except:
                return HttpResponse('Please Write valid Details !!!')
    else:
        form = InstituteAddForm()        
    return render(request,'institute/add.html',{'form':form})

##Institute Edit View## 
def InstituteEditView(request,id):
    institute = Institute.objects.get(id=id)
    form = InstituteForm(instance=institute)
    if request.method == 'POST':
        form = InstituteForm(request.POST, instance=institute)
        if form.is_valid():
            form.save()
            return redirect('institutelist-view')
    context = {
        'institute': institute,
        'form':form
        }
    return render(request,'institute/edit.html',context)

##Institute Delete View##
def InstituteDeleteView(request,id):
    institute = Institute.objects.filter(id=id)
    if request.method == 'GET' or request.is_ajax():
        institute.update(is_deleted=True,is_active=False)
        return redirect('institutelist-view')
    data = {
            'status': 'Deleted Successfully',
            'status_text': 'Deleted',
            'status_icon': 'success'
            }
    '''Sending Json Data in Response'''
    return JsonResponse(data)
 

'''--------------------------------------------------------------------------------------------'''    
"""PROGRAM MANAGEMENT"""
##All Program List View##
def ProgramListView(request):
    programs = Program.objects.filter(is_deleted=False)
    context = {
        'programs':programs,
    }
    return render(request, 'program/list.html', context)

##Program Add View##
def ProgramAddView(request):
    if request.method == 'POST':
        form = ProgramAddForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('programlist-view')
            except:
                return HttpResponse('Please Write valid Details !!!')
    else:
        form = ProgramAddForm()
    return render(request, 'program/add.html',{'form':form})        

##Program Edit View##
def ProgramEditView(request,id):
    program =Program.objects.get(id=id)
    form = ProgramForm(instance=program)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('programlist-view')
    context = {
        'program': program,
        'form':form
        }
    return render(request,'program/edit.html',context)

##Program Delete View##
def ProgramDeleteView(request,id):
    program = Program.objects.filter(id=id)
    if request.method == 'GET' or request.is_ajax() :
        program.update(is_deleted=True,is_active=False)
        return redirect('programlist-view')
    data = {
            'status': 'Deleted Successfully',
            'status_text': 'Deleted',
            'status_icon': 'success'
            }
    '''Sending Json Data in Response'''
    return JsonResponse(data)


'''--------------------------------------------------------------------------------------------'''
"""ACADEMIC SESSION MANAGEMENT"""
##All Session List View##
def AcademicSessionListView(request):
    sessions = AcademicSession.objects.filter(is_deleted=False)
    context = {
        'sessions':sessions,
    }
    return render(request,'academicsession/list.html',context)

##Session Add View##
def AcademicSessionAddView(request):
    if request.method == 'POST':
        form = AcademicSessionAddForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('academicsessionlist-view')
            except:
                return HttpResponse('Please Write valid Details !!!')
    else:
        form = AcademicSessionAddForm()
    return render(request, 'academicsession/add.html',{'form':form})

##Session Edit View##  
def AcademicSessionEditView(request,id):
    session =AcademicSession.objects.get(id=id)
    form = AcademicSessionForm(instance=session)
    if request.method == 'POST':
        form = AcademicSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('academicsessionlist-view')
    context = {
        'session': session,
        'form':form
        }
    return render(request,'academicsession/edit.html',context)

##Session Delete View##
def AcademicSessionDeleteView(request,id):
    session = AcademicSession.objects.filter(id=id)
    print('2')
    if request.method == 'GET' or request.is_ajax():
        print('1')
        session.update(is_deleted=True)
        return redirect('academicsessionlist-view')
    data = {
            'status': 'Deleted Successfully',
            'status_text': 'Deleted',
            'status_icon': 'success'
            }
    '''Sending Json Data in Response'''
    return JsonResponse(data)
    

'''--------------------------------------------------------------------------------------------'''
"""USER MANAGEMENT"""
##All User List View##
def UserListView(request):
    users = User.objects.filter(is_deleted=False)
    context = {
        'users':users,
    }
    return render(request,'usermanagement/list.html',context)

##User Add View##
def UserAddView(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            try:
                un = form.cleaned_data.get('username')
                fn = form.cleaned_data.get('first_name')
                ln = form.cleaned_data.get('last_name')
                em = form.cleaned_data.get('email')
                gndr = form.cleaned_data.get('gender')
                dob = form.cleaned_data.get('dob')
                mb = form.cleaned_data.get('mobile')
                ut = form.cleaned_data.get('user_type')
                inst = form.cleaned_data.get('institute')

                '''Password Generator'''
                st =string.ascii_letters + string.digits
                all = "".join(random.sample(st,6))
                dob2=str(dob)
                ps = fn[0:3] + '@' + dob2[0:4] + all
                print(ps)
                pswd = make_password(ps)               
                user = User(username=un, first_name=fn,password=pswd,user_type=ut,
                        last_name=ln,gender=gndr, dob=dob, mobile=mb,email=em, institute=inst)
                user.save()
                subject = 'Welcome To SBTE Bihar !!!...'
                message = f'Hi {user.first_name} {user.last_name}, Please Login With Registered Email, Password {ps} and Change Your Default Password !!'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
                return redirect('userlist-view')
            except:
                return HttpResponse('Please Write valid Details !!!')
    else:
        form = UserAddForm()
    return render(request, 'usermanagement/add.html',{'form':form})

##User Edit View##
def UserEditView(request,id):
    user =User.objects.get(id=id)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            obj=form.save()
            if user.is_active == True:
                
                '''Password Generator'''
                ps = get_random_string(10)
                print(ps)
                obj.set_password(ps)
                obj.save()
                subject = 'Welcome To SBTE Bihar !!!...'
                message = f'Hi {user.first_name} {user.last_name}, Please Login With Registered Email, Password {ps} and Change Your Default Password !!'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
                return redirect('userlist-view')
            else:
                return redirect('userlist-view')          
    context = {
        'user': user,
        'form':form
        }
    return render(request,'usermanagement/edit.html',context)

##User Delete View##
def UserDeleteView(request,id):
    user = User.objects.filter(id=id)
    if request.method == 'GET' or request.is_ajax():
        user.update(is_deleted=True,is_active=False)
        return redirect('academicsessionlist-view')
    data = {
            'status': 'Deleted Successfully',
            'status_text': 'Deleted',
            'status_icon': 'success'
            }
    '''Sending Json Data in Response'''
    return JsonResponse(data)


'''--------------------------------------------------------------------------------------------'''
"""STUDENT MANAGEMENT"""
##All Student List View##
def StudentListView(request):
    student_list = Student.objects.filter(is_deleted=False)
    page = request.GET.get('page', 1)
    paginator = Paginator(student_list,9)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    context = {
        'students':students,
        'page': page,
    }
    return render(request, 'student/list.html', context)










# def index(request):
#     form = UserLoginForm
#     return render(request, "index.html",{'form':form})
# def dashboard(request):
#     return render(request,"dashboard.html")  
# def forget(request):
#     return render(request,"forget.html")
# def changepass(request):
#     return render(request,"changepass.html")
# def mark(request):
#     return render(request,"mark.html")
# def studentreg(request):  
#     return render(request,"studentreg.html") 
# def studentview(request):  
#     return render(request,"studentview.html")  
# def examschedule(request):  
#     return render(request,"examschedule.html")
# def report(request):
#     return render(request,"report.html")    
    
# def oldmark(request):
#     return render(request,"oldmark.html")    

# def editmark(request):
#    return render(request,"editmark.html")
# def individualmark(request):
#    return render(request,"individualmark.html")   
# def bulkmark(request):
#     return render(request,"bulkmark.html")
# def studentdetail(request):
#     return render(request,"studentdetail.html")
# def registrationverification(request):
#     return render(request,"registrationverification.html")
# def examform (request):
#     return render(request,"examform.html")  
# def backlogregistration (request):
#     return render(request,"backlogregistration.html")  
# def semesterregistration (request):
#     return render(request,"semesterregistration.html")
# def studentreg(request):
#     return render(request, "studentreg.html")  
# def admitcardgeneration(request):
#     return render(request,"admitcardgeneration.html")
# def examverificationnew(request):
#     return render(request,"examverificationnew.html")     
         
#  def newmark(request):
#     return render(request,"newmark.html") 