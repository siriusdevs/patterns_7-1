class PersonCounter:
    id = 0

    def give_id(self):
        self.id += 1
        return self.id

class Person:
    def __init__(self, name: str, id_counter: PersonCounter) -> None:
        self.name = name
        self.id = id_counter.give_id(id_counter)


class Room:
    def __init__(self, name: str):
        self.name = name
        self.__users = list()

    def add(self, person: Person):
        self.__users.append(person.id)

    def remove(self, person: Person):
        if person.id in self.__users:
            self.__users.remove(person.id)
        else:
            print(f'Person {person.name} does not have acces to this room already')

    def watch_access(self):
        return self.__users

class RoomAccess:
    @staticmethod
    def get(person: Person, room: Room):
        if isinstance(person, Person) and isinstance(room, Room):
            is_not = '' if person.id in room.watch_access() else 'not '
            print(f'User {person.name} is {is_not}allowed to enter {room.name}')
        else:
            print('wrong person or room')
counter = PersonCounter
maxim = Person('Maxim', counter)
p2 = Person('Maxim', counter)
bathroom = Room('bathroom')
bathroom.add(maxim)

RoomAccess.get(maxim, bathroom)
RoomAccess.get(p2, bathroom)
RoomAccess.get(4, bathroom)