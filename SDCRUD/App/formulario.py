from django import forms  
from App.models import Acao  

class AcaoFormulario(forms.ModelForm):  
    class Meta:  
        model = Acao  
        fields = ['codigo_acao', 'descricao', 'data', 'open', 'close', 'high', 'low', 'volume']
        widgets = { 
            'codigo_acao': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'descricao': forms.TextInput(attrs={ 'class': 'form-control' }),
            'data': forms.DateInput(attrs={ 'type': 'Date','class': 'form-control'}, 
                format=['%Y-%m-%d %H:%M:%S',
                 '%Y-%m-%d %H:%M',
                 '%Y-%m-%d',
                 '%m/%d/%Y %H:%M:%S', 
                 '%m/%d/%Y %H:%M',      
                 '%m/%d/%Y',             
                 '%m/%d/%y %H:%M:%S',    
                 '%m/%d/%y %H:%M',       
                 '%m/%d/%y']),           
            'open': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'close': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'high': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'low': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'volume': forms.NumberInput(attrs={ 'class': 'form-control' }),
        }
