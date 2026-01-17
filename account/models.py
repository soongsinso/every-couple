# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Board(models.Model):
    board_id = models.BigAutoField(primary_key=True)
    postname = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    createdate = models.DateTimeField()
    updatedate = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


class BoardUni(models.Model):
    board_uni_id = models.BigAutoField(primary_key=True)
    postname = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    createdate = models.DateTimeField()
    updatedate = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board_uni'


class Chat(models.Model):
    chat_id = models.BigAutoField(primary_key=True)
    chat = models.CharField(max_length=100, blank=True, null=True)
    sendtime = models.DateTimeField()
    checker = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    chatroom = models.ForeignKey('Chatroom', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat'


class Chatpa(models.Model):
    chatpa_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    chatroom = models.ForeignKey('Chatroom', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chatpa'


class Chatroom(models.Model):
    chatroom_id = models.BigAutoField(primary_key=True)
    chatname = models.CharField(max_length=100, blank=True, null=True)
    chatstate = models.CharField(max_length=100)
    entertime = models.DateTimeField()
    user1 = models.ForeignKey('Users', models.DO_NOTHING)
    user2 = models.ForeignKey('Users', models.DO_NOTHING, related_name='chatroom_user2_set')

    class Meta:
        managed = False
        db_table = 'chatroom'


class Style(models.Model):
    style_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'style'


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    studentnumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
