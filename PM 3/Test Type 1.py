uts = int(input("NIlai UTS: "))
utsp = int(input("NIlai UTSP: "))
uas = int(input("NIlai UAS: "))
uasp = int(input("NIlai UASP: "))
nilai_akhir = uts * 0.3 + utsp * 0.15 + uas * 0.4 + uasp * 0.15
print(nilai_akhir)
if 80 <= nilai_akhir <= 100:
    print('nilai kamu A')
elif 70 <= nilai_akhir < 80:
    print('nilai kamu B')
elif 60 <= nilai_akhir < 70:
    print('nilai kamu C')
elif 40 <= nilai_akhir < 60:
    print('nilai kamu D')
elif 0 <= nilai_akhir < 40:
    print('nilai kamu E')
else : 
    print("invalid")
