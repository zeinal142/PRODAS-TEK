# # Tugas 1
# year_list = [2006, 2007, 2008, 2009, 2010]
# print ("Pada tahun berapakah dalam year_list anda berumur 3 tahun? ", year_list[3])
# print ("Pada tahun berapakah dalam year_list anda paling tua? ", year_list[-1])

# # Tugas 2
# things = ["mozzarella", "cinderella", "salmonella"]
# things[1] = things[1].upper()
# print ("Huruf besarkan elemen yang merujuk kepada seseorang : ", things)
# things[0] = things[0].upper()
# print ("Huruf besarkan elemen yang merujuk kepada chezzy : ", things)
# things.remove("salmonella")
# print ("Hapuskan elemen yang merujuk kepada disease : ", things)

# # Tugas 3
surprise = ["Groucho", "Chico", "Harpo"]
last_element = surprise[-3].lower()
#fungsi ::-1 adalah untuk reversed string dari harpo
reversed_last_element = last_element[::-1]
upper_reversed_last_element = reversed_last_element.upper()
print ("Huruf-kecilkan elemen terakhir dari list surprise, balik hurufnya, dan kemudian besarkan : ", upper_reversed_last_element)

# # Tugas 4
# e2i = {
#     'dog' : 'anjing',
#     'cat' : 'kucing',
#     'tiger' : 'macan'
# }

# kata = input('masukkan kata dalam bahasa inggris : ')

# if kata in e2i :
#     print(e2i[kata])
# else :
#     print('kata tidak ada dalam kamus inggris ke indonesia')

# i2e = {value: key for key, value in e2i.items() }

# kata2 = input('masukkan kata dalam bahasa indonesia : ')
# if kata2 in i2e :
#     print(i2e[kata2])
# else :
#     print('kata tidak ada dalam kamus indonesia ke inggris')
    
# # Tugas 5
# life={
#     'animals':{
#         'cats':['Henri','Grumpy','Lucy'],
#         'octopi':{},
#         'emus':{}
#     },
#     'plants':{},
#     'other':{}
# }
# print(life.keys())
# print(life['animals'].keys())
# print(life['animals']['cats'])
