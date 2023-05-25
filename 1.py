# Написать следующую структуру классов: 

# Есть класс Person, описывающий человека. У человека есть свойства: 
# 	name: str - имя 
# 	id: int – id 

# Есть класс Room, который описывает помещение. Оно имеет свойство: 
# 	name: str - название помещения. 
# 	Также у любого помещения есть скрытое свойство: 
# 	users: list[int], которое хранит список id всех людей, у которых есть допуск к этому помещению.  
# 	Редактируется этот список только с помощью внешних методов 
# 	add(person: Person) -> None и remove(person: Person) -> None, 
#     которые добавляют и удаляют людей в пользователи комнаты соответственно. 

# Использовать паттерн Заместитель (Proxy) и написать класс RoomAccess 
# со статическим 	методом get(person: Person, room: Room) -> None, 
# который выводит сообщение формата 
# “пользователю {name} [не] предоставлен доступ в комнату {room name}”. 

class Person:
     
    def __init__(self, name, id) -> None:
        self.name: str = name
        self.id: int = id

class Room:

    _users: list[int] = []

    def __init__(self, name):
        self.name: str = name

    def add(self, person: Person) -> None:
        self._users.append(person.id)

    def remove(self, person: Person) -> None:
        try:
            self._users.remove(person.id)
        except ValueError:
            pass

class RoomAccess:

    @staticmethod
    def get(person: Person, room: Room) -> None:
        if person.id in room._users:
            print(f"пользователю {person.name} предоставлен доступ в комнату {room.name}")
        else:
            print(f"пользователю {person.name} не предоставлен доступ в комнату {room.name}")
    

pers1 = Person('Poni', 1)
pers2 = Person('Grifon', 2)

room = Room('Stoika')
room.add(pers1)

RACS = RoomAccess.get(pers1, room)
RACS = RoomAccess.get(pers2, room)
room.remove(pers2)
RACS = RoomAccess.get(pers1, room)