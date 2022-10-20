class Parent:
    def can_sing(self):
        print("Sing a song")


father = Parent()
father.can_sing()

class Child(Parent):
    def can_dance(self):
        print("Let's Dance")

child1 = Child()
child1.can_sing()
child1.can_dance()
