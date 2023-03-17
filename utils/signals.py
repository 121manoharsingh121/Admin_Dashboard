from django.dispatch import receiver
from django.db.models.signals import post_save
from sbte.models import User,Admin,R

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.role==1:
            Admin.objects.create(user=instance)
        
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    if instance.role==1:
        instance.admin.save()
    