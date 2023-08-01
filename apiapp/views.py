from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('hello')

def user_list(request):
    return HttpResponse('用户列表')

def user_add(request):
    return HttpResponse('添加用户')