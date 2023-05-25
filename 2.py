class Person:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

class Room:
    def __init__(self, name: str):
        self.name = name
        self._users = []

    def add(self, person: Person) -> None:
        self._users.append(person.id)

    def remove(self, person: Person) -> None:
        if person.id in self._users:
            self._users.remove(person.id)

class RoomAccess:
    @staticmethod
    def get(person: Person, room: Room) -> None:
        if person.id in room._users:
            print(f"Пользователю {person.name} предоставлен доступ в комнату {room.name}")
        else:
            print(f"Пользователю {person.name} не предоставлен доступ в комнату {room.name}")

slavic = Person("Slavic", 122)
abdulah = Person("Abdullah", 111)
plane = Room("самолет")

plane.add(slavic)
RoomAccess.get(slavic, plane)
RoomAccess.get(abdulah, plane)
