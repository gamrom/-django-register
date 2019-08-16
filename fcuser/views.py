from django.shortcuts import render
from .models import Fcuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password #비밀번호 암호화 저장
# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html') #파일 위치는 템플릿 폴더를 자동적으로 찾는다. 만약 폴더안에 폴더면 폴더경로를 써주면됨.
    elif request.method == "POST":
        username = request.POST.get('username', None) #예외 처리하기위해서 name으로 받은 값들을 기본적으로 None으로 설정
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        #예외처리
        if not (username and password and re_password and useremail): #세개의 input중 적어도 한 개가 비었다면,
            res_data['error'] = '모든 값을 입력해야합니다'

        elif password != re_password: #비밀번호 두개가 서로 일치하는지 확인
            # return HttpResponse('비밀번호가 다릅니다!')
            res_data['error'] = '비밀번호가 다릅니다'
        #예외처리끝
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password) #비밀번호 암호화 저장
            )
            fcuser.save()
        return render(request, 'register.html', res_data)
