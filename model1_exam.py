import json


class Apartment:
    def __init__(self, number, floor, rooms):
        self.number = number
        self.floor = floor
        self.rooms = rooms
        self.residents = []

    def add_resident(self, resident):
        if resident not in self.residents:
            self.residents.append(resident)

    def remove_resident(self, resident):
        if resident in self.residents:
            self.residents.remove(resident)

    def to_dict(self):
        return {
            "floor": self.floor,
            "rooms": self.rooms,
            "residents": self.residents
        }

    @classmethod
    def from_dict(cls, number, data):
        apt = cls(number, data["floor"], data["rooms"])
        apt.residents = data.get("residents", [])
        return apt


class House:
    DATA_FILE = "house_data.json"

    def __init__(self):
        self.apartments = self.load_data()
        self.observers = []

    def load_data(self):
        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return {num: Apartment.from_dict(num, info) for num, info in data.items()}
        except FileNotFoundError:
            return {}

    def save_data(self):
        data = {num: apt.to_dict() for num, apt in self.apartments.items()}
        with open(self.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        self.notify_observers()

    def add_apartment(self, number, floor, rooms):
        if number not in self.apartments:
            self.apartments[number] = Apartment(number, floor, rooms)
            self.save_data()

    def remove_apartment(self, number):
        if number in self.apartments:
            del self.apartments[number]
            self.save_data()

    def add_resident(self, number, resident):
        if number in self.apartments:
            self.apartments[number].add_resident(resident)
            self.save_data()

    def remove_resident(self, number, resident):
        if number in self.apartments:
            self.apartments[number].remove_resident(resident)
            self.save_data()

    def get_apartment_info(self, number):
        return self.apartments.get(number)

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.apartments)
