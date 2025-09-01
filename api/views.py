from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def getTask(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
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
def deleteTask(request, pk):
    task = Task.objects.filter(id=pk).first()
    if not task:
        return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

