# ####################################################################################
# from django.shortcuts import render
# from .models import Chatroom , Chatpa,Users
# from django.utils import timezone

# # Create your views here.
# def index(request):
#     return render(request, "chat/index.html")


# def room(request, room_name):
#     user_id = request.user.username
#     users = Users.objects.filter(username= user_id).first()
#     room = Chatroom.objects.create(chatname=room_name, chatstate= 'activate',entertime=timezone.now())
#     room.save()
    
#     # chatpa = Chatpa.objects.create(user= users, chatroom=room)
#     # chatpa.save()

#     return render(request, "chat/room.html", {"room_name": room_name})




# #########################################################################################
# from django.shortcuts import render,redirect

# def chat_view(request):
#     if request.user.is_authenticated:
#         user_id = request.user.username  # 현재 로그인한 사용자의 ID
#         # 사용자 ID를 사용하여 필요한 로직을 처리합니다.
#         return render(request, 'chat/chat.html', {'user_id': user_id})
#     else:
#         return redirect('account:login')  # 로그인되지 않은 경우 로그인 페이지로 리디렉션
#############################################################################################










from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chatroom, Users, Chat

# 채팅방 리스트를 보여주는 뷰
@login_required
def chatroom_list(request):
    user_id = request.user.username
    users = Users.objects.filter(username= user_id).first()
    chatrooms = Chatroom.objects.filter(user1=users) | Chatroom.objects.filter(user2=users)
    return render(request, 'chat/chatroom_list.html', {'chatrooms': chatrooms})


# 특정 채팅방으로 이동하는 뷰
from django.utils import timezone

@login_required
def chatroom_detail(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    user_id = request.user.username
    users = Users.objects.filter(username=user_id).first()
    
    # 사용자 검증 (해당 방에 있는 사용자만 접근할 수 있게)
    if users not in [chatroom.user1, chatroom.user2]:
        return redirect('chat:chatroom_list')
    
    messages = Chat.objects.filter(chatroom_id=chatroom)
    
    # chatroom_id를 WebSocket에서 사용하기 위해 템플릿에 전달
    return render(request, 'chat/chatroom_detail.html', {
        'chatroom': chatroom,
        'chatroom_id': chatroom_id,  # chatroom_id를 템플릿으로 전달
        'messages': messages,
        'user': request.user
    })


# 채팅방을 생성하는 뷰 (1대1 채팅방)
@login_required
def create_chatroom(request, other_user_id):
    other_user = get_object_or_404(Users, pk=other_user_id)
    user_id = request.user.username
    users = Users.objects.filter(username= user_id).first()
    
    # 이미 채팅방이 존재하는지 확인
    existing_chatroom = Chatroom.objects.filter(user1=users, user2=other_user) | Chatroom.objects.filter(user1=other_user, user2=users)
    if existing_chatroom.exists():
        return redirect('chat:chatroom_detail', chatroom_id=existing_chatroom.first().pk)
    
    # 새 채팅방 생성
    new_chatroom = Chatroom.objects.create(user1=users, user2=other_user,entertime=timezone.now(),chatstate= 'True')
    return redirect('chat:chatroom_detail', chatroom_id=new_chatroom.pk)




