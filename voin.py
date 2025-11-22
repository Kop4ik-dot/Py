class Character:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def attack(self):
        print("Персонаж атакує")

    def take_damage(self):
        print("Персонаж отримує урон")
class Voin(Character):
    def __init__(self, name, hp, dmg):
         super().__init__(name, hp, dmg)

    def take_damage(self):
        if self.hp <= 0:
            print("Voin dead")
        else:
            print("Voin ne dead")
    def attack(self):
        choise = int(input("Кого хочеш атакувати? (1 - Warrior, 2 - Mag)"))
        if (choise == 1):
            print("Ти атакуєш Warrior")

            if (self.hp >= 100):
                print("Ти ваншотнув Warrior")
            else:
                print("Ти завдав шкоди Warrior")
                self.hp = self.hp - 20


        if(choise == 2):
            print("Ти атакуєш Mag")

            if (self.hp >= 100):
                    print("Ти ваншотнув Mag")
            else:
                    print("Ти завдав шкоди Mag")
                    self.hp = self.hp - 40


class Warrior(Character):
    def __init__(self, name, hp, dmg):
         super().__init__(name, hp, dmg)

    def take_damage(self):
        if self.hp <= 0:
            print("Warrior dead")
        else:
            print("Warrior ne dead")
    def attack(self):
        choise = int(input("Кого хочеш атакувати? (1 - Voin, 2 - Mag)"))
        if (choise == 1):
            print("Ти атакуєш Voin")

            if (self.hp >= 100):
                print("Ти ваншотнув Voin")
            else:
                print("Ти завдав шкоди Voin")

        if(choise == 2):
            print("Ти атакуєш Mag")

            if (self.hp >= 100):
                    print("Ти ваншотнув Mag")
            else:
                    print("Ти завдав шкоди Mag")
                    self.hp = self.hp - 40

class Mag(Character):
    def __init__(self, name, hp, dmg, mana):
         super().__init__(name, hp, dmg)
         self.mana = mana

    def take_damage(self):
        if self.hp <= 0:
            print("Mag dead")
        else:
            print("Mag ne dead")
    def attack(self):
        choise = int(input("Кого хочеш атакувати? (1 - Voin, 2 - Warrior)"))
        if (choise == 1):
            print("Ти атакуєш Voin")

            if (self.hp >= 100):
                print("Ти ваншотнув Voin")
            else:
                print("Ти завдав шкоди Voin")
            self.hp = self.hp - 20

        if(choise == 2):
            print("Ти атакуєш Warrior")

            if (self.hp >= 100):
                    print("Ти ваншотнув Warrior")
            else:
                    print("Ти завдав шкоди Warrior")
                    self.hp = self.hp - 40


voin = Voin("Voin", 80, 30)
voin.attack()
voin.take_damage()
warrior = Warrior("Warrior", 60, 30)
warrior.attack()
warrior.take_damage()
mag = Mag("Mag", 50, 30, 20)
mag.attack()
mag.take_damage()