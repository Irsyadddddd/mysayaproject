from django.shortcuts import render 
from berita.models import Artikel, kategori


def home(request):
    template_name = 'halaman/index.html'
    data_artikel = Artikel.objects.all
    print(data_artikel)
    context = {
        'title' : 'Selamat datang',
        'data_artikel': data_artikel,
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'tentang saya',
        'umur' :20,
    }
    return render(request, template_name, context)

