"""
Created on Sun Jul  3 20:29:32 2022

@author: Asadbek Muxtorov

@mavzu: To'plam bilan ishlash 
"""

"""============================== 1 - masala =============================="""
# students = {"Asadbek","Lazizbek","Bekmuhammad","Rashidbek","Raxmatillo"}
# new_student = input("Talabani ismini kiriting: ")
# students.add(new_student)
# print(students)

"""============================== 2 - masala =============================="""
# students = {"Asadbek","Lazizbek","Bekmuhammad","Rashidbek","Raxmatillo"}
# del_student = input("O'chirilishi kerak bo'lgan talaba ismi: ")

# if del_student in students:
#     print(students)
#     students.remove(del_student)
#     print(students)
# else:
#     print("Bunday element to'plamda mavjud emas.")

"""============================== 3 - masala =============================="""
# names = {"Asadbek","Lazizbek","Bekmuhammad","Rashidbek","Raxmatillo", "Hasan"}
# if "Hasan" in names:
#     print(names)
#     names.remove("Hasan")
#     print(names)

# else:
#     print("Hasan bu to'plamda mavjud emas.")

"""============================== 4 - masala =============================="""
# # intersection -- ikkisiga ham tegishli bo'lganini qaytaradi --- kesishma
# a_sonlar = {21,14,48,76,42}
# b_sonlar = {21,75,48,85,42}

# c_sonlar = a_sonlar.intersection(b_sonlar) #kesishmani hisoblash
# print(c_sonlar)

"""============================== 5 - masala =============================="""
# # uninon -- ikkita to'plamni birlashtirib beradi -- birlashtirish
# a_sonlar = {21,14,48,76,42}
# b_sonlar = {21,75,48,85,42}

# c_sonlar = a_sonlar.union(b_sonlar) # birlashmani bajardi
# print(c_sonlar)

"""============================== 6 - masala =============================="""
# # difference() --- nosimmetrik ayrima 
# a_sonlar = {21,14,48,76,42}
# b_sonlar = {21,75,48,85,42}

# c_sonlar = a_sonlar.difference(b_sonlar) # Faqat a to'plamga tegishligini chiqarib beradi.
# print(c_sonlar)

"""============================== 7 - masala =============================="""
# a.issubset(b) --- a to'plam b to'plamni kichik to'plami ekanligini tekshiradi.  
# a_sonlar = {21,42}
# b_sonlar = {21,75,48,85,42}

# print(a_sonlar.issubset(b_sonlar))

"""============================== 7 - masala =============================="""
# # a.issuperset(b) --- a to'plam b to'plamni katta to'plami ekaligini tekshiradi.
# a_sonlar = {21,42}
# b_sonlar = {21,75,48,85,42}

# print(b_sonlar.issuperset(a_sonlar))

"""============================== 8 - masala =============================="""
# a_sonlar = {21,42}
# b_sonlar = {21,75,48,85,42}

# a_sonlar.update(b_sonlar)
# print(a_sonlar)
# a_sonlar.clear()
# print(a_sonlar)

"""============================== 9 - masala =============================="""
# # symmetric_difference() --- ikki to'plamdan umumiy bo'lmaganlarini chiqaradi --- simmetrik ayrima 
# a_sonlar = {21,14,48,76,42}
# b_sonlar = {21,75,48,85,42}

# c_sonlar = a_sonlar.symmetric_difference(b_sonlar)
# print(f"Simmetrik ayrima: {c_sonlar}")

"""============================== 10 - masala =============================="""
# # frozenset() --- muzlatilgan ro'yhat
# a_sonlar = {21,14,48,76,42}
# b_sonlar = {21,75,48,85,42}

# c_sonlar = a_sonlar.union(b_sonlar)
# c_sonlar = frozenset()
# print(c_sonlar)

"""============================== 11 - masala =============================="""
# a_sonlar = {21,14,48,76,42,21,75,48,85,42}
# print(f"To'plamdagi eng kichik son: {min(a_sonlar)}")
# print(f"To'plamdagi eng katta son: {max(a_sonlar)} ")

"""============================== 12 - masala =============================="""
# a_sonlar = {21,14,48,76,42,21,75,48,85,42}
# print(a_sonlar)
# print(f"To'plam uzunligi: {len(a_sonlar)}")

"""============================== 13 - masala =============================="""
# a_sonlar = {21,14,48,76,42,21,75,48,85,42}
# a_son = input("Element kiriting: ")
# if a_son in a_sonlar:
#     print(f"{a_son} to'plamda mavjud.")
# else:
#     print(f"{a_son} to'plamda mavjud emas.")

"""============================== 14 - masala =============================="""
# a_sonlar = {1,2,4,85}
# b_sonlar = {21,75,48,85,42}

# if a_sonlar.intersection(b_sonlar) == set():
#     print("Umumiy elmenti mavjud emas.")
# else:
#     print("umumiy element mavjud.")

"""============================== 15 - masala =============================="""    
# beysboll = {"Asadbek","Lazizbek","Bekmuhammad","Rashidbek","Raxmatillo", "Hasan"}
# basketboll = {"Asadbek","Lazizbek","Bekmuhammad","Rashidbek","Tavvakalboy","Topvoldi","Botir"}

# print(f"Ikkalasiga ham qatnashadigon talabalar: {beysboll.intersection(basketboll)}")
# print(f"Sport bilan shug'ullandigon talabalar: {basketboll.union(beysboll)}")
# print(f"Faqat basketbol bilan shug'ullanadigon talabalar: {basketboll.difference(beysboll)}")























