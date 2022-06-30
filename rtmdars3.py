"""============================== if 1 =============================="""
# num = int(input("Sonni kiriting: "))
# if num > 0:
#     num += 1

# print(num)

"""============================== if 2 =============================="""
# num = int(input("Sonni kiriting: "))
# if num > 0:
#     num += 1
# else:
#     num -= 2

# print(num)

"""============================== if 3 =============================="""
# num = int(input("Sonni kiriting: "))
# if num > 0:
#     num += 1
# elif num < 0:
#     num -= 2
# else:
#     num = 10
    
# print(num)

"""============================== if 4 =============================="""
# count = 0
# for i in range(3):
#     num = int(input(f"{i+1}-sonni kiriting: "))
#     if num > 0:
#         count += 1
        
# print(f"Musbat butun sonlar soni: {count}")

"""============================== if 5 =============================="""
# count_positive = 0
# count_negative = 0
# for i in range(3):
#     num = int(input(f"{i+1}-sonini kiriting: "))
#     if num > 0:
#         count_positive += 1
#     else:
#         count_negative += 1

# print(f"Musbat butun sonlarning soni: {count_positive}")
# print(f"Manfiy butun sonlarning soni: {count_negative}") 

"""============================== if 6 =============================="""       
# num1 = int(input("a sonni kiriting: a= "))
# num2 = int(input("b sonni kiriting: b= "))
# result = 0

# if num1 > num2:
#     result = num1
# else:
#     result = num2

# print(f"{num1} va {num2} sonlarning kattasi: {result}")
    
"""============================== if 7 =============================="""
# num1 = int(input("a sonni kiriting: "))
# num2 = int(input("b sonni kiriting: "))

# if num1 > num2:
#     result = 1
# else:
#     result = 2
# print(f"{num1} va {num2} sonlarning kattasini tartib raqami: {result}")

"""============================== if 8 =============================="""
# num1 = int(input("a sonni kiriting: "))
# num2 = int(input("b sonni kiriting: "))

# if num1 > num2:
#     print(num1,num2)
# else:
#     print(num2,num1)

"""============================== if 9 =============================="""
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))

# if A < B:
#     print(f"A = {A}, B = {B}")
# else:
#     print(f"A = {B}, B = {A}")
    
"""============================== if 10 =============================="""
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))

# if A != B:
#     A = A + B
#     B = A
# elif A == B:
#     A = 0
#     B = A
# print(f"A = {A}, B = {B}")
    
"""============================== if 15 =============================="""
# num1 = int(input("Birinchi sonini kiriting: "))
# num2 = int(input("Ikkinchi sonini kiriting: "))
# num3 = int(input("Uchinchi sonini kiriting: "))

# sum1 = num1 + num2
# sum2 = num1 + num3
# sum3 = num2 + num3

# if sum1 > sum2:
#     if sum1 > sum3:
#         result = f"{num1},{num2}"
#     else:
#         result = f"{num2},{num3}"
# else:
#     if sum2 > sum3:
#         result = f"{num1}, {num3}"
#     else:
#         result = f"{num2},{num3}"
        
# print(result)

"""============================== if 16 =============================="""
# A = int(input("A sonni kiriting: "))
# B = int(input("B sonni kiriting: "))
# C = int(input("C sonni kiriting: "))

# if (A < B) and (B < C):
#     A *= 2
#     B *= 2
#     C *= 2
# else:
#     A *= -1
#     B *= -1
#     C *= -1
    
# print(f"A = {A}, B = {B}, C = {C} ")

"""============================== if 17 =============================="""
# A = int(input("A sonni kiriting: "))
# B = int(input("B sonni kiriting: "))
# C = int(input("C sonni kiriting: "))

# if ((A < B) and B < C) or ((C < B) and (B < A)):
#     A *= 2
#     B *= 2
#     C *= 2
    
# else: 
#     A *= -1
#     B *= -1
#     C *= -1
    
# print((f"A = {A}, B = {B}, C = {C} "))

"""============================== if 18 =============================="""
# A = int(input("A sonni kiriting: "))
# B = int(input("B sonni kiriting: "))
# C = int(input("C sonni kiriting: "))

# if A == B:
#     result = 3

# elif A == C:
#     result = 2

# elif B == C:
#     result = 1
    
# print(result)
    
"""============================== if 19 =============================="""
# A = int(input("A sonni kiriting: "))
# B = int(input("B sonni kiriting: "))
# C = int(input("C sonni kiriting: "))
# D = int(input("D sonni kiriting: "))
 
# if (A == B) and (B == C):
#    result = 4
   
# elif (A == B) and (B == D):
#     result = 3

# elif (A == C) and (C == D):
#     result = 2

# else:
#     result = 1
    
# print(result)

"""============================== if 20 =============================="""
# A = int(input("A nuqta koordinatasini kiriting: "))
# B = int(input("B nuqta koordinatasini kiriting: "))
# C = int(input("C nuqta koordinatasini kiriting: "))

# dis_ab = abs(A - B)
# dis_ac = abs(A - C)

# if dis_ab > dis_ac:
#     result = f"A nuqtaga eng yaqin nuqta {C}, orasidagi masofa: {dis_ac}"
# else:
#     result = f"A nuqtaga eng yaqin nuqta {B}, orasidagi masofa: {dis_ab}"

# print(result)

"""============================== if 21 =============================="""
# print("Nuqta koordinatalarni kiriting:")
# x = int(input("x = "))
# y = int(input("y = "))
# if x == 0 and y == 0:
#     result = 0

# elif x != 0 and y == 0:
#     result = 1
 
# elif x == 0 and y != 0:
#     result = 2

# else:
#     result = 3

# print(f"Natija: {result}")   

"""============================== if 22 =============================="""
# print("Nuqta koordinatalarini kiriting: ")
# x = int(input("x = "))
# y = int(input("y = "))

# if x != 0 and y != 0:
#     if x > 0 and y > 0: result = 1
 
#     elif x < 0 and y > 0: result = 2
        
#     elif x < 0 and y < 0: result = 3
    
#     else: result = 4
    
# else:
#     result = 0
    
# if result == 0:
#     print("Kiritishda xatolik!!!")
# else:
#     print(f"({x}, {y}) -- nuqta {result}-chorakka tegishli nuqta.")

"""============================== if 23 =============================="""
"""============================== if 24 =============================="""
# import math
# x = int(input("x ni qiymatini kiriting: "))
# if x > 0:
#     result = 2 * math.sin(x) 
# else:
#     result = x - 6
# print(f"F(x) funksiyaning {x} nuqtadagi qiymati: {result}")

"""============================== if 25 =============================="""
# x = int(input("x sonini kiriting: "))
# if x < -2 or x > 2:
#    result = 2 * x
# else:
#     result = -3 * x

# print(result)x = int(input("x sonini kiriting: "))   

"""============================== if 26 =============================="""  
# x = int(input("x sonini kiriting: "))
# if x <= 0:
#     result = -1 * x
# elif 0 < x and x < 2:
#     result = x ** 2
# else:
#     result = 4
# print(result)

"""============================== if 27 =============================="""  
# x = float(input("x sonini kiriting: "))

# if x < 0:
#     result = 0
# elif int(x) % 2 == 0:
#     result = 1
# else:
#     result = -1
    
# print(result)

"""============================== if 28 =============================="""  
# year = int(input("Yilni kiriting: "))
# if year % 4 == 0 or year % 400 == 0:
#     result = 366
# else:
#     result = 365 
    
# print(f"{year}-yildagi kunlar sonini: {result} kun")

"""============================== if 29 =============================="""  
# num = int(input("Sonini kiriting: "))
# if num != 0:
#     if num > 0:
#         result = "musbat "
#     else:
#         result = "manfiy "
        
#     if num % 2 == 0:
#         result += "juft son"
#     else:
#         result += "toq son"
# else:
#     result = "son nolga teng"
        
# print(f"{result}")
    
"""============================== if 30 =============================="""     
# num = int(input("Sonini kiriting: "))
# if 0 < num and num < 9:
#     result = "bir xonalik "

# elif 10 < num and num < 99:
#     result = "ikki xonalik "
    
# else:
#     result = "uch xonalik "
    
# if num % 2 == 0:
#     result += "juft son"

# else:
#     result += "toq son"
    
# print(result)























