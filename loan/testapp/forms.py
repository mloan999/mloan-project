from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from testapp.models import loan



class UserForm(forms.ModelForm):

     class Meta():
        model = User
        fields = ('first_name','last_name','email')
     def clean_email(self):
        email = self.cleaned_data.get('email')
        # username = self.cleaned_data.get('username')
        # if email and User.objects.filter(email=email).exclude(username=username).exists():
        #     raise forms.ValidationError(u'Email addresses must be unique.')
        # return email


class loanform(forms.ModelForm):

     class Meta():
        model = loan
        fields = ('fullname','phone','gender','select_state','enter_city','employee_type','monthly_salary','salary_mode','upload_bankstatement','upload_aadhar','upload_pan')
