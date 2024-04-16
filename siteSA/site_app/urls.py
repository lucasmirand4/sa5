from django.urls import path
from .views import home, criar, deletar, atualizar, pesquisar, atualizarp

urlpatterns = [
    path('', home, name="home"),

    path('deletar/<int:id>', deletar, name="deletar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),

    path('pesquisar/', pesquisar ),
    path('criar/', criar),
     path('atualizar/', atualizarp),

]
