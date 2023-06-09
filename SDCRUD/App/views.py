from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect   
from App.models import Acao  
from App.formulario import AcaoFormulario

User = get_user_model()

@login_required()
def adicionar(request):  
    if request.method == "POST":  
        form = AcaoFormulario(request.POST)  
        if form.is_valid():  
            try: 
                form.instance.user = request.user
                form.save() 
                return redirect('/')  
            except:  
                pass 
    else:  
        form = AcaoFormulario()  
    return render(request,'adicionar.html',{'form':form}) 


@login_required()
def listarAcoes(request):  
    lista_acoes = Acao.objects.all().filter(user=request.user)
    return render(request,"listar.html",{'lista_acoes':lista_acoes})  

@login_required()
def editar(request, id):  
    acao = Acao.objects.get(id=id) 
    return render(request,'editar.html', {'acao':acao})  

@login_required()
def atualizar(request, id):  
    acao = Acao.objects.get(id=id)

    form = AcaoFormulario(request.POST, instance=acao)  
    if form.is_valid():
        try:
            form.instance.user = request.user
            form.save()  
            return redirect('/')
        except ValueError:
            print(ValueError)
            
    else: 
        return render(request, 'editar.html', {'acao':acao}) 
 
@login_required()
def remover(request, id):  
    acao = Acao.objects.get(id=id)  
    acao.delete()  
    return redirect("/")  
