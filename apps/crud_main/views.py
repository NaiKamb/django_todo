from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def list_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response (serializer.data)
    # return Response ({'msg':f'Hello, i am list todo called from {request.method}'})

@api_view(['POST'])
def create_todos(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def delete_todos(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return Response(f'Успешно удалена запись под номером {pk}')

@api_view(['PATCH'])    
def update_todos(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(f'Запись под номером {pk} обновлена ')
