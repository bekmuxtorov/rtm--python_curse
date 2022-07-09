# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:02:27 2022

@author: Asadbek Muxtorov

@mavzu: Funksiya
 
"""
# for i in range(7):
#     print('"""' + '*' * 20 + f" {i+1}-masala " + '*' * 20 + '"""')
"""******************** 1-masala ********************"""
# def bolish(son1, son2):
#     if (son2 != 0):
#         result = son1 / son2
#     else:
#         result = "NOLga bo'lish mumkin emas"
#     print(result)
    
"""******************** 2-masala ********************"""
# def area(width, height):
#     area = width * height
#     print(f"To'rtburchakni yuzi: {area}")
    
"""******************** 3-masala ********************"""
# def perimetr(height, width):
#     perimetr = 2 * (height + width)
#     print(perimetr)
    
"""******************** 4-masala ********************"""
# def area(balandlik, asos):
#     area = (balandlik * asos) / 2
#     print(area)

"""******************** 5-masala ********************"""
# def yegindi(*args):
#     s = 0
#     for arg in args:
#         s += arg
#     print(s)
    
"""******************** 6-masala ********************"""
# def kub(num):
#     result = num ** 3
#     print(result)
    
"""******************** 7-masala ********************"""
# def datas(ism, familiya, sharif, yosh = 20):
#     print(f"Ism: {ism} \nFamiliya: {familiya} \nSharif: {sharif} \nYosh: {yosh}")

"""******************** 8-masala ********************
Mobile waiter mobil app
"""
def oshxona():
    print("""
    \n__MENU__
    \n1 ---- Taomlar
    \n2 ---- Ichimliklar
    \n3 ---- Shirinliklar
    \n0 ---- Chiqish   
    """)
    tanlov = int(input("Tanlovingizni kiriting: "))
    while tanlov > 0:
        if tanlov == 1:
            taomlar()
            print("""
            \n__MENU__
            \n1 ---- Taomlar
            \n2 ---- Ichimliklar
            \n3 ---- Shirinliklar
            \n0 ---- Chiqish   
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))
            
        elif tanlov == 2:
            ichimliklar()
            print("""
            \n__MENU__
            \n1 ---- Taomlar
            \n2 ---- Ichimliklar
            \n3 ---- Shirinliklar
            \n0 ---- Chiqish   
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))
            
        elif tanlov == 3:
            shirinliklar()
            print("""
            \n__MENU__
            \n1 ---- Taomlar
            \n2 ---- Ichimliklar
            \n3 ---- Shirinliklar
            \n0 ---- Chiqish   
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))
            
        elif tanlov == 0:
            tanlovlarni_hisobla(taomlar)
            tanlovlarni_hisobla(ichimliklar)
            tanlovlarni_hisobla(shirinliklar)
        
        else:
            print('*' * 10 + 'Kiritishda xatolik!!!' + '*' * 10)
            print("""
            \n__MENU__
            \n1 ---- Taomlar
            \n2 ---- Ichimliklar
            \n3 ---- Shirinliklar
            \n0 ---- Chiqish   
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))

def tanlovlarni_hisobla(lugat):
    # tanlovlar = {}
    print("Buyurtmalar:")
    for k in lugat.keys():
        print(f"{k} --- {lugat[k]}")
        
    
            
def taomlar():
    tanlovlar = {}
    print("""
    \n__TAOMLAR__
    \n1. Osh --- 25 000 so'm
    \n2. Lagmon --- 20 000 so'm
    \n3. Shashlik --- 10 000 so'm
    \n4. Manti --- 15 000 so'm    
    \n0. Chiqish
    """)
    tanlov = int(input("Taomlardan tanlovingiz: "))
    while tanlov > 0:
        if tanlov == 1:
            tanlovlar["Osh"] = 25000
            
            print("""
            \n__TAOMLAR__
            \n1. Osh --- 25 000 so'm
            \n2. Lagmon --- 20 000 so'm
            \n3. Shashlik --- 10 000 so'm
            \n4. Manti --- 15 000 so'm    
            \n0. Chiqish
            """)
            tanlov = int(input("Taomlardan tanlovingiz: "))
        
        elif tanlov == 2:
            tanlovlar["Lagmon"] = 20000
            
            print("""
            \n__TAOMLAR__
            \n1. Osh --- 25 000 so'm
            \n2. Lagmon --- 20 000 so'm
            \n3. Shashlik --- 10 000 so'm
            \n4. Manti --- 15 000 so'm    
            \n0. Chiqish
            """)
            tanlov = int(input("Taomlardan tanlovingiz: "))
        
        elif tanlov == 3:
            tanlovlar["shashlik"] = 10000
            print("""
            \n__TAOMLAR__
            \n1. Osh --- 25 000 so'm
            \n2. Lagmon --- 20 000 so'm
            \n3. Shashlik --- 10 000 so'm
            \n4. Manti --- 15 000 so'm    
            \n0. Chiqish
            """)
            tanlov = int(input("Taomlardan tanlovingiz: "))
            
        elif tanlov == 4:
            tanlovlar["manti"] = 15000
            print("""
            \n__TAOMLAR__
            \n1. Osh --- 25 000 so'm
            \n2. Lagmon --- 20 000 so'm
            \n3. Shashlik --- 10 000 so'm
            \n4. Manti --- 15 000 so'm    
            \n0. Chiqish
            """)
            tanlov = int(input("Taomlardan tanlovingiz: "))
            
        elif tanlov == 0:
            break
        
        else:
            print("Kiritishda xatolik!!!")
            
        return tanlovlar
 
def ichimliklar():
    tanlovlar = {}
    print("""
    \n__ICHIMLIKLAR__
    \n1. Choy --- 5 000 so'm
    \n2. Pepsi --- 20 000 so'm
    \n3. Cola --- 15 000 so'm
    \n4. Aqua --- 5 000 so'm    
    \n0. Chiqish
    """)
    tanlov = int(input("Ichimliklardan tanlovingiz: "))
    while tanlov > 0:
        if tanlov == 1:
            tanlovlar["Choy"] = 25000
            
            print("""   
                \n__ICHIMLIKLAR__
                \n1. Choy --- 5 000 so'm
                \n2. Pepsi --- 20 000 so'm
                \n3. Cola --- 15 000 so'm
                \n4. Aqua --- 5 000 so'm    
                \n0. Chiqish
            """)
            tanlov = int(input("Ichimliklardan tanlovingiz: "))
        
        elif tanlov == 2:
            tanlovlar["Pepsi"] = 20000
            
            print("""   
                \n__ICHIMLIKLAR__
                \n1. Choy --- 5 000 so'm
                \n2. Pepsi --- 20 000 so'm
                \n3. Cola --- 15 000 so'm
                \n4. Aqua --- 5 000 so'm    
                \n0. Chiqish
            """)
            tanlov = int(input("Ichimliklardan tanlovingiz: "))
        
        elif tanlov == 3:
            tanlovlar["Cola"] = 15000
            
            print("""   
                \n__ICHIMLIKLAR__
                \n1. Choy --- 5 000 so'm
                \n2. Pepsi --- 20 000 so'm
                \n3. Cola --- 15 000 so'm
                \n4. Aqua --- 5 000 so'm    
                \n0. Chiqish
            """)
            tanlov = int(input("Ichimliklardan tanlovingiz: "))
            
        elif tanlov == 4:
            tanlovlar["Aqua"] = 5000
                  
            print("""   
                \n__ICHIMLIKLAR__
                \n1. Choy --- 5 000 so'm
                \n2. Pepsi --- 20 000 so'm
                \n3. Cola --- 15 000 so'm
                \n4. Aqua --- 5 000 so'm    
                \n0. Chiqish
            """)
            tanlov = int(input("Ichimliklardan tanlovingiz: "))
            
        elif tanlov == 0:
            break
        
        else:
            print("Kiritishda xatolik!!!")
 
        return tanlovlar

def shirinliklar():
    tanlovlar = {}
    print("""
    \n__SHIRINLIKLAR__
    \n1. Tort --- 5 000 so'm
    \n2. Keks --- 20 000 so'm
    \n3. Muzqaymoq --- 15 000 so'm
    \n4. Alfiretto --- 5 000 so'm    
    \n0. Chiqish
    """)
    
    tanlov = int(input("Shirinliklardan tanlovingiz: "))
    while tanlov > 0:
        if tanlov == 1:
            tanlovlar["Tort"] = 5000
                    
            print("""
            \n__SHIRINLIKLAR__
            \n1. Tort --- 5 000 so'm
            \n2. Keks --- 20 000 so'm
            \n3. Muzqaymoq --- 15 000 so'm
            \n4. Alfiretto --- 5 000 so'm    
            \n0. Chiqish
            """)
            
            tanlov = int(input("Shirinliklardan tanlovingiz: "))
        
        elif tanlov == 2:
            tanlovlar["Keks"] = 20000

            print("""
            \n__SHIRINLIKLAR__
            \n1. Tort --- 5 000 so'm
            \n2. Keks --- 20 000 so'm
            \n3. Muzqaymoq --- 15 000 so'm
            \n4. Alfiretto --- 5 000 so'm    
            \n0. Chiqish
            """)
            
            tanlov = int(input("Shirinliklardan tanlovingiz: "))
                
        elif tanlov == 3:
            tanlovlar["Muzqaymoq"] = 15000

            print("""
            \n__SHIRINLIKLAR__
            \n1. Tort --- 5 000 so'm
            \n2. Keks --- 20 000 so'm
            \n3. Muzqaymoq --- 15 000 so'm
            \n4. Alfiretto --- 5 000 so'm    
            \n0. Chiqish
            """)
            
            tanlov = int(input("Shirinliklardan tanlovingiz: "))
        
            
        elif tanlov == 4:
            tanlovlar["Alfiretto"] = 5000
                  

            print("""
            \n__SHIRINLIKLAR__
            \n1. Tort --- 5 000 so'm
            \n2. Keks --- 20 000 so'm
            \n3. Muzqaymoq --- 15 000 so'm
            \n4. Alfiretto --- 5 000 so'm    
            \n0. Chiqish
            """)
            
            tanlov = int(input("Shirinliklardan tanlovingiz: "))
        
            
        elif tanlov == 0:
            break
        
        else:
            print("Kiritishda xatolik!!!")
            
        return tanlovlar


        
