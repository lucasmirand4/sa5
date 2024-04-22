from django.shortcuts import render, redirect
from .models import Pessoa
dados = []

# Create your views here.
def home(request):
    nome = ""
    email = ""
    idade = ""
    dados = Pessoa.objects.all().order_by('-id')[:10]
    

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        idade= request.POST.get("idade")
        Pessoa.objects.create(nome= nome,email= email, idade = idade)
        
    return render(request, "site_app/global/home.html", context={"dados":dados,"nome":nome,"email":email, "idade":idade})


def deletar(request,id=0):
    pessoa = {}
    if id:
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        return redirect(deletar)
    
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)  
    else:
        pessoa ["pessoas"] = Pessoa.objects.all()
    return render(request, "site_app/partials/deletar.html", context=pessoa)
    
def atualizar(request,id=0):
    
    pessoa = {}
    if id: 
        if request.POST:
            pessoa = Pessoa.objects.get(id=id)
            pessoa.nome = request.POST.get("nome", pessoa.nome)
            pessoa.email = request.POST.get("email", pessoa.email)
            pessoa.idade = request.POST.get("idade",pessoa.idade)

            pessoa.save()

            return redirect(atualizar)
        
        pessoa["pessoa"] = Pessoa.objects.get(id=id)
        return render(request, "site_app/partials/atualizarp.html", pessoa)
    

    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)  
    else:
        pessoa ["pessoas"] = Pessoa.objects.all()
        
    return render(request, "site_app/partials/atualizar.html", context=pessoa)



def pesquisar(request):
    pessoa = {}
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)  
    else:
        pessoa ["pessoas"] = Pessoa.objects.all()
        
    return render(request, "site_app/partials/pesquisar.html", pessoa)

def criar(request):
    nome = ""
    email = ""
    idade = 0
    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        idade= request.POST.get("idade")
        Pessoa.objects.create(nome= nome,email= email, idade = idade)
        
    return render(request, "site_app/partials/criar.html", context={"nome":nome,"email":email, "idade":idade})

def atualizarp(request):
    return render(request, "site_app/global/atualizarP.html")