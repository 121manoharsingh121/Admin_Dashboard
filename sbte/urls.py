from django.contrib import admin
from django.urls import path
from views import views
from sbte import Adminviews ,Instituteviews, Studentviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView,name="home-view"),
    path('login/', views.UserLoginView, name="login-view"),
    path('registration/', views.UserSignUpView, name="registration-view"),
    path('logout/', views.UserLogoutView, name="logout-view"),
    path('changepassword/<int:id>', views.UserChangePasswordView, name='changepassword-view'),
    path('passwordreset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('passwordreset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('report/', Adminviews.TabularReportView, name='report-view'),
# '''--------------------------------------------------------------------------------------------'''
    ## URL for Admin ##
    path('admin_dashboard/', Adminviews.DashboardView, name="admindashboard-view"),
    
    
# '''--------------------------------------------------------------------------------------------'''
    ## URL for User Management ##
    path('userlist/', Adminviews.UserListView, name="userlist-view"),
    path('useradd/', Adminviews.UserAddView, name="useradd-view"),
    path('useredit/<int:id>', Adminviews.UserEditView, name="useredit-view"),
    path('userdelete/<int:id>', Adminviews.UserDeleteView, name="userdelete-view"),
    
    
# '''--------------------------------------------------------------------------------------------'''
    ## URL for Institute Management ##
    path('institute_list/', Adminviews.InstituteListView, name="institutelist-view"),
    path('institute_add/', Adminviews.InstituteAddView, name="instituteadd-view"),
    path('institute_edit/<int:id>', Adminviews.InstituteEditView, name="instituteedit-view"),
    path('institute_delete/<int:id>', Adminviews.InstituteDeleteView, name="institutedelete-view"),
    
    
# '''--------------------------------------------------------------------------------------------'''
    ## URL for Program Management ##
    path('program_list/', Adminviews.ProgramListView, name="programlist-view"),
    path('program_add/', Adminviews.ProgramAddView, name="programadd-view"),
    path('program_edit/<int:id>', Adminviews.ProgramEditView, name="programedit-view"),
    path('program_delete/<int:id>', Adminviews.ProgramDeleteView, name="programdelete-view"),
    
    
# '''--------------------------------------------------------------------------------------------'''
    ## URL for Academic Session Management ##
    path('academicsessionlist/', Adminviews.AcademicSessionListView, name="academicsessionlist-view"),
    path('academicsessionadd/', Adminviews.AcademicSessionAddView, name="academicsessionadd-view"),
    path('academicsessionedit/<int:id>', Adminviews.AcademicSessionEditView, name="academicsessionedit-view"),
    path('academicsessiondelete/<int:id>', Adminviews.AcademicSessionDeleteView, name="academicsessiondelete-view"),
    
    
# '''--------------------------------------------------------------------------------------------'''
    ## URL for Student Management ##
    path('studentlistview/',Adminviews.StudentListView,name="studentlist-view"),

    ##URL for Student ##
    path('student_dashboard/', Studentviews.StudentDashboardView, name="studentdashboard-view"),
    
    ##URL for Institute ##
    path('institute_dashboard/', Instituteviews.InstituteDashboardView, name="institutedashboard-view"),
    ]














#     
#     path('studentreg/',views.studentreg,name="studentreg"),
#     path('/forget/',views.forget,name="forget"),
#     path('mark/',views.mark,name="mark"),
#     
#     path('examschedule/',views.examschedule,name="examschedule"),
#     path('report/', views.report,name="report"),

#     path('oldmark/', views.oldmark,name="oldmark"),
#     path('editmark/',views.editmark,name="editmark"),
#     path('individualmark/', views.individualmark,name="individualmark"),
#     path('bulkmark/', views.bulkmark,name="bulkmark"),
#     path('studentdetail/', views.studentdetail,name="studentdetail"),
#     path('registrationverification/',views.registrationverification,name="registrationverification"),
#     path('examform/',views.examform,name="examform"),
#     path('backlogregistration/',views.backlogregistration,name="backlogregistration"),
#     path('semesterregistration/',views.semesterregistration,name="semesterregistration"),
     
#     path('admitcardgeneration/',views.admitcardgeneration,name="admitcardgeneration"),
#     path('examverificationnew/',views.examverificationnew,name="examverificationnew"),
