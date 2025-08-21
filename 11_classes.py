class MyPerson:
    pass

print(MyPerson)
print(MyPerson())

class Person:

    def  __init__(self, name, surname):
        self.name = name
        self.surname = surname


my_person = Person("Silvia", "Fuentes")
print(my_person.name)