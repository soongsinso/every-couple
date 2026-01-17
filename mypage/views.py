from django.http import JsonResponse
from .models import Users




# from django.http import JsonResponse, HttpResponseBadRequest
# from django.contrib.auth.decorators import login_required
# from .models import Users

# @login_required  # 로그인 여부 확인
# def index(request):
#     try:
#         # 현재 로그인한 사용자의 정보를 가져옵니다.
#         user = Users.objects.get(username=request.user.username)
        
#         # JSON으로 반환할 데이터를 딕셔너리 형태로 변환합니다.
#         user_data = {
#             'username': user.username,
#             'age': user.age,
#             'name': user.name,
#             'university': user.university,
#             'major': user.major,
#             'studentnumber': user.studentnumber,
#         }

#         return JsonResponse(user_data)

#     except Users.DoesNotExist:
#         # 사용자가 존재하지 않을 때 처리
#         return JsonResponse({'error': 'User does not exist'}, status=404)

#     except Exception as e:
#         # 다른 오류 발생 시 처리
#         return JsonResponse({'error': str(e)}, status=500)

# def index(request):
#     # 현재 로그인한 사용자의 정보를 가져옵니다.
#     user = Users.objects.get(username=request.user.username)
    
#     # JSON으로 반환할 데이터를 딕셔너리 형태로 변환합니다.
#     user_data = {
#         'username': user.username,
#         'age': user.age,
#         'name': user.name,
#         'university': user.university,
#         'major': user.major,
#         'studentnumber': user.studentnumber,
#         # 'password': user.password  # 비밀번호는 보통 JSON 응답에 포함되지 않습니다.
#     }

#     return JsonResponse(user_data)


########################html



# mypage/views.py
from django.shortcuts import render
from .models import Users

def index(request):
    # 현재 로그인한 사용자의 정보를 가져옵니다.
    # request.user는 Django의 기본 인증 시스템에서 사용되는 User 객체를 참조합니다.
    # 만약 request.user와 Users 모델이 연결되어 있다면, 그 정보를 가져오는 방법입니다.
    user = Users.objects.get(username=request.user.username)  # request.user.username이 Users 모델의 username과 일치한다고 가정

    return render(request, 'mypage/mypage.html', {'user': user})




