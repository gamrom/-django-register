from django.shortcuts import render, redirect
from .models import Fcuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 저장
# Create your views here.
#
def home(request):
    user_id = request.session.get('user')
    if user_id: #user가 있으면
        fcuser = Fcuser.objects.get(pk = user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data= {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다'
        else:
            fcuser = Fcuser.objects.get(username=username) #앞에는 필드명, 뒤에는 값. 따라서 앞에는 모델의 필드명, 뒤에는 username = request.POST.get('username', None) 이거.
            if check_password(password, fcuser.password):
                #비밀번호가 일치, 로그인 처리를!
                #아래는 세션에 저장
                request.session['user'] = fcuser.id
                return redirect('/')
            else:
                res_data['error'] = '비밀번호를 틀렸습니다'

        return render(request, 'login.html', res_data)



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
