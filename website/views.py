from django.shortcuts import render
from numpy import require
from .forms import *
from .models import *

def common_code(request):
    context = {}
    return context

def home_page(request):
    context1 = common_code(request)
    return render(request, 'home.html',context1)


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



    # form = CreateStudent()
    # if request.method  == 'POST':
    #     form = CreateStudent(request.POST)
    #     print(form.is_valid())
    #     # print(form.cleaned_data.get('email'))
    #     if form.is_valid():
    #         form.save()
    #         print(form.cleaned_data.get('email'))
    #         return redirect('login')
    # context = {'form': form}
def registration_page(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.is_valid())
    context = {'form': form}
    return render(request, 'registration_page_1.html',context)

def feedback_page(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        print(form.is_valid())
    context = {'form': form}
    return render(request, 'feedback_page_1.html',context)



