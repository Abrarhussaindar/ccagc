# from asyncio.windows_events import NULL
from django import forms
# from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateStudent(UserCreationForm):
    class Meta:
        model = Student
        fields = ('first_name', 'middle_name', 'last_name','roll_number', 'application_number', 'uid', 'section', 'dob', 'course', 'admitted_through', 'applied_year', 'address', 'city', 'state', 'country', 'email', 'password1', 'password2')

CHOICES = [('M','Male'),('F','Female'),('O','Other')]

class PersonalForm(forms.ModelForm):
    Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    class Meta:
        model = Stu_Personal
        # 'first_name', 'middle_name', 'last_name', 'dob', 'gender', 'roll_number', 'phone_number','school', 'university_mail_id', 'course', 'semester', 'section', 'hobbies','why_ccagc', 'career_goals','hopes','barries', 'ambition', 'permanent_address', 'current_address'
        fields = ('__all__')

class AcadamicForm(forms.ModelForm):
    class Meta:
        model = Stu_Acadamic
        # 'first_name', 'middle_name', 'last_name', 'dob', 'gender', 'roll_number', 'phone_number','school', 'university_mail_id', 'course', 'semester', 'section', 'hobbies','why_ccagc', 'career_goals','hopes','barries', 'ambition', 'permanent_address', 'current_address'
        fields = ('__all__')

class CareerForm(forms.ModelForm):
    class Meta:
        model = Stu_career
        # 'first_name', 'middle_name', 'last_name', 'dob', 'gender', 'roll_number', 'phone_number','school', 'university_mail_id', 'course', 'semester', 'section', 'hobbies','why_ccagc', 'career_goals','hopes','barries', 'ambition', 'permanent_address', 'current_address'
        fields = ('__all__')
CHOICE = [
        ('Drop-In', 'Drop-In'),
        ('Scheduled', 'Scheduled'),
    ]
class FeedbackFormone(forms.ModelForm):
    type_of_counselling_session = forms.CharField(label='Type of counselling session', widget=forms.RadioSelect(choices=CHOICE))
    # beneficial = .CharField(='The meeting was beneficial in achieving my immediate goal (s)')
    class Meta:
        model = FeedbackFormFieldsPartOne
        # 'counselor_name', 'type_of_counselling_session', 'beneficial', 'Information', 'address_my_concerns', 'valuable', 'genuine_interest', 'knowledgeable', 'examine_my_alternatives', 'like', 'dislike', 'changes'
        fields = ('__all__')
CHOICES = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
class FeedbackFormtwo(forms.ModelForm):
    beneficial = forms.CharField(label='The meeting was beneficial in achieving my immediate goal (s)', widget=forms.RadioSelect(choices=CHOICES))
    # beneficial = models.BooleanField(label='The meeting was beneficial in achieving my immediate goal (s)')
    Information = forms.BooleanField(label='Information was thoroughly and clearly explained.',widget=forms.RadioSelect(choices=CHOICES)) 
    address_my_concerns = forms.BooleanField(label='There was enough time to address my concerns.',widget=forms.RadioSelect(choices=CHOICES)) 
    valuable = forms.BooleanField(label='Session will be valuable to me in completing my academic and career',widget=forms.RadioSelect(choices=CHOICES))
    genuine_interest = forms.BooleanField(label='Counselor showed genuine interest in assisting me.',widget=forms.RadioSelect(choices=CHOICES))
    knowledgeable = forms.BooleanField(label='Counselor was knowledgeable and prepared for the session',widget=forms.RadioSelect(choices=CHOICES))
    examine_my_alternatives = forms.BooleanField(label='Counselor helped me to consider options and examine my alternatives',widget=forms.RadioSelect(choices=CHOICES))
    
    class Meta:
        model = FeedbackFormFieldsParttwo
        # 'counselor_name', 'type_of_counselling_session', 'beneficial', 'Information', 'address_my_concerns', 'valuable', 'genuine_interest', 'knowledgeable', 'examine_my_alternatives', 'like', 'dislike', 'changes'
        fields = ('__all__')

class FeedbackFormthree(forms.ModelForm):
    class Meta:
        model = FeedbackFormFieldsPartthree
        # 'counselor_name', 'type_of_counselling_session', 'beneficial', 'Information', 'address_my_concerns', 'valuable', 'genuine_interest', 'knowledgeable', 'examine_my_alternatives', 'like', 'dislike', 'changes'
        fields = ('__all__')