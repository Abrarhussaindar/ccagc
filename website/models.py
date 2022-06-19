from email.mime import application
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import random

from django.db.models.expressions import Value
from requests import session

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, roll_number, email,first_name, middle_name, last_name, phone_number,application_number, uid, section, dob, course, admitted_through, applied_year, address, city, state, country, alternate_address, house_number, pincode, password=None):

        user=self.model(
            email=self.normalize_email(email),
            roll_number = roll_number,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            phone_number = phone_number,
            
            application_number = application_number,
            uid = uid,
            section = section,
            dob = dob,
            course = course,
            admitted_through = admitted_through,
            applied_year = applied_year,

            address = address,
            city = city,
            state = state,
            country = country,
            alternate_address = alternate_address,
            house_number = house_number,
            picode = pincode,
            # password = password,
#             # alternative_phone_number = alternative_phone_number,
#             # address = address,
#             # city = city,
#             # state=state,
#             # country = country,
#             # alternate_address = alternate_address,
#             # house_number = house_number,
#             # pincode = pincode
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,roll_number, email, first_name, middle_name, last_name, phone_number, password=None):
        user=self.create_user(
            email=email,
            roll_number = roll_number,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            phone_number = phone_number,
            password=password,
            # application_number= application_number,

        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class Student(AbstractBaseUser):
    first_name = models.CharField(verbose_name='First Name', max_length=200, null=True)
    middle_name = models.CharField(verbose_name='Middle Name', max_length=200, null=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=200, null=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=10, null=True)
    # alternative_phone_number = models.CharField(verbose_name='alternative_phone_number', max_length=10, null=True)
    roll_number = models.CharField(verbose_name='Roll Number', max_length=20, null=True, unique=True)
    application_number = models.CharField(verbose_name='Registration Number', max_length=20, null=True, unique=True)
    uid = models.CharField(verbose_name='UID', max_length=20, null=True)
    section = models.CharField(verbose_name='Section', max_length=20, null=True)
    dob = models.DateField(verbose_name='Date Of Birth', max_length=20, null=True)
    course = models.CharField(verbose_name='Course', max_length=200, null=True)
    admitted_through = models.CharField(verbose_name='Admitted Through', max_length=200, null=True)
    applied_year = models.CharField(verbose_name='Applied Year', max_length=20, null=True)
    address = models.CharField(verbose_name='address', max_length=500, null=True)
    city = models.CharField(verbose_name='city', max_length=200, null=True)
    state = models.CharField(verbose_name='state', max_length=200, null=True)
    country = models.CharField(verbose_name='country', max_length=100, null=True)
    alternate_address = models.CharField(verbose_name='alternate_address', max_length=500, null=True)
    house_number = models.CharField(verbose_name='house_number', max_length=5, null=True)
    pincode = models.CharField(verbose_name='pincode', max_length=10, null=True)

    email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)



    USERNAME_FIELD = 'roll_number'
    # # REQUIRED_FIELDS = ['first_name']
    REQUIRED_FIELDS = ['first_name','middle_name', 'last_name', 'phone_number', 'email']

    objects = MyUserManager()

    def __str__(self):
        return self.roll_number


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

Gender = (
    ('None', 'None'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
Choices = (
    ('None', 'None'),
    ('Placements', 'Placements'),
    ('Higher Studies', 'Higher Studies'),
    ('Enterpreneurship', 'Enterpreneurship'),
    ('Other', 'Other'),
)

School = (
    ('None','None'),
    ('School Of Engineering', 'School Of Engineering'),
    ('School Of Law', 'School Of Law'),
    ('School Of Desiging', 'School Of Desiging'),
    ('School Of Management', 'School Of Management'),
)

class Stu_Personal(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=200, null=True)
    middle_name = models.CharField(verbose_name='Middle Name', max_length=200, null=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=200, null=True)
    gender = models.CharField(verbose_name='Gender',max_length=20, null=True)
    dob = models.DateField(verbose_name='Date Of Birth', max_length=20, null=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=10, null=True)
    

    def __str__(self):
        return self.first_name + self.middle_name + self.last_name
# current_address = models.CharField(verbose_name='Current Address', max_length=600, null=True)
# permanent_address = models.CharField(verbose_name='Permanent Address', max_length=600, null=True)

class Stu_Acadamic(models.Model):
    roll_number = models.CharField(verbose_name='Roll Number', max_length=20, null=True, unique=True)
    section = models.CharField(verbose_name='Section',max_length=20)
    semester = models.CharField(verbose_name='Semester', max_length=20, null=True)
    university_mail_id = models.CharField(verbose_name='Mail Id', max_length=100, null=True, unique=True)
    course = models.CharField(verbose_name='Course', max_length=50, null=True)
    school = models.CharField(verbose_name='School',max_length=100, default="None", choices=School)
    
    def __str__(self):
        return self.roll_number
    
class Stu_career(models.Model):
    ambition = models.TextField(verbose_name='Ambition', max_length=1500, null=True)
    hobbies = models.TextField(verbose_name='hobbies', max_length=500, null=True)
    why_ccagc = models.CharField(verbose_name='You are looking Career counselling and Guidance for', max_length=50, default="None", choices=Choices)
    career_goals = models.TextField(verbose_name='What are your current career goals? (Even if you are uncertain/, fill in any thoughts you might have)/,', max_length=5000, null=True)
    hopes = models.TextField(verbose_name='What are you hoping for from Career counselling and Guidance Cell?', max_length=5000, null=True)
    barries = models.TextField(verbose_name='What kinds of barriers do you think could get in the way of you pursuing the career you want, or meeting your career goals?', max_length=5000, null=True)

sessio = (
    ('Drop-In', 'Drop-In'),
    ('Scheduled', 'Scheduled'),
)

scale = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)
class FeedbackFormFieldsPartOne(models.Model):
    counselor_name = models.CharField(verbose_name='Counselor Name', max_length=100, null=True)
    type_of_counselling_session = models.CharField(verbose_name='Type of counselling session', max_length=30, choices=sessio)

    def __str__(self):
        return self.counselor_name


class FeedbackFormFieldsParttwo(models.Model):
    beneficial = models.BooleanField(verbose_name='The meeting was beneficial in achieving my immediate goal (s)',choices=scale) 
    Information = models.BooleanField(verbose_name='Information was thoroughly and clearly explained.',choices=scale) 
    address_my_concerns = models.BooleanField(verbose_name='There was enough time to address my concerns.',choices=scale) 
    valuable = models.BooleanField(verbose_name='The session will be valuable to me in completing my academic, career and/or personal goals',choices=scale)
    genuine_interest = models.BooleanField(verbose_name='Counselor showed genuine interest in assisting me.',choices=scale)
    knowledgeable = models.BooleanField(verbose_name='Counselor was knowledgeable and prepared for the session',choices=scale)
    examine_my_alternatives = models.BooleanField(verbose_name='Counselor helped me to consider options and examine my alternatives',choices=scale)
    
class FeedbackFormFieldsPartthree(models.Model):
    like = models.TextField(verbose_name='What did you like about this counselling session?', max_length=500, default=None)
    dislike = models.TextField(verbose_name='What did you dislike about this counselling session?', max_length=500, default=None)
    changes = models.TextField(verbose_name='What specific changes could improve the counselling session?', max_length=500, default=None)
    


modes = (
    ("Online", "Online"),
    ("Offline", "offline") 
)
class Event(models.Model):
    eve_id = models.IntegerField(verbose_name="id", null=True)
    s_no = models.IntegerField(verbose_name="SI No.", null=True)
    date = models.CharField(verbose_name="Date", max_length=50, null=True)
    event_name = models.CharField(verbose_name="Event Name", max_length=500, null=True)
    mode = models.CharField(verbose_name="Mode", max_length=10, null=True, choices=modes)
    audience = models.CharField(verbose_name="Target Audience", max_length=100, null=True)
    num_stus = models.IntegerField(verbose_name="No. Students Reg.", null=True)
    speaker = models.CharField(verbose_name="Speaker", max_length=500, null=True)
    school = models.CharField(verbose_name="School", max_length=200, null=True)
    def __str__(self):
        return self.event_name
