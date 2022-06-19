# from asyncio.windows_events import NULL
from django import forms
# from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateStudent(UserCreationForm):
    class Meta:
        model = Student
        fields = ('first_name', 'middle_name', 'last_name','roll_number', 'application_number', 'uid', 'section', 'dob', 'course', 'admitted_through', 'applied_year', 'address', 'city', 'state', 'country', 'email', 'password1', 'password2')


class PersonalForm(forms.ModelForm):
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

class FeedbackFormone(forms.ModelForm):
    class Meta:
        model = FeedbackFormFieldsPartOne
        # 'counselor_name', 'type_of_counselling_session', 'beneficial', 'Information', 'address_my_concerns', 'valuable', 'genuine_interest', 'knowledgeable', 'examine_my_alternatives', 'like', 'dislike', 'changes'
        fields = ('__all__')

class FeedbackFormtwo(forms.ModelForm):
    class Meta:
        model = FeedbackFormFieldsParttwo
        # 'counselor_name', 'type_of_counselling_session', 'beneficial', 'Information', 'address_my_concerns', 'valuable', 'genuine_interest', 'knowledgeable', 'examine_my_alternatives', 'like', 'dislike', 'changes'
        fields = ('__all__')

class FeedbackFormthree(forms.ModelForm):
    class Meta:
        model = FeedbackFormFieldsPartthree
        # 'counselor_name', 'type_of_counselling_session', 'beneficial', 'Information', 'address_my_concerns', 'valuable', 'genuine_interest', 'knowledgeable', 'examine_my_alternatives', 'like', 'dislike', 'changes'
        fields = ('__all__')