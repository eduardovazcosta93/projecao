from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HTTP REQUEST


def home_page_view(request):
    
    list = {'nome':'Eduardo', 'sobrenome':'Vaz da Costa', 'data':'17/05/1993'}
    # FUNÇÃO RETORNA HTTP RESPONSE
    return render(request, 'ShuffleApp/home.html', context=list)
