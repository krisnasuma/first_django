from django.db import models

# Create your models here.

class Friends(models.Model): 
    #nama tabel sebagai contoh Friends
    name = models.CharField(max_length=255)
    #nama tabel name dengan tipe data charfield (string)
    age = models.IntegerField()

    #pastikan setelah membuat model lakukan migration pada promp
    #lalu migrate

    #pada tampilan page admin web biasanya belum terlihat
    #harus register di admin.py

    #untuk menampilkan informasi berupa "name" saja di web admin
    #biasanya di admin namanya masih diberi nama berupa "objek" saja
    #harus di definisikan
    def __str__(self):
        return self.name