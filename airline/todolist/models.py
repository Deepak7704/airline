from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.

class User(AbstractUser):
        groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change the related name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
        user_permissions = models.ManyToManyField(
            Permission,
            related_name='custom_user_set',  # Change the related name to avoid conflict
            blank=True,
            help_text='Specific permissions for this user.',
            verbose_name='user permissions',
        )

class Goals(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="user_goals")
    title=models.CharField(max_length=90)
    goal=models.CharField(max_length=500)


    def __str__(self):
        return f"{self.goal} - {self.user}"
    
class Tasks(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="user_tasks")
    tasks=models.CharField(max_length=120)

    def __str__ (self):
        return f"{self.Tasks} - {self.user}"