from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class loan(models.Model):
    user = models.OneToOneField(User,null=True)
    fullname = models.CharField(max_length=128, blank=True)
    phone = models.IntegerField(default=0)
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
    )
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES, blank=True)
    STATE_CHOICES = (
            ('Delhi', 'Delhi'),
            ('Karnataka', 'Karnataka'),
            ('Andhra', 'Andhra'),
            ('Telangana', 'Telangana'),
    )
    select_state=models.CharField(max_length=10,choices=STATE_CHOICES, blank=True)
    enter_city=models.CharField(max_length=100,blank=True)
    EMP_CHOICES = (
            ('Salaried', 'Salaried'),
            ('Self', 'Self'),
    )
    employee_type=models.CharField(max_length=10,choices=EMP_CHOICES, blank=True)
    monthly_salary = models.IntegerField(default='')
    SALARY_CHOICES = (
            ('Cash', 'Cash'),
            ('Bank Transor', 'Bank Transor'),
            ('Cheque', 'Cheque'),
    )
    salary_mode=models.CharField(max_length=10,choices=SALARY_CHOICES, blank=True)
    upload_bankstatement = models.FileField(upload_to='media/pdf/',help_text='Last 3 months payslips', null=True, blank=True)
    upload_aadhar = models.FileField(upload_to='media/aadhar/', null=True, blank=True)
    upload_pan = models.FileField(upload_to='media/pan/', null=True, blank=True)

    def __str__(self):
       return self.fullname
