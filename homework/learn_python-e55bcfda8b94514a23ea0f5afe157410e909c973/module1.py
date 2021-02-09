class Swimmable:
    def __init__(self, name):
        print('Init Swimmable')
        self.name = name

    def greeting(self):
        print('Hello, my name is {} and I can swim!'.format(self.name))


class Walkable:
    def __init__(self, name):
        print('Init Walkable')
        self.name = name

    def greeting(self):
        print('Hello, my name is {} and I can walk!'.format(self.name))


class Flyable:
    def __init__(self, name):
        print('Init Flyable')
        self.name = name

    def greeting(self):
        print('Hello, my name is {} and I can fly!'.format(self.name))



class GameCharacter(Walkable, Flyable, Swimmable):
    def __init__(self,name):
        print('Init GameCharacter')
        self.name = name
        Walkable.__init__(self,name)
        Swimmable.__init__(self, name)
        Flyable.__init__(self,name)


    def greeting(self):
        print('Hello, my name is {}'.format(self.name))


james = GameCharacter('James')
print(isinstance(james,Flyable))

print(isinstance(5,str))
