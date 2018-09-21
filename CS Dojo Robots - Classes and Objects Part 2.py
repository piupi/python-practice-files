#class
class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
        
    def introduce_self(self):
        print("My name is " + self.name)

#the objects in the class
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

#stuff youre making the objects do
r1.introduce_self()
r2.introduce_self()



#another class
class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

#new objects for the new class Person
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

#we wanna show that p1 owns r2
p1.robot_owned = r2
#that defines a new attribute in p1 called
#robot_owned and sets it to r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
