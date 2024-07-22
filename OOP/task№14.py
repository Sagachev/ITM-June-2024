# Напишите класс, который принимает список людей с интерфейсом добавления новых и при итерации возвращал имена людей
class PeopleList:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.people):
            person = self.people[self._index]
            self._index += 1
            return person
        else:
            raise StopIteration

people_list = PeopleList()

people_list.add_person("Biba")
people_list.add_person("Boba")

for person in people_list:
    print(person)