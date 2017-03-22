from django.shortcuts import render

# Create your views here.
def home(request):
    info = {'site': u'南哥', 'content': '无敌'}
    return render(request, 'home.html', {'info': info})