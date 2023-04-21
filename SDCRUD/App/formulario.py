from django import forms  
from App.models import Acao  

class AcaoFormulario(forms.ModelForm):  
    class Meta:  
        model = Acao  
        fields = ['codigo_acao', 'descricao', 'data', 'open', 'close', 'high', 'low', 'volume']
        widgets = { 
            'codigo_acao': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'descricao': forms.TextInput(attrs={ 'class': 'form-control' }),
            'data': forms.DateInput(attrs={ 'class': 'form-control'}),
            'open': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'close': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'high': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'low': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'volume': forms.NumberInput(attrs={ 'class': 'form-control' }),
        }