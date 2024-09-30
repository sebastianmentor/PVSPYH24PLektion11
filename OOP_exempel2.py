class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Privat attribut, namnmanglat
        # self._lösenord = ''

    # Getter och setter för det privata attributet
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Ålder måste vara positiv!")

    def __str__(self):
        return f"Mitt namn är {self.name*20} och jag är {self.__age} gammal!"

    # def __repr__(self) -> str:
    #     return f"Person({self.name}, {self.__age})"

person = Person("Bob", 25)

# Vi kan inte direkt komma åt __age, vilket är meningen
# print(person.__age)  # Detta ger ett felmeddelande


# Men vi kan använda gettern och settern för att interagera med det
print(person.get_age())  # 25
info = str(person)
print(info)

# För att komma åt __age behöver vi veta name mangling
# print(person._Person__age) # Kommer fungera men ska aldrig användas på detta viset!