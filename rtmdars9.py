# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:02:33 2022

@author: Asadbek Muxtorov
        github.com\bekmuxtorov
        
@mavzu: Tuple(kortej) bilan ishlash
"""

"""============================== 1 - masala =============================="""
# nums = (10,45,76,1,43)
# print(nums[-1])


"""============================== 2 - masala =============================="""
# nums = (10,45,76,1,43,1)
# num = int(input("Yangi element qo'shing: "))
# print(nums)

# nums_list = list(nums) # ro'yhatga aylantirildi
# nums_list.append(num)  # ro'yhatga yangi element qo'shildi

# nums = tuple(nums_list) # ro'yhat kortej(tuple)ga aylantirildi. 
# print(nums)

"""============================== 3 - masala =============================="""
# nums = (10,45,76,1,43,1,5)
# print(5 in nums) # 5 soni berilgan kortejda bor yoki o'qligini tekshiradi. in yordamida.

"""============================== 4 - masala =============================="""
# nums = [10,45,76,1,43,1,5]
# print(nums)

# nums_tuple = tuple(nums)
# print(nums_tuple)

"""============================== 5 - masala =============================="""
# students = ('Asadbek','Kamol','Komil',"G'ayrat", 'Anvar')
# print(students)
# students_list = list(students)

# students_list.remove("Anvar")

# students = tuple(students_list)
# print(students)

"""============================== 6 - masala =============================="""
# cars = (
#             ('Malibu', 2022, 'qizil'),
#             ('Cobilt', 2022, 'qora'),
#             ('Gentra', 2021, 'oq'),
#             ('Nexia 3',2020, 'qora')
#         )

# print(cars[3][1])

"""============================== 7 - masala =============================="""
# countries = (
#                 ('Braziliya','Braziliya'),
#                 ('Uzbekiston', 'Toshkent'),
#                 ('Singapur','Singapur'),
#                 ('Rossiya', 'Moskva'),
#                 ('AQSH', 'Washinton')
#             )
# for i in range(len(countries)):
#     if countries[i][0] == countries[i][1]:
#         print(countries[i])
    
#     else:
#         print("Unaqasi yo'q.")

"""
1. list -- ro'yhat [element]

2. dictonary -- lug'at {key:value}

3. set -- to'plam {element}
    To'plam ga oid amallarni bajarish mumkin

4. tuple -- kortej (element)
    Qo'shib ham olib ham bo'lmaydi
    count 
    index
    
"""
