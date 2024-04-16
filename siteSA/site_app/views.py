from django.shortcuts import render, redirect
dados = []

# Create your views here.
def home(request):
    global dados
    nome = ""
    email = ""

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        dados.append({"nome":nome,
                    "email":email})
        
    for i,row in enumerate(dados):
        row["id"] = i
        
    return render(request, "site_app/global/home.html", context={"dados":dados,"nome":nome,"email":email})


def deletar(request,id):
    global dados
    dados.pop(id)
    return redirect(home)

def atualizar(request,id):
    global dados
    
    if request.POST:
        r = dados.pop(id)
        print(r)
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        dados.insert(id,{"nome":nome,
                    "email":email})

        return redirect(home)
    
    nome = dados[id].get("nome")
    email = dados[id].get("email")
    return render(request, "site_app/global/atualizar.html", context={"id":id, "nome":nome,"email":email})



def pesquisar(request):
    return render(request, "site_app/global/pesquisar.html")

def criar(request):
    return render(request, "site_app/global/criar.html")

def atualizarp(request):
    return render(request, "site_app/global/atualizarP.html")