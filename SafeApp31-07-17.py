#-*- coding: utf-8 -*-
import datetime as tarih

def ParaEkle(para):
    # Islem Numarasini artt?r.
    global IslemNo
    IslemNo+=1
    # Tarihi Al
    now = tarih.datetime.now()
    simdikitarih=now.strftime("%d.%m.%Y")
    # [islem numaras?, tarih, tur,miktar]
    KasaHareketler.append([IslemNo,simdikitarih,"Giris",para])

IslemNo=0

def ParaCikar(para):
    global KasaTutar
    global IslemNo


    IslemNo += 1
    # Tarihi Al
    now = tarih.datetime.now()
    simdikitarih = now.strftime("%d.%m.%Y")
    # [islem numaras?, tarih, tur,miktar]
    KasaHareketler.append([IslemNo, simdikitarih, "Cikis", -para])


def Yazdir():
    # KasaHareketler icindeki islemleri yazd?r
    print "-------------------------------------------------------"
    for i in KasaHareketler:
        print i

    print "-------------------------------------------------------"

def Hesapla():
    toplam=0
    for i in KasaHareketler:
        toplam=toplam+i[-1]
    print "Kasa Tutar=",toplam



#KasaHareketler adinda bir liste olusturuyoruz.
KasaHareketler=[]

print "Hosgeldiniz."
while True:
    print "İşlem Seçiniz. "
    print "1. Para Ekle "
    print "2. Para Çıkar. "
    print "Çıkmak için 3 e basınız."
    secim=input("Seçiniz:")
    if secim==3:
        break;

    miktar= input("Miktar Giriniz:")
    if secim==1:
        ParaEkle(miktar)
    elif secim==2:
        ParaCikar(miktar)
    else:
        print "Hatalı giriş"


Hesapla()
Yazdir()
