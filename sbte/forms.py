from django import forms
from sbte.models import User, Institute, Program, AcademicSession
from django.core.exceptions import ValidationError  
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm



"""USER SIGNUP FORM"""
class UserRegisterationForm(UserCreationForm):
    password1 = forms.CharField(required=True,widget=forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your password', "autocomplete":"off"}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm your password', "autocomplete":"off"}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your email address', "autocomplete":"off"}))
	
    class Meta:
        model = User
        fields = ('username','email','mobile','dob','password1', 'password2','first_name','last_name')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Username', "autocomplete":"off"}),
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter first name', "autocomplete":"off"}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter last Name', "autocomplete":"off"}),
            'email':forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your email address', "autocomplete":"off"}),
            'mobile':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your mobile number', "autocomplete":"off"}),
            'dob':forms.DateInput(format = '%Y-%m-%d',attrs={'class':'form-control form-control-lg', 'placeholder': 'Select a date', 'type': 'date', "autocomplete":"off" }),
            'password1':forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your password', "autocomplete":"off"}),
            'password2':forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm your password', "autocomplete":"off"}),
        }
        
    def save(self, commit=True):
        user = super(UserRegisterationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

"""USER SIGNIN FORM"""    
class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=30, 
                            widget=forms.EmailInput(
                            attrs={'class':'form-control form-control-sm', 'placeholder':'Enter your Email', "autocomplete":"off"})
                            )
    password = forms.CharField(max_length=30, 
                            widget=forms.PasswordInput(
                            attrs={'class':'form-control form-control-sm', 'placeholder':'Enter your password', "autocomplete":"off"})
                            )

"""USER PASSWORD CHANGE FORM""" 
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(required=True,widget=forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your password', "autocomplete":"off"}))
    new_password1 = forms.CharField(required=True,widget=forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your password', "autocomplete":"off"}))
    new_password2 = forms.CharField(required=True,widget=forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm your password', "autocomplete":"off"}))
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')
        widgets = {
            'old_password':forms.PasswordInput( attrs={'class':'form-control form-control-sm', 'placeholder':'Enter your password', "autocomplete":"off"}),
            'new_password1':forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your password', "autocomplete":"off"}),
            'new_password2':forms.PasswordInput( attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm your password', "autocomplete":"off"}) 
        }

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username', 'mobile', 'dob', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]

'''CHOICES YES/NO'''
YES_NO_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

'''CHOICES ACTIVE/INACTIVE'''
ACTIVE_INACTIVE_CHOICES = (
    (True, 'Active'),
    (False, 'InActive')
)

## INSTITUTE MANAGEMENT ##        
"""INSTITUTE ADD FORM"""        
class InstituteAddForm(forms.ModelForm):
    is_active = forms.ChoiceField(choices = ACTIVE_INACTIVE_CHOICES, label="Status", 
                widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
    is_marksentry = forms.ChoiceField(choices = YES_NO_CHOICES, 
            widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
 
    class Meta:
        model = Institute
        fields = ('code','name','short_name','is_active','is_marksentry')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter the institute name', "autocomplete":"off"}),
            'code':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter the institute code', "autocomplete":"off"}),
            'short_name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter the institute short name', "autocomplete":"off"}),
            
        }
    
    def clean(self):
        cleaned_data = super(InstituteAddForm, self).clean()
        code = cleaned_data.get("code")
        if not code.isnumeric():
            raise ValidationError("Institute code must be an integer !!!")
        return cleaned_data

"""INSTITUTE EDIT FORM"""
class InstituteForm(forms.ModelForm):
    is_active = forms.ChoiceField(choices = ACTIVE_INACTIVE_CHOICES, label="Status", 
                widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
    is_marksentry = forms.ChoiceField(choices = YES_NO_CHOICES, 
            widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))

    class Meta:
        model = Institute
        fields = ('code','name','short_name','is_active','remarks','is_marksentry')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter the institute name', "autocomplete":"off"}),
            'code':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter the institute code', "autocomplete":"off"}),
            'short_name':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter the institute short name', "autocomplete":"off"}),
            'remarks':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Remarks', "autocomplete":"off"}),
        }
        
    def clean(self):
        cleaned_data = super(InstituteForm, self).clean()
        code = cleaned_data.get("code")
        if not code.isnumeric():
            raise ValidationError("Institute code must be an integer !!!")
        return cleaned_data    




## PROGRAM MANAGEMENT ##
"""PROGRAM ADD FORM""" 
class ProgramAddForm(forms.ModelForm):
    is_active = forms.ChoiceField(choices = ACTIVE_INACTIVE_CHOICES, label="Status", 
                widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
    class Meta:
        model = Program
        fields = ('code','name','short_name','is_active')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter the program name', "autocomplete":"off"}),
            'code':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter the program code', "autocomplete":"off"}),
            'short_name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter the program short name', "autocomplete":"off"}),
        }
        
    def clean(self):
        cleaned_data = super(ProgramAddForm, self).clean()
        code = cleaned_data.get("code")
        if not code.isnumeric():
            raise ValidationError("Program code must be an integer !!!")
        return cleaned_data    
        
"""PROGRAM EDIT FORM"""
class ProgramForm(forms.ModelForm):
    is_active = forms.ChoiceField(choices = ACTIVE_INACTIVE_CHOICES, label="Status", 
                widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
    
    class Meta:
        model = Program
        fields = ('code','name','short_name','is_active','remarks')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter the institute name', "autocomplete":"off"}),
            'code':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter the institute code', "autocomplete":"off"}),
            'short_name':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter the institute short name', "autocomplete":"off"}),
            'remarks':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Remarks', "autocomplete":"off"}),
        }        

    def clean(self):
        cleaned_data = super(ProgramForm, self).clean()
        code = cleaned_data.get("code")
        if not code.isnumeric():
            raise ValidationError("Program code must be an integer !!!")
        return cleaned_data




## ACADEMIC SESSION MANAGEMENT ##
"""ACADEMIC SESSION ADD FORM"""
class AcademicSessionAddForm(forms.ModelForm):
    class Meta:
        model = AcademicSession
        fields = ('name','remarks',)
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter the session name', "autocomplete":"off"}),
            'remarks':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Remarks', "autocomplete":"off"}),
        } 
    # def clean(self):
    #     cleaned_data = super(ProgramForm, self).clean()
    #     code = cleaned_data.get("code")
    #     if not code.isnumeric():
    #         raise ValidationError("Program code must be an integer !!!")
    #     return cleaned_data

"""ACADEMIC SESSION EDIT FORM"""
class AcademicSessionForm(forms.ModelForm):
    for_le = forms.ChoiceField(choices = YES_NO_CHOICES, 
            widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
    class Meta:
        model = AcademicSession
        fields = ('name','remarks','for_le',)
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter the session name', "autocomplete":"off"}),
            'remarks':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Remarks', "autocomplete":"off"}),
        } 
    # def clean(self):
    #     cleaned_data = super(ProgramForm, self).clean()
    #     code = cleaned_data.get("code")
    #     if not code.isnumeric():
    #         raise ValidationError("Program code must be an integer !!!")
    #     return cleaned_data            



## USER MANAGEMENT ##
"""USER ADD FORM"""
class UserAddForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ('username','email','mobile','dob','user_type','gender','first_name','last_name','institute')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Username', "autocomplete":"off"}),
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter first name', "autocomplete":"off"}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter last Name', "autocomplete":"off"}),
            'email':forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your email address', "autocomplete":"off"}),
            'mobile':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your mobile number', "autocomplete":"off"}),
            'dob':forms.DateInput(format = '%Y-%m-%d',attrs={'class':'form-control form-control-lg', 'placeholder': 'Select a date', 'type': 'date', "autocomplete":"off" }),
            'user_type':forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}),
            'gender':forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}),
            'institute':forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}),
        }

"""USER EDIT FORM"""      
class UserForm(forms.ModelForm):
    is_active = forms.ChoiceField(choices = ACTIVE_INACTIVE_CHOICES, 
                widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
    is_admin = forms.ChoiceField(choices = YES_NO_CHOICES, 
                widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
    is_staff = forms.ChoiceField(choices = YES_NO_CHOICES, 
                widget=forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}))
   
    class Meta:
        model = User
        fields = ('username','first_name','last_name','is_active','is_staff',
                 'dob','gender','remarks','is_admin','user_type','email','mobile')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Username', "autocomplete":"off"}),
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter first name', "autocomplete":"off"}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter last Name', "autocomplete":"off"}),
            'email':forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your email address', "autocomplete":"off"}),
            'user_type':forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}),
            'remarks':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Remarks', "autocomplete":"off"}),
            'dob':forms.DateInput(format = '%Y-%m-%d',attrs={'class':'form-control form-control-lg', 'placeholder': 'Select a date', 'type': 'date', "autocomplete":"off" }),
            'gender':forms.Select(attrs={'class':'form-control form-control-sm',"autocomplete":"off"}),
            'mobile':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your mobile number', "autocomplete":"off"}),
        } 
        

        