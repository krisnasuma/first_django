from django.shortcuts import render, HttpResponse #untuk memanggil render dan HttpResponse

#untuk menampilkan database pada views, kita akan meletakkan pada bagian page 'b'
#import dahulu dari file models pada fungsi 'Friends'
from .models import Friends
#--

# Create your views here.


def hello_world(request):
    #jika opsi menggunakan konteks, ini contohnya
    context = {
        'name1': 'Krisna',
        'age1': 23
    }
    return render(request, 'hello_world.html', context) #cara ini bisa dilakukan jika menggunakan tempelate dengan membuat folder tempelate di folder utama sebelumnya setting dahulu di bagian setting.py
    #return HttpResponse("<h1>Selamat Datang</h1>") #cara konvensional untuk membuat view


def a(request):
    #jika opsi menggunakan konteks, ini contohnya
    context1 = {
        'saya' : 'saya',
        'suka' : 'suka',
        'makan' : 'makan'
    }
    return render(request, 'a.html', context1) #cara ini bisa dilakukan jika menggunakan tempelate dengan membuat folder tempelate di folder utama sebelumnya setting dahulu di bagian setting.py
    #return HttpResponse("<h1>Ini A</h1>") #cara konvensional untuk membuat view

def b(request):
    #menampilkan models Friends disini buat variable baru dahulu
    all_friends = Friends.objects.all()
    #buat lebih dahulu konteksnya
    context3 = {
        'all_friends': all_friends
    }
    #definisikan variable context3 dibagian return
    return render(request, 'b.html', context3) #cara ini bisa dilakukan jika menggunakan tempelate dengan membuat folder tempelate di folder utama sebelumnya setting dahulu di bagian setting.py
    #return HttpResponse("<h1>Ini B</h1>") #cara konvensional untuk membuat view