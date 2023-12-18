from datetime import datetime

class Workers:
    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def complete_name(self):
        return f'{self.name} {self.last_name}'

    def actual_age(self):
        actual_year = datetime.now().year
        return actual_year - self.birth_year


user1 = Workers('Thiago', 'Faria', 2004)
user2 = Workers('Bruna', 'Alves', 2003)

print(user1.complete_name())
print(Workers.complete_name(user1))
print(user2.actual_age())
print(Workers.actual_age(user2))

