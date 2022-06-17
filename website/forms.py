# from asyncio.windows_events import NULL
from django import forms
# from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateStudent(UserCreationForm):
    class Meta:
        model = Student
        fields = ('first_name', 'middle_name', 'last_name','roll_number', 'application_number', 'uid', 'section', 'dob', 'course', 'admitted_through', 'applied_year', 'address', 'city', 'state', 'country', 'email', 'password1', 'password2')


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Stu_Register
        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'gender', 'roll_number', 'phone_number','school', 'university_mail_id', 'course', 'semester', 'section', 'hobbies','why_ccagc', 'career_goals','hopes','barries', 'ambition', 'permanent_address', 'current_address')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackFormFields
        fields = ('counselor_name', 'type_of_counselling_session', 'beneficial', 'Information', 'address_my_concerns', 'valuable', 'genuine_interest', 'knowledgeable', 'examine_my_alternatives', 'like', 'dislike', 'changes')
