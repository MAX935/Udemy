##class Cars:
##    wheels_number = 4
##
##    def __init__(self, name, color, year, is_crashed):
##        self.name = name
##        self.color = color
##        self.year = year
##        self.is_crashed = is_crashed
##        print('Car is created')
##
##
##    def drive(self, city):
##        print(self.name + ' is driving to ' + city)
##
##    def change_color(self, new_color):
##        self.color = new_color
##
##
##class Cargo(Cars):
##
##    wheels_number = 6
##    def __init__(self, name, color, year, is_crashed):
##        Cars.__init__(self, name,color, year, is_crashed)
##        print('Cargo is created')
##
##    def drive(self,city):
##        print(self.name + ' is ebashing to ' + city)
##
##
##    def load_weight(self, weight):
##        print(self.name + ' is going ' + str(weight))
##
##
##truck = Cargo('Mann','white',2010,False)
##truck.drive('Moscow')
##print(Cargo.wheels_number)
##truck.drive('Piter')
##truck.load_weight(142)

#1 zadanie
class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level


    def speak(self):
        print('Hi, my name is {}'.format(self.name))

obj = GameCharacter('Max','ok', 14)
obj.speak()


#2 zadanie


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print('Hi, my name is {}, and i will kill you'.format(self.name))

    def kill(self, gc_obj):
        gc_obj.health = 0
        print('Bang-bang, now you\'re dead')

obj1 = Villain('John','normal', 132)

obj1.speak()

obj1.kill(obj)




