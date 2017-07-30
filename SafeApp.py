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
ParaEkle(1150)
ParaEkle(200)
ParaEkle(300)
ParaEkle(400)
ParaEkle(500)
ParaCikar(200)
Yazdir()
Hesapla()


"""
Notlar:
Yapilacaklar:
    Arayuz Gelistirilecek
    Kullanici sistemi eklenecek
    VeriTabani sistemi ekle

"""
