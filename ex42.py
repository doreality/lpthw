"""
ex42.py Is-A, Has-A, 对象和类
"""


class Animal(object):
    """Animal is-a object"""
    pass


class Dog(Animal):
    """Dog is-a Animal"""

    def __init__(self, name):
        # Dog has-a name
        self.name = name


class Cat(Animal):
    """Cat is-a Animal"""

    def __init__(self, name):
        # Cat has-a name
        self.name = name


class Person(object):
    """Person is-a object"""

    def __init__(self, name):
        # Person has-a name
        self.name = name
        # Person has-a pet of some kind
        self.pet = None


class Employee(Person):
    """Employee is-a Person"""

    def __init__(self, name, salary):
        # ??
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


class Fish(object):
    """Fish is-a object"""
    pass


class Salmon(Fish):
    """Salmon is-a Fish"""
    pass


class Halibut(Fish):
    """Halibut is-a Fish"""
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet that is satan
mary.pet = satan

# frank is-a Employee whose name is Frank and has salary of 120000
frank = Employee("Frank", 120000)

# frank has-a pet that is rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
