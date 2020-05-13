from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from testapp.models import Userprofile



class signupform(forms.ModelForm):
    name=forms.CharField(max_length=25)
    username=forms.CharField(max_length=25)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Re Enter Password',widget=forms.PasswordInput)
    phone = forms.IntegerField()
    # rpassword=forms.CharField(label='Re Enter Password',widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)
    location = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(required=True)
    # email = forms.EmailField(max_length=60, help_text='Required. Inform a valid email address.')
    # date_of_birth= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
    # date_of_birth =  forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)
    # date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'),
    #                            input_formats=('%d/%m/%Y',),
    #                            required=False)
    date_of_birth=forms.DateTimeField(help_text='DD/MM/YYYY H:M',input_formats=['%d/%m/%Y %H:%M'])
    # gender = forms.CharField(max_length=10, required=True)
    age = forms.IntegerField()
    comments = forms.CharField(max_length=500, help_text="Comments: ", required=False)
    photo = forms.ImageField(help_text="Upload image: ", required=False)
    # bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)





    class Meta:
        model=Userprofile
        fields=('username','password','rpassword','phone','first_name','last_name','location','caste','date_of_birth','email','gender','age','comments','photo')

    def __str__(self):
       return self.username
#

#
#
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username','password','email')
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model=UserProfile
#         fields=('nickname',)
#
# def clean(self):
#         print('validating passwords match...')
#         total_cleaned_data=super().clean()
#         fpwd=total_cleaned_data['password']
#         spwd=total_cleaned_data['rpassword']
#         if fpwd != spwd:
#              raise forms.ValidationError('Both passwords must be matched')
#         bot_handler_value=total_cleaned_data['bot_handler']
#         if len(bot_handler_value)>0:
#             raise forms.ValidationError('Request from BOT...cannot be submitted!!!')
