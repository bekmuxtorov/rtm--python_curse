# """
# Created on 2022-07-27 17:40:12.596544

# @author: Asadbek Muxtorov

# @mavzu: Class(sinflar)

# """

class Transport:
    def __init__(self, tezlik, sarf):
        self.tezlik = tezlik
        self.sarf = sarf

class Users:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def get_info(self):
        print(f"Ism: {self.name.title()}\n"
              f"Foydalanuvchi ismi: {self.username}\n"
              f"Email:: {self.email}\n")


# user1 = Users('Asadbek', 'bekmuxtorov', 'asadbekmuxtorov2@gmail.com')
# user1.get_info()

class Avto:
    def __init__(self, model, rang, korobka, narx, kilometr = 0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.kilometr = 0

    def get_model(self):
        return self.model

    def get_rang(self):
        return self.rang

    def get_korobka(self):
        return self.korobka

    def get_narx(self):
        return self.narx

    def get_info(self):
        return f"Model: {self.model}\n" \
               f"Rang: {self.rang}\n" \
               f"Korobka: {self.korobka}\n" \
               f"Narx: {self.narx}\n" \
               f"Kilometr: {self.kilometr}"

    def set_kilometr(self, km):
        return (self.kilometr + km)

# moshin1 = Avto('Malibu', 'qora', 'avtomat', 40_000)
# print(moshin1.get_info())
# moshin1.kilometr

class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.cars = []

    def get_nomi(self):
        return self.nomi

    def get_manzili(self):
        return self.manzili

    def get_cars(self):
        return self.cars

    def get_cars(self, *args):
        for arg in args:
            self.cars.append(arg)

salon1 = Avtosalon('Chevralet', 'Quva')
print(salon1.get_nomi())
salon1.get_cars('Malibu', 'Tiko', 'Matiz')
print(salon1.cars)


