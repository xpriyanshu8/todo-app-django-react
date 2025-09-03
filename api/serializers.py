from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.models import make_password


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields = "__all__" 
        read_only_fields = ['user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','email','password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer,self).create(validated_data)