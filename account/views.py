from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.core.exceptions import MultipleObjectsReturned

from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect


from django.views.decorators.csrf import csrf_protect,csrf_exempt
from .models import Users  # 사용자 모델이 정의된 파일에서 임포트

def index(request):
    return HttpResponse("안녕하세요, 여러분. 폴즈 인덱스에 오신 것을 환영합니다.")





# from django.contrib.auth import authenticate, login, logout
# from .models import Users
# from django.contrib.auth.models import User
# import json
# from django.db import DatabaseError

# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             username = data.get('username')
#             password = data.get('password')
            
#             # 사용자 존재 여부 확인
#             user = User.objects.filter(username=username).first()
#             if not user:
#                 return JsonResponse({'message': 'User does not exist'}, status=401)
            
#             # 사용자 인증
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 #print(f"Session Key: {request.session.session_key}") ##
            
#                 return JsonResponse({
#                     'message': 'Login successful',
#                     'user_id': user.id,
#                 }, status=200)
#             else:
#                 return JsonResponse({'message': 'Invalid login credentials'}, status=401)
#         except DatabaseError as e:
#             return JsonResponse({'error': str(e)}, status=500)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
#     return HttpResponseBadRequest('Invalid request method')
# # def login_view(request):
# #     if request.method == 'POST':
# #         data = json.loads(request.body.decode('utf-8'))
# #         username = data.get('username')
# #         password = data.get('password')
        
        
# #         # 사용자 존재 여부 확인
# #         if not User.objects.filter(username=username).exists():
# #             return JsonResponse({'status': 'error', 'message': 'User does not exist'})
        
# #         user = authenticate(request, username=username, password=password)
# #         if user is not None:
# #             login(request, user)
# #             return JsonResponse({'status': 'success', 'message': 'Login successful'})
# #         else:
# #             return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})
    
# #     return HttpResponseBadRequest('Invalid request method')

# @csrf_exempt
# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return JsonResponse({'status': 'success', 'message': 'Logout successful'})
    
#     return HttpResponseBadRequest('Invalid request method')

# @csrf_exempt
# def register(request):
#     if request.method == "POST":
#         # user_id = request.POST.get('id')
#         # password = request.POST.get('password')
#         # age = request.POST.get('age')
#         # name = request.POST.get('name')
        
#         data = json.loads(request.body.decode('utf-8'))
#         user_id = data.get('username')
#         password = data.get('password')
#         age = data.get('age')
#         name = data.get('name')
#         university = data.get('university')
#         major = data.get('major')
#         studentnumber = data.get('studentnumber')        

#         if Users.objects.filter(username=user_id).exists():
#             return JsonResponse({'status': 'error', 'message': '사용자 이름이 이미 존재합니다.'})
        
#         else:
#             user_profile = Users.objects.create(username=user_id, password=password, age=age, name=name, university=university, major=major,studentnumber=studentnumber)
#             user_profile.save()
        
#         if User.objects.filter(username=user_id).exists():
#             return JsonResponse({'status': 'error', 'message': '사용자 이름이 이미 존재합니다.'})
        
#         else:
#             user = User.objects.create_user(username=user_id, password=password)
#             user.save()
            
#         login(request, user)
#         return JsonResponse({'status': 'success', 'message': 'Registration successful', 'redirect': reverse("account:login")})
    
#     return HttpResponseBadRequest('Invalid request method')




######################html


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('password')
        
        # 사용자 존재 여부 확인
        if not User.objects.filter(username=username).exists():
            return render(request, 'account/login.html', {'message': 'User does not exist'})
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return redirect('account:index')
            return redirect('board_uni:index')
        else:
            return render(request, 'account/login.html', {'message': 'Invalid credentials'})
    
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')


def register(request):
    if request.method == "POST":
        user_id = request.POST.get('id')
        password = request.POST.get('password')
        age = request.POST.get('age')
        name = request.POST.get('name')
        university = request.POST.get('university')
        major = request.POST.get('major')
        studentnumber = request.POST.get('studentnumber')
        
        if Users.objects.filter(username= user_id).exists():
            return render(
                request, "account/register.html", {"message": "사용자 이름이 이미 존재합니다."}
            )
        else:
            user = Users.objects.create(username=user_id, password=password, age=age, name=name, university=university, major=major,studentnumber=studentnumber)
            user.save()
        
        if User.objects.filter(username= user_id).exists():
            return render(
                request, "account/register.html", {"message": "사용자 이름이 이미 존재합니다."}
            )
        else:
            user = User.objects.create_user(username=user_id, password=password)
            user.save()
            
        login(request, user)
        return HttpResponseRedirect(reverse("account:login"))
    else:
        return render(request, "account/register.html")  # 템플릿 경로를 상대 경로로 변경


