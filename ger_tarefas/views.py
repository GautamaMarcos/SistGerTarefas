# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .serializers import TaskSerializer, UserSerializer
# from rest_framework_jwt.settings import api_settings
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render, get_object_or_404
from .forms import TaskForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from supabase_config import fetch_from_supabase, insert_to_supabase

def fetch_data_view(request):
    data = fetch_from_supabase('gautama')
    return JsonResponse(data, safe=False)

def insert_data_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        response = insert_to_supabase('gautama', data)
        return JsonResponse(response, safe=False)

@permission_classes([IsAuthenticated])
def edit_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return render(request, 'ger_tarefas/edit_task.html', {'form': form, 'task': task, 'message': 'Tarefa atualizada com sucesso!'})
    else:
        form = TaskForm(instance=task)
    return render(request, 'ger_tarefas/edit_task.html', {'form': form, 'task': task})

@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('nome', openapi.IN_QUERY, description="Nome da tarefa", type=openapi.TYPE_STRING),
        openapi.Parameter('status', openapi.IN_QUERY, description="Status da tarefa (concluída ou pendente)", type=openapi.TYPE_STRING),
    ]
)

@swagger_auto_schema(method='post', request_body=TaskSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user)
        nome = request.GET.get('nome')
        if nome:
            tasks = tasks.filter(nome__icontains=nome)

        status = request.GET.get('status')
        if status:
            if status.lower() == 'concluída':
                tasks = tasks.filter(status=True)
            elif status.lower() == 'pendente':
                tasks = tasks.filter(status=False)

        paginator = PageNumberPagination()
        paginated_tasks = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(paginated_tasks, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='put', request_body=TaskSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    # try:
    #     task = Task.objects.get(pk=pk, user=request.user)
    # except Task.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
        
    elif request.method == 'PUT':     
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()           
            return Response({'message': 'Tarefa atualizada com sucesso!'}, status=status.HTTP_200_OK)       
        else:   
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
@swagger_auto_schema(method='post', request_body=UserSerializer)
@api_view(['POST'])
@csrf_exempt
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return JsonResponse({'message': 'Usuário cadastrado com sucesso'}, status=201)
    return JsonResponse(serializer.errors, status=400)








# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def mark_task_concluida(request, pk):
#     try:
#         task = Task.objects.get(pk=pk, user=request.user)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     task.mark_as_concluida()
#     return Response(status=status.HTTP_200_OK)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def mark_task_pendente(request, pk):
#     try:
#         task = Task.objects.get(pk=pk, user=request.user)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     task.mark_as_pendente()
#     return Response(status=status.HTTP_200_OK)



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.settings import api_settings
# from .models import Task
# from .serializers import TaskSerializer, UserSerializer

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# @api_view(['POST'])
# @csrf_exempt
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         user.set_password(user.password)
#         user.save()
#         return JsonResponse({'message': 'Usuário cadastrado com sucesso'}, status=201)
#     return JsonResponse(serializer.errors, status=400)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def task_list(request):
#     user = request.user
#     status = request.query_params.get('status')
#     if status:
#         tasks = Task.objects.filter(user=user, completed=(status.lower() == 'true'))
#     else:
#         tasks = Task.objects.filter(user=user)
#     serializer = TaskSerializer(tasks, many=True)
#     return JsonResponse(serializer.data, safe=False)
    
    
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def task_create(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(user=request.user)
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def task_detail(request, pk):
#     task = get_object_or_404(Task, pk=pk, user=request.user)
#     serializer = TaskSerializer(task)
#     return JsonResponse(serializer.data)

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def task_update(request, pk):
#     task = get_object_or_404(Task, pk=pk, user=request.user)
#     serializer = TaskSerializer(task, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data)
#     return JsonResponse(serializer.errors, status=400)

# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def task_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk, user=request.user)
#     task.delete()
#     return JsonResponse({'message': 'Tarefa deletada'}, status=204)

