class Osoba:
    def __init__(self, imya, vik):
        self.imya = imya
        self.vik = vik

    def otrymaty_imya(self):
        return self.imya

    def otrymaty_vik(self):
        return self.vik

    def zminyty_imya(self, nove_imya):
        self.imya = nove_imya

    def zminyty_vik(self, noviy_vik):
        self.vik = noviy_vik

    def informaciya(self):
        print("Ім'я:", self.imya)
        print("Вік:", self.vik)


class Transport:
    def __init__(self, nazva, typ, shvydkist):
        self.nazva = nazva
        self.typ = typ
        self.shvydkist = shvydkist
        self.ruhayetsya = False

    def start(self):
        self.ruhayetsya = True

    def stop(self):
        self.ruhayetsya = False

    def status(self):
        if self.ruhayetsya:
            print("Транспорт рухається")
        else:
            print("Транспорт стоїть")

    def informaciya(self):
        print("Назва:", self.nazva)
        print("Тип:", self.typ)
        print("Швидкість:", self.shvydkist)


class Vodiy(Osoba):
    def __init__(self, imya, vik, posvidchennya):
        super().__init__(imya, vik)
        self.posvidchennya = posvidchennya
        self.keruye = False

    def otrymaty_posvidchennya(self):
        return self.posvidchennya

    def mozhe_keruvaty(self):
        return self.vik >= 18

    def pochaty_keruvannya(self):
        if self.mozhe_keruvaty():
            self.keruye = True
            print(self.imya, "може керувати")
        else:
            print(self.imya, "не може керувати, бо менше 18 років")

    def zupynyty_keruvannya(self):
        if self.keruye:
            self.keruye = False
            print(self.imya, "зупинив керування")
        else:
            print("Керування не було розпочато")

    def keruvaty(self, transport):
        if self.mozhe_keruvaty():
            self.pochaty_keruvannya()
            transport.start()
            transport.informaciya()
            transport.status()
        else:
            print("Керування заборонено")

    def informaciya(self):
        super().informaciya()
        print("Посвідчення:", self.posvidchennya)


auto = Transport("Toyota", "Авто", 200)
bus = Transport("Volvo", "Автобус", 160)

vodiy1 = Vodiy("Діма", 20, "AA123123")
vodiy2 = Vodiy("Максим", 16, "BB321321")

vodiy1.informaciya()
vodiy1.keruvaty(auto)
vodiy1.zupynyty_keruvannya()

vodiy2.informaciya()
vodiy2.keruvaty(bus)
vodiy2.zupynyty_keruvannya()