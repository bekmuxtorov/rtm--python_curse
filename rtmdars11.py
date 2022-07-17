"""
Created on 2022-07-17 16:06:58.990923

@author: Asadbek Muxtorov
        github.com\bekmuxtorov

@mavzu: Random moduli bilan ishlash
1. sample(royhat, a) - ro'yhatdan a ta miqdordagi qiymatlarni tanlaydi
"""
"""============================== 1 - masala ============================== """
# from random import sample
# # sample(royhat, a) -- royhatdan a ta elementni ixtiyoriy tanlab beradi.
#
# nums = list(range(100, 1000))
# sonlar=(sample(nums, 3))
# print(sonlar)

"""============================== 2 - masala ============================== """
# from random import randrange
# # randrange(boshi, ohiri, qadam) -- boshi'dan boshlab ohiri'gacha bo'lgan qadam'da joylashgan ixtiyoriy bittasonini tanlab beradi
#
# a = randrange(1, 100, 1)
# print(a)

"""============================== 3 - masala ============================== """
# from random import randint
# # randint(a, b) -- a va b oraliqdagi ixtiyoriy soni tanlab beradi
# matn = "12345678890!@#$%^&*"
# a = matn[randint(0, len(matn))]
# print(a)

"""============================== 4 - masala ============================== """
# from random import randint
#
# a = randint(1, 31)
# print(a)

"""============================== 5 - masala ============================== """
# from random import randint
# tasodifiy_son = randint(1,100)
# print(tasodifiy_son)
# tanlov = int(input("Tahminingizni kiriting: "))
#
# while True:
#     if tanlov == tasodifiy_son:
#         result = "Tahminingiz tog'ri. Malades topdiz.👍"
#         print(result)
#         break
#     elif tanlov < tasodifiy_son:
#         result = "Tahminingiz kichik, qayta urinib ko'ring.👀"
#         print(result)
#         tanlov = int(input("Tahminingizni kiriting: "))
#     elif tanlov > tasodifiy_son:
#         result = "Tahminingiz katta, qayta urinib ko'ring.👀 "
#         print(result)
#         tanlov = int(input("Tahminingizni kiriting: "))
#


"""============================== 6 - masala ============================== """

from random import randint,choice
def matem():
    trues = []
    falses = []
    print(f"""__MENU__
    \n1 -- Qo'shish
    \n2 -- Ayrish
    \n3 -- Ko'paytirish
    \n4 -- Bo'lish
    \n5 -- Aralash
    \n0 -- Natija
    """)
    tanlov = int(input("Tanlovingizni kiriting: "))
    while tanlov != 0:
        if tanlov == 1:
            t,f = qoshish()
            trues = [i for i in t]
            falses = [j for j in f]
            print(f"""__MENU__
            \n1 -- Qo'shish
            \n2 -- Ayrish
            \n3 -- Ko'paytirish
            \n4 -- Bo'lish
            \n5 -- Aralash
            \n0 -- Natija
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))

        elif tanlov == 2:
            ayrish()
            print(f"""__MENU__
            \n1 -- Qo'shish
            \n2 -- Ayrish
            \n3 -- Ko'paytirish
            \n4 -- Bo'lish
            \n5 -- Aralash
            \n0 -- Natija
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))


        elif tanlov == 3:
            kopaytirish()
            print(f"""__MENU__
            \n1 -- Qo'shish
            \n2 -- Ayrish
            \n3 -- Ko'paytirish
            \n4 -- Bo'lish
            \n5 -- Aralash
            \n0 -- Natija
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))

        elif tanlov == 4:
            bolish()
            print(f"""__MENU__
            \n1 -- Qo'shish
            \n2 -- Ayrish
            \n3 -- Ko'paytirish
            \n4 -- Bo'lish
            \n5 -- Aralash
            \n0 -- Natija
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))

        elif tanlov == 5:
            aralash()
            print(f"""__MENU__
            \n1 -- Qo'shish
            \n2 -- Ayrish
            \n3 -- Ko'paytirish
            \n4 -- Bo'lish
            \n5 -- Aralash
            \n0 -- Natija
            """)
            tanlov = int(input("Tanlovingizni kiriting: "))

        else:
            print("Kiritishda xatolik")
            tanlov = int(input("Qayta kiriting: "))
    print(f"Tog'ri javoblaringiz: {len(trues)} ball. ")
    for true in trues:
        print(true)

    print("Xato javoblaringiz: ")
    for false in falses:
        print(false)
def qoshish():
    true = []
    false = []
    i = 4
    while True:
        if i == 0:
            break
        a = randint(1, 100)
        b = randint(1, 100)
        javob = int(input(f"{a} + {b} = "))
        if javob == (a+b):
            true.append(f"{a} + {b} = {javob} ✔")
        else:
            false.append(f"{a} + {b} = {javob} ❓")

        i -= 1

    return true, false

def ayrish():
    true = []
    false = []
    i = 4
    while True:
        if i == 0:
            break
        a = randint(100, 200)
        b = randint(1, 100)
        javob = int(input(f"{a} - {b} = "))
        if javob == (a - b):
            true.append(f"{a} - {b} = {javob} ✔")
        else:
            false.append(f"{a} - {b} = {javob} ❓")

        i -= 1

    return true, false

def kopaytirish():
    true = []
    false = []
    i = 4
    while True:
        if i == 0:
            break
        a = randint(1, 20)
        b = randint(1, 20)
        javob = int(input(f"{a} * {b} = "))
        if javob == (a * b):
            true.append(f"{a} * {b} = {javob} ✔")
        else:
            false.append(f"{a} * {b} = {javob} ❓")

        i -= 1

    return true, false

def bolish():
    true = []
    false = []
    i = 4
    while True:
        if i == 0:
            break
        a = randint(100, 200)
        b = randint(1, 100)
        javob = int(input(f"{a} / {b} = "))
        if javob == (a / b):
            true.append(f"{a} / {b} = {javob} ✔")
        else:
            false.append(f"{a} / {b} = {javob} ❓")

        i -= 1

    return true, false

matem()


