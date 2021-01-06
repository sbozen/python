list = []
tek=[]
adet = int(input("Kaç elemanlı bir dizi oluşturmak istiyorsunuz :"))
for x in range(adet):
    sayi = int(input("Elemanı girin: "))
    list.append(sayi)
    if sayi%2==1:
        tek.append(sayi)
print("Girmiş olduğunuz liste: ",list)
print("Listenizdeki tek sayılar",sorted(tek))
print("Listenizdeki en büyük tek sayı: ",max(tek))
