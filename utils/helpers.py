from django.core.mail import send_mail
import uuid
from django.conf import settings
import random
import string



'''Forget password'''
def send_forget_password_email(email, token):
    subject = 'Your forget password link !!'
    message = f'Hi, click on the link to reset your password http://127.0.0.1.8000/changepassword/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

'''Password Generator'''
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase +string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


'''Queryset Report Table'''
def tableStruc(ModelObj, fields_names):
	table = []
	for value in ModelObj.values():
		t=[]
		for i in range(len(fields_names)):
			t.append(value['{}'.format(fields_names[i])])
		table.append(t)
	return table

def customQuerysetReportTable(ModelObj, customModelFields=[]):
	fields_names = customModelFields
	return tableStruc(ModelObj,fields_names)