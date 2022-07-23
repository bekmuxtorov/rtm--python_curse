"""
# Created on 2022-07-22

@author: Asadbek Muxtorov

@mavzu: Fayllar bilan ishlash

for i in range(7):
    print(f" \"{'*'*20} {i+1} - masala {'*'*20}\" ")

 """
"******************** 1 - masala ********************"
# Matnli faylni o'qish uchun dastur yozing.
# file = open('word.txt', 'r')
# file_tarkibi = file.read()
# print(file_tarkibi)
# file.close()

"******************** 2 - masala ********************"
# Faylni birinchi n qatorini o'quvchi dastur yozing.
# n = int(input("n ni kiriting: "))
# i = 0
#
# file = open('word.txt', 'r')
# file_tarkiblar = file.readlines()
# if len(file_tarkiblar) >= n:
#     while i < n:
#         print(file_tarkiblar[i])
#         i += 1
#
# else:
#     print(f"Kiritishda xatolik!!!. Fayldagi maxsimal qator {len(file_tarkiblar)}")
# file.close()

"******************** 3 - masala ********************"
# Faylga matn qo'shish va matnni ko'rsatish uchun dastur yozing:
# file_name = input("Fayl nomini(kengaytmasi bilan) yoki yo'lini ko'rsating: ")
# add_text = input("Matn qo'shishingiz mumkin: ")
# if file_name:
#     file = open(file_name, 'a')
#     file.write(add_text)
#     file.close()
#
# else:
#     print("Bunday fayl mavjud emas!!!")

# file_name = input("Fayl nomini(kengaytmasi bilan) yoki yo'lini ko'rsating: ")
# try:
#     file = open(file_name, 'r')
#     file_tarkibi = file.read()
#     print(file_tarkibi)
#     file.close()
#
# except FileNotFoundError :
#     print("Bunday fayl mavjud emas!!!")

"******************** 4 - masala ********************"
# Fayl satrini oq'ish va ro'yxatda saqlash uchun dastur yozing.
# file = open('word.txt', 'r')
# file_lines = file.readline()
# print(file_lines)
#
# file_arr = file.readlines()
# print(file_arr)
"******************** 5 - masala ********************"
# Eng uzun so'zlarni topish dasturini yozing:
# file = open('word.txt', 'r')
#
# file_arr = [i.strip() for i in file.readlines()]
# file_arr_length = []
# for file_arr_item in file_arr:
#     file_arr_length.append(len(file_arr_item))
#
# index = file_arr_length.index(max(file_arr_length))
# print(file_arr[index])

"******************** 6 - masala ********************"
# Ro'yxatni faylga yozish uchun   dastur yozing
# arr = ['Absattor', "G'ulom", 23, 'iyul']
# file = open('word.txt', 'w')
# file.write(str(arr))

"******************** 7 - masala ********************"
def golf():
    print("1 -- Saqlash."
        "\n2 -- Natijalarni ko'rish."
        "\n0 -- Dasturni to'xtatish.")
    tanlov = int(input("Tanlovinigizni kiriting: "))
    while tanlov != 0:
        if tanlov == 1:
            name, hisob = saqlash()
            result = f"{name.title()} ----- {hisob}" + '\n'
            file = open('word.txt', 'a')
            file.write(result)
            file.close()
            print("Muvaffaqiyatli kiritildi. Malades✅")

            print("1 -- Saqlash."
                  "\n2 -- Natijalarni ko'rish."
                  "\n0 -- Dasturni to'xtatish.")
            tanlov = int(input("Tanlovinigizni kiriting: "))

        elif tanlov == 2:
            korish()
            print("1 -- Saqlash."
                  "\n2 -- Natijalarni ko'rish."
                  "\n0 -- Dasturni to'xtatish.")
            tanlov = int(input("Tanlovinigizni kiriting: "))
        else:
            print("Kiritishda xatolik!!! ")
            tanlov = int(input("Qayta kiriting: "))

def saqlash():
    print('='*40)
    name = input("O'yinchini ismini kiriting: ")
    hisob = input(f"{name.title()}ning golf hisobini kiriting: ")
    print('=' * 40)
    return name, hisob

def korish():
    file = open('word.txt', 'r')
    file_tarkibi = [i.rstrip('\n') for i in file.readlines()]
    print('='*20)
    print("Natijalar:")
    for j, file_tarkib in enumerate(file_tarkibi):
        print(f"{j+1}. {file_tarkib}")
    print('='*20)


golf()



