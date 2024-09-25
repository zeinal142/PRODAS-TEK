# print('Menggabungkan Dua List')

# # Input: List pertama dan kedua
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# # List baru untuk menyimpan hasil gabungan
# new_list = []

# # Menggunakan loop untuk menggabungkan elemen list1 dan list2
# for i in range(len(list1)):
#     new_list.append(list1[i] + list2[i])

# # Output list hasil gabungan
# print(new_list)

# things = ["mozzarella", "cinderella", "salmonella"]
# seseorang_things = things[1].upper()
# print ("Huruf besarkan elemen yang merujuk kepada seseorang : ", seseorang_things)
# chezzy_things = things[0].upper()
# print ("Huruf besarkan elemen yang merujuk kepada chezzy : ", chezzy_things)
# things.remove("salmonella")
# new_things = things[0].upper(), things[1].upper()
# print ("Hapuskan elemen yang merujuk kepada disease : ", new_things)

things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].upper()
print ("Huruf besarkan elemen yang merujuk kepada seseorang : ", things)
things[0]= things[0].upper()
print ("Huruf besarkan elemen yang merujuk kepada chezzy : ", things)
things.remove("salmonella")
print ("Hapuskan elemen yang merujuk kepada disease : ", things)