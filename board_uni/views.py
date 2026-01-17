from django.shortcuts import render
from .models import Board
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import BoardUni,Users

# # Create your views here.
# def index(request):
#     # Database 조회
#     boards = BoardUni.objects.all() # 모든 데이터

#     context = {
#         'boards': boards,
#     }
#     return render(request, 'board/index.html', context)

def index(request):
    # Database 조회: university가 특정 값이 아닌 사용자만 조회
    user_id = request.user.username
    users = Users.objects.filter(username= user_id).first()
    user_university = users.university

    # 같은 university의 user 게시물만 조회
    boards = BoardUni.objects.filter(user__university=user_university)

    context = {
        'boards': boards,
    }
    return render(request, 'board_uni/index.html', context)


def new(request): # GET + POST 
    if request.method == 'POST': 
        postname = request.POST.get('title')
        content = request.POST.get('content')

        # Database에 저장
        # 1. Article 인스턴스 생성
        user_id = request.user.id
        board = BoardUni(postname=postname, content=content,createdate=timezone.now(),updatedate=timezone.now(),user_id=user_id)
        # 2. 저장!
        board.save()
        return redirect('board_uni:detail', board.pk)
    
    else : 
        context = {

        }
        return render(request, 'board_uni/new.html', context)

def create(request): # POST
    postname = request.POST.get('title')
    content = request.POST.get('content')

    # Database에 저장
    # 1. Article 인스턴스 생성
    user_id = request.user.id
    board = BoardUni(postname=postname, content=content,createdate=timezone.now(),updatedate=timezone.now(),user_id=user_id)
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
    board = BoardUni.objects.get(pk=pk)
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
    return render(request, 'board_uni/detail.html', context)


def delete(request, pk): # POST
    # Database 삭제 (조회 + 삭제)
    # 1. 조회
    board = BoardUni.objects.get(pk=pk)
    # 2. 삭제
    board.delete()

    return redirect('board_uni:index')


def edit(request, pk): # GET
    
    if request.method == 'POST': 
        # 게시글 수정 수행 
        postname = request.POST.get('title')
        content = request.POST.get('content')

        # Database 조회 + 수정 + 저장
        # 1. 조회
        board = BoardUni.objects.get(pk=pk)
        # 2. 수정
        board.postname = postname
        board.content = content
        # 3. 저장
        board.save()

        return redirect('board_uni:detail',board.pk)
        
    else : 
        # 게시글 수정 양식 ! 


        # Database 조회( + 저장)
        # 1. 조회
        board = BoardUni.objects.get(pk=pk)

        context = {
            'board': board,
        }
        return render(request, 'board_uni/edit.html', context)

def update(request, pk): # POST
    postname = request.POST.get('title')
    content = request.POST.get('content')

    # Database 조회 + 수정 + 저장
    # 1. 조회
    board = BoardUni.objects.get(pk=pk)
    # 2. 수정
    board.postname = postname
    board.content = content
    # 3. 저장
    board.save()

    return redirect('board_uni:detail',board.pk)
    
    
# def index(request):
#     return HttpResponse("안녕하세요, 여러분. 폴즈 인덱스에 오신 것을 환영합니다.")

# def blog(request):
#     # 모든 Post를 가져와 postlist에 저장합니다
#     postlist = Board.objects.all()
#     # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
#     return render(request, 'board/board.html', {'postlist':postlist})

# def posting(request, pk):
#     # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
#     post = Board.objects.get(pk=pk)
#     # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
#     return render(request, 'main/posting.html', {'post':post})