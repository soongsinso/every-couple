# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# from django.utils import timezone
# from .models import Chatroom, Chatpa, Chat, Users

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"

#         # # 채팅방과 사용자 객체 가져오기
#         self.user = self.scope["user"]
        
#         if self.user.is_authenticated:
#             user_instance = Users.objects.filter(username=self.user.username).first()
#             chatroom_instance = Chatroom.objects.filter(chatname=self.room_name).first()

#             # chatroom_instance = Chatroom.objects.create(chatname=self.room_name, chatstate= 'activate',entertime=timezone.now())
#             # chatroom_instance.save()
            
#             if user_instance and chatroom_instance:
#                 # 채팅방과 사용자 간의 관계를 기록
#                 Chatpa.objects.get_or_create(
#                     user=user_instance,
#                     chatroom=chatroom_instance
#                 )

#                 # Join room group
#                 async_to_sync(self.channel_layer.group_add)(
#                     self.room_group_name, self.channel_name
#                 )

#                 self.accept()
#             else:
#                 self.close()  # 사용자가 인증되지 않았거나 채팅방이 존재하지 않을 경우 연결 종료
#         else:
#             self.close()  # 인증되지 않은 사용자 연결 종료
#         # Join room group
#         # async_to_sync(self.channel_layer.group_add)(
#         #     self.room_group_name, self.channel_name
#         # )

#         # self.accept()
        
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )

#     # Receive message from WebSocket (= client)
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # 현재 채팅방과 사용자 객체 가져오기
#         chatroom = Chatroom.objects.filter(chatname=self.room_name).first()
#         user = Users.objects.filter(username=self.user.username).first()

#         if chatroom and user:
#         #     # 이전 Chat 객체의 checker 값을 조회하여 가장 큰 값에 1을 더합니다.
#         #     last_chat = Chat.objects.filter(chatroom=chatroom).order_by('-checker').first()
#         #     if last_chat:
#         #         checker_value = last_chat.checker + 1
#         #     else:
#         #         checker_value = 1  # 채팅방에 저장된 메시지가 없을 경우 기본값으로 1 설정

#             # 메시지를 Chat 모델에 저장합니다.
#             chat = Chat.objects.create(
#                 chat=message,
#                 sendtime=timezone.now(),
#                 checker=1,  # 누적된 checker 값을 설정
#                 user=user,  # 현재 사용자를 설정
#                 chatroom=chatroom
#             )

#             # Send message to room group
#             async_to_sync(self.channel_layer.group_send)(
#                 self.room_group_name, {"type": "chat.message", "message": message}
#             )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({"message": message}))



###############################################################################################
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.utils import timezone
from .models import Chatroom, Chatpa, Chat, Users


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.chatroom_id = self.scope["url_route"]["kwargs"]["chatroom_id"]
        self.room_group_name = f"chat_{self.chatroom_id}"

        self.user = self.scope["user"]

        if self.user.is_authenticated:
            user_instance = Users.objects.filter(username=self.user.username).first()
            chatroom_instance = Chatroom.objects.filter(chatroom_id=self.chatroom_id).first()

            if user_instance and chatroom_instance:
                # 관계 저장
                Chatpa.objects.get_or_create(user=user_instance, chatroom=chatroom_instance)

                # 그룹 추가
                async_to_sync(self.channel_layer.group_add)(
                    self.room_group_name, self.channel_name
                )

                self.accept()
            else:
                self.close()
        else:
            self.close()

    def disconnect(self, close_code):
        # 그룹 제거
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        chatroom = Chatroom.objects.filter(chatroom_id=self.chatroom_id).first()
        user = Users.objects.filter(username=self.user.username).first()

        if chatroom and user:
            # 메시지 저장
            Chat.objects.create(
                chat=message,
                sendtime=timezone.now(),
                checker=1,
                user=user,
                chatroom=chatroom
            )

            # 메시지 그룹에 브로드캐스트
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "message": message,
                    "user": user.username,
                    "sender_channel_name": self.channel_name,  # 현재 클라이언트 추가
                }
            )

    def chat_message(self, event):
        message = event["message"]
        user = event["user"]
        sender_channel_name = event["sender_channel_name"]

        # 현재 클라이언트가 보낸 메시지는 제외
        if self.channel_name != sender_channel_name:
            self.send(text_data=json.dumps({
                "message": message,
                "user": user
            }))
