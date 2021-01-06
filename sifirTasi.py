sayiDizi=[]
basaAl = []
kacEleman=int(input("Kaç elemanlı bir dizi oluşturmak istiyorsunuz? "))
for x in range(kacEleman):
    sayi=int(input("Eleman: "))
    sayiDizi.append(sayi)

for i in sayiDizi:# 15 30 0 21 65
    if i == 0:
        basaAl.append(i)
        sayiDizi.remove(i)

basaAl.extend(sayiDizi)
print("Oluşturduğunuz ",kacEleman,"elemanlı sayı diziniz:",basaAl)


