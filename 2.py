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

    def __init__(self, name: str, id: int) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return self.name

class Room:

    def __init__(self, name: str) -> None:
        self.name = name
        self.__users = []

    def add(self, person : Person):
        self.__users.append(person.id)

    def remove(self, person : Person):
        self.__users.remove(person.id)

    def __str__(self) -> str:
        return self.name
    
    @property
    def users(self):
        return self.__users
    
class RoomAccess:

    @staticmethod
    def get(person: Person, room: Room) -> None:
        if person.id in room.users:
            print(f'пользователю {person} предоставлен доступ в комнату {room}')
        else:
            print(f'пользователю {person} не предоставлен доступ в комнату {room}')

max = Person('Max', 1)
classroom = Room('classroom')
classroom.add(max)
kirill = Person('Kirill', 2)
RoomAccess.get(max, classroom)
RoomAccess.get(kirill, classroom)