# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def set_default_password(sender, instance, created, **kwargs):
#     # Set the default password if a new user is created
#     if created and not instance.password:
#         instance.set_password('testing321')
#         instance.save()