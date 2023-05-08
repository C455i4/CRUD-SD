from rest_framework import serializers
from api.models import Acao

class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acao
        fields = [
            'id',
            'codigo_acao', 
            'descricao',
            'data',
            'open',
            'close',
            'high',
            'low',
            'volume',
        ]