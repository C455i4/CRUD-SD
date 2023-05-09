# from django.shortcuts import render
from api.serializers import AcaoSerializer
from rest_framework import viewsets, permissions
from App.models import Acao
from api.serializers import AcaoSerializer

class AcaoViewSet(viewsets.ModelViewSet):
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer
    permission_classes = [permissions.IsAuthenticated]
