class Person: 
    antal_personer_skapade = 0
    EGENSKAPER = ("Snäll", "Elak", "Dum", "Smart", "Rolig")

    def __init__(self, name, age, egenskap):
        self.name = name          # Publikt attribut
        self._age = age         # Skyddat attribut (ska inte ändras direkt) 
        self._egenskap = egenskap
        Person.antal_personer_skapade += 1
        # self.antal_personer_skapade += 1
    
    def get_egenskap(self):
        return self._egenskap
    
    def set_egenskap(self, egenskap):
        if egenskap in self.EGENSKAPER:
            self._egenskap = egenskap

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
    

person = Person("Alice", 30, "Rolig")

print(person.get_egenskap())
person.set_egenskap("Dum")
print(person.get_egenskap())

person = Person("Kalle", 30, "Elak")

print(Person.antal_personer_skapade)