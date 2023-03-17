from django.db import models
from django.utils import timezone
from django.contrib.auth. models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager
      
        
USER_TYPE_CHOICES = (
        ('A','ADMIN'),
        ('IA','INSTITUTE ADMIN'),
        ('IS','INSTITUTE STAFF'),
        ('ST','STAFF'),
        ('AC','ACCOUNT'),
        
    )

GENDER_TYPE_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O","Others"),
    )

"""CUSTOM USER MANAGER"""
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, password, is_superuser, is_admin,**extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Email id is required')
        email = self.normalize_email(email)
        if is_superuser:
            user = self.model(email=email, username=username, is_superuser=True,is_admin=True,user_type=USER_TYPE_CHOICES[0][0],
                              is_staff=True, **extra_fields)
         
        else:
            user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(force_insert=True)
        return user
    
    ### NORMAL USER FUNCTION ###
    def create_user(self, email, username, password=None, **extra_fields):
        user = self._create_user(email, username, password, False, False,**extra_fields)
        user.save()
        return user
    
    ### SUPER USER FUNCTION ###
    def create_superuser(self, email, username, password, **extra_fields):
        user = self._create_user(email, username, password, True,True, **extra_fields)
        return user


"""ALL USER MODEL"""
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50,blank=False, null=False)
    last_name = models.CharField(max_length=50,blank=False, null=False)
    username = models.CharField(max_length=50)
    user_type = models.CharField(choices=USER_TYPE_CHOICES,default=USER_TYPE_CHOICES[2][0],max_length=2)
    email = models.EmailField(_('email'),unique=True)
    is_staff = models.BooleanField(default=False)
    is_passupdated = models.BooleanField(default=False,blank=False,null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    reg_date_time = models.DateTimeField(default = timezone.now)
    date_joined = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_TYPE_CHOICES, blank=False, null=True)
    dob = models.DateField(max_length=255,blank=False, null=True)
    last_login = models.DateTimeField(_('last login'), default=timezone.now,blank=False, null=True)
    is_deleted = models.BooleanField(default=False,blank=False,null=False)
    modified_by = models.CharField(max_length=255, blank=False, null=True)
    modified_date = models.DateTimeField(max_length=255,blank=False, null=True)
    remarks = models.CharField(max_length=255, blank=False, null=True)
    mobile = models.CharField(max_length=10, blank=False, null=True)
    institute = models.ForeignKey('Institute', models.DO_NOTHING, blank=True, null=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def __str__(self):
        
        return self.username +", "+'User Type: '+ self.user_type
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label ):
        return True
    
    class Meta:
        managed = True
        db_table = 'user'

"""ADMIN MODEL"""  
class AdminHod(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_type = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=False, null=True)
    objects = CustomUserManager()
    
    class Meta:
        db_table = 'adminhod'
        
"""INSTITUTE MODEL"""   
class Institute(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    is_deleted = models.BooleanField(default=False,blank=False,null=False)  # This field type is a guess.
    is_active = models.BooleanField(default=True,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=255, blank=False, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255)
    is_marksentry = models.BooleanField(default=False,blank=False,null=False)
    objects = CustomUserManager()

    class Meta:
        managed = True
        db_table = 'institute'          
    
    def __str__(self):
        return self.name  
   
"""PROGRAM MODEL"""
class Program(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255, blank=False, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False,blank=False,null=False)
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255)
    objects = CustomUserManager()
    class Meta:
        managed = True
        db_table = 'program'
        
    def __str__(self):
        return self.name       

"""ACADEMIC SESSION MODEL"""  
class AcademicSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    for_le = models.BooleanField(default=False,blank=False,null=False)
    is_current = models.BooleanField(default=True,blank=False,null=False)
    is_deleted = models.BooleanField(default=False,blank=False,null=False)
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    objects = CustomUserManager()
    class Meta:
        managed = True
        db_table = 'academic_session'  
        
    def __str__(self):
        return self.name      

"""STUDENT USER MODEL"""
class Student(models.Model):
    id = models.BigIntegerField(primary_key=True) # here i have added primary_key = True
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False,blank=False,null=False)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    aadhar_number = models.CharField(max_length=255, blank=True, null=True)
    admission_type = models.CharField(max_length=255, blank=True, null=True)
    bcece = models.BigIntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    category_admission = models.CharField(max_length=255, blank=True, null=True)
    class_roll_no = models.BigIntegerField(blank=True, null=True)
    comm_city = models.CharField(max_length=255, blank=True, null=True)
    comm_country = models.CharField(max_length=255, blank=True, null=True)
    comm_line1 = models.CharField(max_length=255, blank=True, null=True)
    comm_line2 = models.CharField(max_length=255, blank=True, null=True)
    comm_pin = models.CharField(max_length=6, blank=True, null=True)
    comm_state = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    doj = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    is_iti = models.BooleanField(default=False,blank=False,null=False)
    is_rec = models.BooleanField(default=False,blank=False,null=False)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    perm_city = models.CharField(max_length=255, blank=True, null=True)
    perm_country = models.CharField(max_length=255, blank=True, null=True)
    perm_line1 = models.CharField(max_length=255, blank=True, null=True)
    perm_line2 = models.CharField(max_length=255, blank=True, null=True)
    perm_pin = models.CharField(max_length=6, blank=True, null=True)
    perm_state = models.CharField(max_length=255, blank=True, null=True)
    reg_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    reg_no = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=False, null=False)
    academic_session = models.BigIntegerField(blank=True, null=True)
    institute = models.BigIntegerField()
    program = models.BigIntegerField()
    is_issued = models.BooleanField(default=False,blank=False,null=False)
    is_provisional = models.BooleanField(default=False,blank=False,null=False)
    is_registered = models.BooleanField(default=False,blank=False,null=False)
    is_new = models.BooleanField(default=False,blank=False,null=False)
    bcece_roll_no = models.BigIntegerField(blank=True, null=True)
    PaymentStatus = models.BooleanField(default=False,blank=False,null=False)
    objects = CustomUserManager()
    
    class Meta:
        managed = False
        db_table = 'student'
        
    def __str__(self):
        return self.first_name 
        
        
"""EXAMS TABLE"""
class Exams(models.Model):
    id = models.BigAutoField(primary_key=True)
    academic_term = models.CharField(max_length=255)
    exam_held = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(default=False,blank=False,null=False)
    is_current = models.BooleanField(default=True,blank=False,null=False)
    term = models.CharField(max_length=255, blank=True, null=True)
    objects = CustomUserManager()

    class Meta:
        managed = False
        db_table = 'exams'   
    def __str__(self):
        return self.academic_term 


"""COURSELE TABLE"""
class CourseLe(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    full_mark = models.IntegerField()
    is_deleted = models.BooleanField(default=False,blank=False,null=False)
    name = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course_le'

    def __str__(self):
        return self.name 





