""""
İlk olarak bir tam sayı ile mail adresinin @ işaretinden sonraki uzunluğunu girersiniz. Daha sonrasında ise mail adreslerini girerek geçerli bir adres olup olmadığını bize döndüren programı yazmalısınız.
Geçerli e-posta adresleri şu kurallara uymalıdır:
•	kullanıcıAdı@websiteSağlayıcı.siteUzantısı.ülkeKodu biçim türüne sahip olmalıdır .
•	Kullanıcı adı yalnızca harf, rakam, kısa çizgi ve alt çizgi içerebilir.
•	Web sitesi adı yalnızca harf ve rakamlardan oluşabilir.
•	Uzantının maksimum uzunluğu 3 olmalıdır. ( websitesağlayıcı.siteuzantısı veya websitesağlayıcı veya websiteSağlayıcı.siteUzantısı.ülkeKodu  bilgilerini içermelidir.

Giriş Formatı
1.	İlk olarak uzantı uzunluğunu giriniz.
2.	Daha sonrasında mail adresini giriniz.
3.	Sonucu ekrana yazdırınız. ( Mail Adresi Uygundur veya mail adresi uygun değildir. )

Kısıtlamalar
Mail Doğrulamayı bir fonksiyon kullanarak yapmalısın.
Fonksiyon çıktı olarak bir bool döndürmelidir.
Gelen bool true ise mail adresi doğru, false ise yanlış olarak kabul edilecektir.
Çıkış formatı
3
Gaziuniversitesi@gazi.edu.tr
Mail adresiniz doğrudur.
"""
def kontrol(mail):
    parcalaMail = mail.split("@")
    kAd = parcalaMail[0]
    uzanti= parcalaMail[1]
    siteSaglayici=uzanti.split(".",2)
    ozelKarakterler = "%\~|[]<>{}!@#&*+=()×÷₺':;/^$"
    print("Girmiş olduğunuz mail adresi: ",mail)
    uzantiUzunluk=len(siteSaglayici)
    print(uzantiUzunluk)
    uzantiUzunluk=uzantiUzunluk+1
    if uzantiUzunluk <=3 :
        for i in kAd:
            if i in ozelKarakterler:
                print("Kullanıcı adında özel karakter kullandınız!")
                break
            else:
                print("Mail adresiniz doğrudur.")
                break
    else:
        print("Mail adresiniz geçerli değil!")

print("-"*100+
      "\nLütfen e-posta adresinizi belirtilen formatta giriniz \n"+
      "(kullanıcıAdı@websiteSağlayıcı.siteUzantısı.ülkeKodu)\n"+
      "-"*100)

mail = input("Mail adresiniz: ")
kontrol(mail)
