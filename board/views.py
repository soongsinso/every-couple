from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Board,Users




# from django.http import JsonResponse, HttpResponse
# from django.utils import timezone
# from .models import Users, Board

# from django.http import JsonResponse
# from .models import Board

# def index(request):
#     # Database 조회: university가 특정 값이 아닌 사용자만 조회
#     user_id = request.user.username
#     users = Users.objects.filter(username=user_id).first()
#     exclude_university = users.university  # 제외할 학교 이름

#     # Board와 연결된 user 필드의 university가 exclude_university가 아닌 경우만 필터링
#     boards = Board.objects.exclude(user__university=exclude_university).values()

#     # QuerySet을 리스트로 변환
#     board_list = list(boards)
    
#     return JsonResponse({'boards': board_list}, safe=False)


# def new(request):  # GET + POST
#     if request.method == 'POST':
#         postname = request.POST.get('title')
#         content = request.POST.get('content')

#         # Database에 저장
#         user_id = request.user.id
#         board = Board(postname=postname, content=content, createdate=timezone.now(), updatedate=timezone.now(), user_id=user_id)
#         board.save()
        
#         return JsonResponse({'status': 'success', 'board_id': board.pk})
    
#     return JsonResponse({'status': 'ready'})


# def create(request):  # POST
#     postname = request.POST.get('title')
#     content = request.POST.get('content')

#     # Database에 저장
#     user_id = request.user.id
#     board = Board(postname=postname, content=content, createdate=timezone.now(), updatedate=timezone.now(), user_id=user_id)
#     board.save()

#     return JsonResponse({'status': 'success', 'board_id': board.pk})


# def detail(request, pk):
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         return JsonResponse({'error': 'Board not found'}, status=404)

#     user_id = board.user_id
#     users = Users.objects.filter(user_id=user_id).first()

#     if users is None:
#         return JsonResponse({'error': 'User not found'}, status=404)

#     board_data = {
#         'postname': board.postname,
#         'content': board.content,
#         'createdate': board.createdate,
#         'updatedate': board.updatedate,
#         'username': users.username,
#         'other_user_id': users.user_id,
#     }

#     return JsonResponse({'board': board_data})


# def delete(request, pk):  # POST
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         return JsonResponse({'error': 'Board not found'}, status=404)
    
#     board.delete()

#     return JsonResponse({'status': 'deleted'})


# def edit(request, pk):  # GET + POST
#     if request.method == 'POST':
#         postname = request.POST.get('title')
#         content = request.POST.get('content')

#         try:
#             board = Board.objects.get(pk=pk)
#         except Board.DoesNotExist:
#             return JsonResponse({'error': 'Board not found'}, status=404)

#         board.postname = postname
#         board.content = content
#         board.save()

#         return JsonResponse({'status': 'success', 'board_id': board.pk})
    
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         return JsonResponse({'error': 'Board not found'}, status=404)

#     board_data = {
#         'postname': board.postname,
#         'content': board.content,
#         'createdate': board.createdate,
#         'updatedate': board.updatedate
#     }

#     return JsonResponse({'board': board_data})


# def update(request, pk):  # POST
#     postname = request.POST.get('title')
#     content = request.POST.get('content')

#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         return JsonResponse({'error': 'Board not found'}, status=404)

#     board.postname = postname
#     board.content = content
#     board.save()

#     return JsonResponse({'status': 'success', 'board_id': board.pk})














######################################html
# # Create your views here.
def index(request):
    # Database 조회
    boards = Board.objects.all() # 모든 데이터

    context = {
        'boards': boards,
    }
    return render(request, 'board/index.html', context)

# def index(request):
#     # Database 조회: university가 특정 값이 아닌 사용자만 조회
#     user_id = request.user.username
#     users = Users.objects.filter(username= user_id).first()
#     exclude_university = users.university  # 제외할 학교 이름

#     # Board와 연결된 user 필드의 university가 exclude_university가 아닌 경우만 필터링
#     boards = Board.objects.exclude(user__university=exclude_university)

#     context = {
#         'boards': boards,
#     }
#     return render(request, 'board/index.html', context)

def new(request): # GET + POST 
    if request.method == 'POST': 
        postname = request.POST.get('title')
        content = request.POST.get('content')

        # Database에 저장
        # 1. Article 인스턴스 생성
        user_id = request.user.id
        board = Board(postname=postname, content=content,createdate=timezone.now(),updatedate=timezone.now(),user_id=user_id)
        # 2. 저장!
        board.save()
        return redirect('board:detail', board.pk)
    
    else : 
        context = {

        }
        return render(request, 'board/new.html', context)

def create(request): # POST
    postname = request.POST.get('title')
    content = request.POST.get('content')

    # Database에 저장
    # 1. Article 인스턴스 생성
    user_id = request.user.id
    board = Board(postname=postname, content=content,createdate=timezone.now(),updatedate=timezone.now(),user_id=user_id)
    # 2. 저장!
    board.save()

    return redirect('articles:detail', board.pk)
    # context = {
    #     'title': title,
    #     'content': content,
    # }
    # return render(request, 'articles/create.html', context)

def detail(request, pk):
    # Database 조회: 단 하나의 data
    board = Board.objects.get(pk=pk)
    user_id = board.user_id
    users = Users.objects.filter(user_id= user_id).first()

    if users is None:
        # 사용자가 없는 경우에 대한 처리
        return HttpResponse("해당 사용자를 찾을 수 없습니다.")
    
    context = {
        'board': board,
        'users':users.name,
        'other_user_id': users.user_id,
    }
    return render(request, 'board/detail.html', context)


def delete(request, pk): # POST
    # Database 삭제 (조회 + 삭제)
    # 1. 조회
    board = Board.objects.get(pk=pk)
    # 2. 삭제
    board.delete()

    return redirect('board:index')


def edit(request, pk): # GET
    
    if request.method == 'POST': 
        # 게시글 수정 수행 
        postname = request.POST.get('title')
        content = request.POST.get('content')

        # Database 조회 + 수정 + 저장
        # 1. 조회
        board = Board.objects.get(pk=pk)
        # 2. 수정
        board.postname = postname
        board.content = content
        # 3. 저장
        board.save()

        return redirect('board:detail',board.pk)
        
    else : 
        # 게시글 수정 양식 ! 


        # Database 조회( + 저장)
        # 1. 조회
        board = Board.objects.get(pk=pk)

        context = {
            'board': board,
        }
        return render(request, 'board/edit.html', context)

def update(request, pk): # POST
    postname = request.POST.get('title')
    content = request.POST.get('content')

    # Database 조회 + 수정 + 저장
    # 1. 조회
    board = Board.objects.get(pk=pk)
    # 2. 수정
    board.postname = postname
    board.content = content
    # 3. 저장
    board.save()

    return redirect('board:detail',board.pk)
    
    
