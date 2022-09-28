import imp
from django.shortcuts import render, redirect
# from numpy import require
from formtools.wizard.views import *
from .forms import *
from .models import *

def common_code(request):
    context = {}
    return context

def home_page(request):
    context1 = common_code(request)
    return render(request, 'home.html',context1)

def demo():
    pass

def events_page(request):
    # ALL EVENTS
    eves = Event.objects.all()
    print(eves[0].date)

    # SCHOOL WISE EVENTS
    SOE_eves = Event.objects.filter(school="SOE")
    soe_num = SOE_eves.count()
    print(soe_num)
    SOD_eves = Event.objects.filter(school="SOD")
    sod_num = SOD_eves.count()
    SOL_eves = Event.objects.filter(school="SOL")
    sol_num = SOL_eves.count()
    SOM_eves = Event.objects.filter(school="SOM")
    som_num = SOM_eves.count()
    SOC_eves = Event.objects.filter(school="SOM")
    soc_num = SOC_eves.count()
    SOI_eves = Event.objects.filter(school="SOM")
    soi_num = SOI_eves.count()
    context1 = {
        "eves": eves,
        "SOE_eves":SOE_eves,    
        "soe_num": soe_num,

        "SOL_eves":SOL_eves,
        "sol_num": sol_num,

        "SOM_eves":SOM_eves,
        "som_num": som_num,

        "SOC_eves":SOC_eves,
        "soc_num": soc_num,

        "SOD_eves":SOD_eves,
        "sod_num": sod_num,

        "SOI_eves":SOI_eves,
        "soi_num": soi_num,
        
    }
    return render(request, 'events_page.html',context1)

def particular_eves(request, eveid):
    event = Event.objects.filter(id=eveid)

    context1 = {
        "event":event,
        # common_code(request)
    }
    return render(request, 'particular_event.html',context1)

def importance_page(request):
    context1 = common_code(request)
    return render(request, 'importance_page.html',context1)

def intro_page(request):
    context1 = common_code(request)
    return render(request, 'introduction_page.html',context1)


def members_page(request):
    context1 = common_code(request)
    return render(request, 'members_page.html',context1)

def registration_page(request):
    return render(request, 'registration_page_1.html',)

class mulitstepform(SessionWizardView):
    template_name = 'registration_page.html'
    form_list = [PersonalForm, AcadamicForm, CareerForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        stu_personal = Stu_Personal(
            first_name = form_data[0]['first_name'],
            middle_name = form_data[0]['middle_name'],
            last_name = form_data[0]['last_name'],
            dob = form_data[0]['dob'],
            # gender = form_data[0]['gender'],
            phone_number = form_data[0]['phone_number'],
        )
        
        stu_personal.save()

        stu_acadmic = Stu_Acadamic(
            roll_number = form_data[1]['roll_number'],
            section = form_data[1]['section'],
            semester = form_data[1]['semester'],
            course = form_data[1]['course'],
            university_mail_id = form_data[1]['university_mail_id'],
            school = form_data[1]['school'],
        )
        stu_acadmic.save()
# 'hobbies','why_ccagc', 'career_goals','hopes','barries', 'ambition', 'permanent_address', 'current_address'
        stu_career = Stu_career(
            hobbies = form_data[2]['hobbies'],
            why_ccagc = form_data[2]['why_ccagc'],
            career_goals = form_data[2]['career_goals'],
            hopes = form_data[2]['hopes'],
            barries = form_data[2]['barries'],
            ambition = form_data[2]['ambition'],
        )
        stu_career.save()
        # print("student",stu_acadmic)
        return render(self.request, 'thankyou.html', {'data': form_data})
        

def thankyou(request):
    return render(request, 'thankyou.html')

def feedback_page(request):
    return render(request, 'feedback_page_1.html')

class mulitstepfeedbackform(SessionWizardView):
    template_name = 'feedback_page.html'
    form_list = [FeedbackFormone, FeedbackFormtwo, FeedbackFormthree]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        partone = FeedbackFormFieldsPartOne(
            counselor_name = form_data[0]['counselor_name'],
            # type_of_counselling_session = form_data[0]['type_of_counselling_session'],
        )
        
        partone.save()

        parttwo = FeedbackFormFieldsParttwo(
            # beneficial = form_data[1]['beneficial'],
            # Information = form_data[1]['Information'],
            # address_my_concerns = form_data[1]['address_my_concerns'],
            # valuable = form_data[1]['valuable'],
            # genuine_interest = form_data[1]['genuine_interest'],
            # knowledgeable = form_data[1]['knowledgeable'],
            # examine_my_alternatives = form_data[1]['examine_my_alternatives'],
        )
        parttwo.save()
# 'hobbies','why_ccagc', 'career_goals','hopes','barries', 'ambition', 'permanent_address', 'current_address'
        partthree = FeedbackFormFieldsPartthree(
            like = form_data[2]['like'],
            dislike = form_data[2]['dislike'],
            changes = form_data[2]['changes'],
        )
        partthree.save()
        # print("student",stu_acadmic)
        return render(self.request, 'thankyouforfeedback.html', {'data': form_data})
        