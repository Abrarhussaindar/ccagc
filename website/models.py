from email.mime import application
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import random

from django.db.models.expressions import Value

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