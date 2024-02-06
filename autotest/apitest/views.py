from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from apitest.models import ApiTest, ApiStep, Apis
from django.contrib.auth.decorators import login_required


# Create your views here.

def test(request):
    return HttpResponse('hello test')


def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': '账号或密码错误，请重新输入！'})
    # else:
    #     context={}
    #     return render(request,'login.html',context)

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


@login_required
def apitest_manage(request):
    apitest_list = ApiTest.objects.all()
    username = request.session.get('user', '')
    return render(request, 'apitest_manage.html', {'user': username, 'apitests': apitest_list})


@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = ApiStep.objects.all()
    return render(request, 'apistep_manage.html', {'user': username, 'apisteps': apistep_list})


@login_required
def apis_manage(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    return render(request, 'apis_manage.html', {'user': username, 'apiss': apis_list})
