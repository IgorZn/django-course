from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("<b>Hello world!</b>")
#
# def igor(request):
#     return HttpResponse("<b>Hello Igor!</b>")

def t_index(request):
    my_dict = {'insert_me': "This string from %s" % (__file__)}
    return render(request,'first_app\index.html',context=my_dict)

def help(request):
    my_dict = {'insert_help': HttpResponse("<b>This string from %s<br>, moreover it's </b>" % (__file__))}
    return render(request, 'first_app\help.html', context=my_dict)