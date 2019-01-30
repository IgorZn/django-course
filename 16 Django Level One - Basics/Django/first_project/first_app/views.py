from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *

# Create your views here.
# def index(request):
#     return HttpResponse("<b>Hello world!</b>")
#
# def igor(request):
#     return HttpResponse("<b>Hello Igor!</b>")

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app\index.html', context=date_dict)

def my_users(request):
    usrs_list = Users.objects.order_by('first_name')
    usrs_dict = {'my_users': usrs_list}
    return render(request, 'first_app\my_users.html', usrs_dict)


# def t_index(request):
#     my_dict = {'insert_me': "This string from %s" % (__file__)}
#     return render(request,'first_app\index.html',context=my_dict)

def help(request):
    my_dict = {'insert_help': HttpResponse("<b>This string from %s<br>, moreover it's </b>" % (__file__))}
    return render(request, 'first_app\help.html', context=my_dict)