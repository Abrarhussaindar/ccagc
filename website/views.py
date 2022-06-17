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
    
    eves = Event.objects.all()
    print(eves[0].date)
    context1 = {
        "eves": eves,
    }
    return render(request, 'events_page.html',context1)

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



