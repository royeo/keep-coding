from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'home.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a , b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

# 比如用户收藏夹中收藏的URL是旧的，让以前的 /add/3/4/自动跳转到现在新的网址,需要自己写一个跳转
def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))


