from django.urls import path
from . import views

app_name = 'chat'


# urlpatterns = [
#     path("", views.index, name="index"),
#     #path('list/list/', views.chatroom_list, name='chatroom_list'), 
#     path("<str:room_name>/", views.room, name="room"),
#     # path("<str:room_name>/", views.room, name="room"),
#     ###################################################
#     path("view/view/", views.chat_view, name="chat_view"),
# ]






##################################################################################3
urlpatterns = [
    path('', views.chatroom_list, name='chatroom_list'),  # 채팅방 목록
    path('<int:chatroom_id>/', views.chatroom_detail, name='chatroom_detail'),  # 특정 채팅방
    path('create/<int:other_user_id>/', views.create_chatroom, name='create_chatroom'),  # 채팅방 생성
]


