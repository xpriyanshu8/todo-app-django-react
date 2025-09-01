from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializers
from .models import Task


@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTasks(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTasks(request):
    tasks = task.objects.get(id=pk)
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTasks(request):
    tasks = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted successfully")

