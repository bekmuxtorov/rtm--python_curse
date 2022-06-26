"""============================== Integer 6 =============================="""
# # input: ab --> ikki honali son
# # output: a, b --> onlik, birlik
# a = int(input("Sonni kiriting: "))

# onlik = a // 10
# birlik = a % 10

# print(f"""o'nlik: {onlik}
# birlik: {birlik}
# """)

"""============================== Integer 7 =============================="""
# # input: ab --> ikki xonalik son
# # output: a + b --> raqamlar yeg'indisi

# a = int(input("Sonni kiriting: "))
# yegindi = a // 10 + a % 10
# print(f"{a} ning raqamlar yeg'indisi: {yegindi}")

"""============================== Integer 8 =============================="""
# # input: ab --> ikki xonalik son
# # output ba --> o'rinlari almashgan son

# num = int(input("Sonni kiriting: "))
# num_reverse = 10 * (num % 10 ) + (num // 10 )
# print(f"{num} ni raqamlari teskari yozilgan son: {num_reverse}")

"""============================== Integer 9 =============================="""
# # input: abc --> uch xonlik son
# # output: a --> yuzlar xonasidagi raqam

# num = int(input("Sonni kiriting: "))
# yuzlar = num // 100
# print(f"{num} ni yuzlar xonasidagi raqam: {yuzlar}")

"""============================== Integer 10 =============================="""
# # input: abc --> uch xonalik son
# # output: c, b --> birlik, onlik

# num = int(input("Uch xonalik son kiriting: "))
# birlik = num % 100 % 10
# onlik = num % 100 // 10
# print(f"""{num}da birlik: {birlik}
#       onlik: {onlik}      
#       """)

"""============================== Integer 11 =============================="""
# # input: abc --> uch xonalik son
# # output: a + b + c --> raqamlar yeg'indisi

# num = 258
# # num = int(input("Uch xonali son kiriting: "))
# yuzlik = num // 100
# onlik = num % 100 // 10
# birlik = num % 100 % 10
# yegindi = yuzlik + onlik + birlik
# print(f"{num} ni raqamlar yeg'indisi: {yegindi}")

"""============================== Integer 12 =============================="""
# # input: abc --> uch xonalik son
# # output: cba --> teskari tartibda yozilgan son

# num = int(input("Uch xonalik son kiriting: "))
# yuzlik = num // 100
# onlik = num % 100 // 10
# birlik = num % 100 % 10

# new_num = birlik * 100 + onlik * 10 + yuzlik * 1
# print(f"{num} ni teskari tartibda: {new_num}")

"""============================== Integer 13 =============================="""
# # input: abc --> uch xonalik son
# # output: bca --> 

# num = int(input("Uch xonalik son kiriting: "))
# yuzlik = num // 100
# onlik = num % 100 // 10
# birlik = num % 100 % 10

# new_num = onlik * 100 + birlik *10 + yuzlik * 1
# print(f"Result: {new_num}")

"""============================== Integer 14 =============================="""
# # input: abc --> uch xonalik son
# # output: cab --> 

# num = int(input("Uch xonalik son kiriting: "))
# yuzlik = num // 100
# onlik = num % 100 // 10
# birlik = num % 100 % 10

# new_num = birlik * 100 + yuzlik * 10 + onlik * 1
# print(f"Result: {new_num}")

"""============================== Integer 15 =============================="""
# # input: abc --> uch xonalik son
# # output: bac --> 

# num = int(input("Uch xonalik son kiriting: "))
# yuzlik = num // 100
# onlik = num % 100 // 10
# birlik = num % 100 % 10

# new_num = onlik * 100 + yuzlik * 10 + birlik * 1
# print(f"Result: {new_num}")

"""============================== Integer 16 =============================="""
# # input: abc --> uch xonalik son
# # output: acb --> 

# num = int(input("Uch xonalik son kiriting: "))
# yuzlik = num // 100
# onlik = num % 100 // 10
# birlik = num % 100 % 10

# new_num = yuzlik * 100 + birlik * 10 + onlik * 1
# print(f"Result: {new_num}")

"""============================== Integer 17 =============================="""
# # input: abcd --> to'rt xonalik son
# # output: b --> yuzlik xonasidagi raqam

# num = int(input("To'rtxonalik son kiriting: "))
# yuzlik = num % 1000 // 100
# print(f"{num} ni yuzlik raqami: {yuzlik}")
  
"""============================== Integer 18 =============================="""  
# # input: abcd --> to'rt xonalik son
# # output: a --> minglar xonasidagi raqam

# num = int(input("To'rt xonalik son kiriting: "))
# minglik = num // 1000
# print(f"{num} ni minglik raqami: {minglik}")

"""============================== Integer 19 =============================="""
"""
Masala: Kun boshidan N sekund vaqt o'tti. Kun boshidan boshlab qancha minut 
to'la o'tganligini aniqlovchi dastur tuzilsin.

1 minut --> 60 sekund
x minut --> N
x = N * 1 / 60
Bizdan o'tgan to'la minut so'ralmoqda, Demak / (bo'lish)ni o'rniga  //
(butun bo'lish)ni ishlatamiz.
"""
# N = int(input("N = "))
# minut = N // 60
# print(f"{N} sekundda to'la o'tgan minut: {minut} ")

"""============================== Integer 20 =============================="""  
# # input: N --> o'tgan sekundlar soni
# # output: to'la soatni aniqlash
# N = int(input("O'tgan sekundni kiriting: "))
# full_hour = N // 3600 
# print(f"{N} sekundda o'tgan tola soat: {full_hour} soat")

"""============================== Integer 21 =============================="""  
# # input: N --> o'tgan sekundlar 
# # output: O'tgan minut va sekundlar aniqlansin

# N = int(input("O'tgan sekundni kiriting: "))
# minut = N // 60 
# secund = N % 60 
# print(f"{N} sekundda o'tgan daqiqa: {minut} minut, sekund: {secund} sekund ")

"""============================== Integer 22 =============================="""  
# # input: N --> o'tgan sekundlar 
# # output: O'tgan va sekundlar aniqlansin

# N = int(input("O'tgan sekundni kiriting: "))
# hour = N // 3600
# secund = N % 3600 % 60 

# print(f"{N} sekundda o'tgan soat: {hour} soat, {secund} sekund")

"""============================== Integer 23 =============================="""  
# # output: O'tgan minut va sekundlar aniqlansin

# N = int(input("O'tgan sekundni kiriting: "))
# hour = N // 3600
# minut = N % 3600 // 60 
# secund = N % 3600 % 60 

# print(f"{N} sekundda o'tgan soat: {hour} soat, {minut} minut, {secund} sekund")
















