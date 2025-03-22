## **Render Data from DB with SQLite**

Kali ini saya mencoba untuk menampilkan data dari Database pada web browser. ada beberapa yang harus di siapkan yaitu : 

- Install Virtual Environtment
- Install Django
- Install Taildwind CDN
- Folder Template

![image.png](attachment:cf50557c-e8e0-43b8-bec1-646202c66cae:image.png)

1. Siapkan databasenya dengan cara masuk folder handphones dan buka file `models.py` dan disini saya membuat database spesifikasi product handphones contoh seperti di bawah ini
    
    ![image.png](attachment:726c3fe9-1f32-47ab-b539-f5c13159ce46:image.png)
    
    - Penjelasan :
        
        `from django.db import models` : Baris ini mengimpor modul models dari Django, yang menyediakan kelas dan fungsi untuk mendefinisikan model database.
        `class Handphone(models.Model):` : Bagian ini mendefinisikan kelas Handphone yang merupakan subclass dari models.Model. Ini berarti Handphone adalah model Django yang akan diterjemahkan menjadi tabel dalam database.
        `variable = models.CharField(max_length=100)` : Bagian ini mendefinisikan beberapa field untuk model Handphone. Setiap field akan menjadi kolom dalam tabel database dengan panjang maksimum 100 karakter.
        
        `def **str**(self):` : Metode ini mendefinisikan representasi string dari objek Handphone. Ketika objek Handphone diubah menjadi string (misalnya, saat ditampilkan di admin Django), akan menampilkan merek dan tipe handphone.
        
2. Lalu cek pada admin panel apakah sudah muncul atau belum untuk database handphones tersebut
    
    ![image.png](attachment:0cd12083-bc09-4f99-9330-dba6988514b3:image.png)
    
    jika sudah muncul silahkan di klik lalu lanjut untuk pengisian sebagai contoh seperti di bawah ini
    
    ![image.png](attachment:a7652695-e4de-4a5e-b68e-892885ff2235:image.png)
    
    klik save nanti akan muncul seperti di bawah ini
    
    ![image.png](attachment:56d74d74-fa86-4c3e-9552-bfa27b040a13:image.png)
    
3. Lalu kita coba untuk passing datanya dari database ke Browser dengan cara buka file [views.py](http://views.py) dan isikan seperti berikut ini
    
    ![image.png](attachment:7563b6a0-995d-44cb-a159-765dd485fe85:image.png)
    
    - Penjelasan :
        
        `from .models import Handphone` : Baris ini mengimpor fungsi render dari django.shortcuts dan model Handphone dari file models.py yang berada di direktori yang sama.
        `handphones = Handphone.objects.all()` : Baris ini mengambil semua objek Handphone dari database menggunakan metode all() dari manager objects. Hasilnya adalah QuerySet yang berisi semua objek Handphone.
        `context = { “handphones”: handphones }` : Bagian ini membuat dictionary context yang berisi data yang akan diteruskan ke template. Dalam hal ini, dictionary memiliki satu kunci, `"handphones"`, yang nilainya adalah QuerySet dari semua objek Handphone.
        
        `return render(request, "index.html", context)` : Baris ini menggunakan fungsi render untuk merender template `index.html` dengan konteks yang diberikan. Fungsi render menggabungkan template dengan data dari context dan mengembalikan objek `HttpResponse` yang berisi halaman HTML yang dihasilkan.
        
4. Jika sudah saya akan mencoba untuk membuat styling card setiap `handphone` , saya akan membuat file bernama `card-hp.html` pada folder `components` , yang isinya adalah seperti berikut ini
    
    ![image.png](attachment:388e157c-cca9-4407-8cbc-c3311019eb5b:image.png)
    
    - Penjelasan :
        
        Secara keseluruhan, template ini digunakan untuk menampilkan informasi detail tentang handphone dalam format kartu. Template ini akan di-include dalam template utama (`index.html`) untuk setiap objek `handphone` yang ada dalam konteks.
        
5. Lalu saya akan melakukan looping untuk menampilkan semua data yang akan di render dengan cara seperti beriku ini
    
    ![image.png](attachment:2efcc321-d4c6-4cc4-8744-5d697670c64f:image.png)
    
    Penjelasan : 
    Bagian ini adalah loop yang iterasi melalui setiap objek `handphone` dalam konteks handphones. Untuk setiap `handphone`, template `components/card-hp.html` akan di-include dan dirender.
    `{% for handphone in handphones %}`: Memulai loop yang iterasi melalui setiap objek `handphone` dalam konteks handphones.
    
    `{% include "components/card-hp.html" %}`: Menyertakan template `components/card-hp.html` untuk setiap `handphone`. Template ini akan menampilkan detail dari setiap `handphone`.
    
    `{% endfor %}`: Mengakhiri loop.
    
6. lalu coba jalankan runserver dan buka pada browsernya hasilnya akan seperti di bawah ini
