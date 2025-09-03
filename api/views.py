from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Task
from rest_framework import viewsets,filters,permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTask(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTask(request, pk):
    task = Task.objects.filter(id=pk).first()
    if not task:
        return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTask(request, pk):
    task = Task.objects.filter(id=pk).first()
    if not task:
        return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def registerUser(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user=request.user
    return Response({
        "username": user.username,
        "email":user.email
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTasks(request,pk):
    task=get_object_or_404(Task, id= pk, user=request.user)
    serializer = TaskSerializer(task,many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def addTask(request):
    data=request.data
    task=Task.objects.create(
        user=request.user,
        title=data['title'],
        completed=data['completed']
    )
    serilaizer =TaskSerializer(task, many=False)
    return Response(serilaizer.data)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class=TaskSerializer
    filter_backends=[filters.SearchFilter]
    search_fields= ['title'] 
