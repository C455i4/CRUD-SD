# from django.shortcuts import render
from api.serializers import AcaoSerializer
from rest_framework import viewsets, permissions
from App.models import Acao
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import AcaoSerializer

class AcaoViewSet(viewsets.ModelViewSet):
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def lista_de_acoes(request):
    if request.method == 'GET':
        acoes = Acao.objects.all()
        serializer = AcaoSerializer(acoes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        acao = JSONParser().parse(request)
        serializer = AcaoSerializer(data=acao)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def acoes_detalhes(request, pk):
    try:
        acao = Acao.objects.get(pk=pk)
    except Acao.DoesNotExist:
        return JsonResponse({'message': 'A ação não existe'}, status=404)

    if request.method == 'GET':
        serializer = AcaoSerializer(acao)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        acao = JSONParser().parse(request)
        serializer = AcaoSerializer(acao, data=acao)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        acao.delete()
        return JsonResponse({'message': 'Acao excluída com sucesso!'}, status=204)