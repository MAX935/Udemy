class Fighters:
    amount_of_fighters = 0


    @classmethod
    def get_active(cls):
        return Fighters.amount_of_fighters

##
##    @classmethod
##    def add_fighter(cls):
##        Dillashaw = cls('dsa','sfd',22,22,22,22)
##



    def __init__(self, name, last_name, age, amount_of_fights, wins, loses):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.amount_of_fights = amount_of_fights
        self.wins = wins
        self.loses = loses
        Fighters.amount_of_fighters += 1
    def out_fighters(self):
        Fighters.amount_of_fighters -= 1

    def get_name(self):
        return self.name
    def get_last_name(self):
        return self.last_name
    def get_age(self):
        return self.age
    def get_amount_of_fights(self):
        return self.amount_of_fights
    def get_wins(self):
        return self.wins
    def get_loses(self):
        return self.loses
##
##
##Cody = Fighters('Cody','Garbrant', 27, 15, 12, 3)
##print(Fighters.amount_of_fighters)
#Fighters.add_fighter()

print(Fighters.get_active())

