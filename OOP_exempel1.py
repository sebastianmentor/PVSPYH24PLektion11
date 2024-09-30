class Ålder:
    def __init__(self, number) -> None:
        if not isinstance(number,int) and number < 0: 
            raise ValueError('Måste vara positiv integer')
        self._age = number

    def __str__(self) -> str:
        return str(self._age)
    
    def __int__(self) -> int:
        return self._age


class Person: 

    EGENSKAPER = ("Snäll", "Elak", "Dum", "Smart", "Rolig")
    
    def __init__(self, name, age:Ålder):
        self.name = name          # Publikt attribut
        self._age = age 
        self._secrets = []           # Skyddat attribut (ska inte ändras direkt)

    # Getter för att hämta värdet på _age
    def get_age(self):
        return self._age
    
    def is_ålder(self, ålder):
        return True if 123 >= ålder >= 0 else False 

    # Setter för att uppdatera värdet på _age, med validering
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Ålder måste vara positiv!")

    def get_secrets(self):
        new_list = []
        for item in self._secrets:
            new_list.append(item)
        
        return new_list
        return self._secrets.copy()
    
    def print_secrets(self):
        for secret in self._secrets:
            print(secret)

# Användning av klassen
ålder = Ålder(20)
print(ålder)
int(ålder)
p = Person("Kalle", ålder)
person = Person("Alice", 30)

# Vi kan direkt få tillgång till det publika attributet
print(person.name)  # Alice

# Vi bör inte direkt få tillgång till _age, även om det är möjligt
print(person._age)  # 30 (ska egentligen inte göras)
age = person.get_age()
age = 20
print(person._age)

secrets = person.get_secrets()
print(secrets)
secrets.append("New secret!!")
person.print_secrets()

# # Använd getter och setter för att få och sätta _age
# print(person.get_age())  # 30
# person.set_age(35)       # Uppdaterar åldern till 35
# print(person.get_age())  # 35
# person.set_age(-5)       # Ogiltigt värde, åldern uppdateras inte
