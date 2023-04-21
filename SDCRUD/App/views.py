from django.shortcuts import render, redirect   
from App.models import Acao  
from App.formulario import AcaoFormulario

def adicionar(request):  
    if request.method == "POST":  
        form = AcaoFormulario(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = AcaoFormulario()  
    return render(request,'adicionar.html',{'form':form}) 
 
def listarAcoes(request):  
    lista_acoes = Acao.objects.all()  
    return render(request,"listar.html",{'lista_acoes':lista_acoes})  

def editar(request, id):  
    acao = Acao.objects.get(id=id) 
    print(acao.data) 
    return render(request,'editar.html', {'acao':acao})  

def atualizar(request, id):  
    acao = Acao.objects.get(id=id)

    form = AcaoFormulario(request.POST, instance=acao)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'editar.html', {'acao':acao}) 
 
def remover(request, id):  
    acao = Acao.objects.get(id=id)  
    acao.delete()  
    return redirect("/")  
