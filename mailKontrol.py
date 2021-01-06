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
