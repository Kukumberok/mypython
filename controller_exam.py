class HouseController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.add_observer(view)

    def add_apartment(self):
        number, floor, rooms = self.view.get_apartment_data()
        if not number and not floor and not rooms:
            print("All fields are required!")
            return
        try:
            floor = int(floor)
            rooms = int(rooms)
            if rooms <= 0:
                rooms = "1"
                print("at least one room!!!")
        except ValueError:
            self.view.show_error("Floors and rooms should be numbers!")
            return

        self.model.add_apartment(number, floor, rooms)

    def remove_apartment(self):
        number = self.view.get_selected_apartment()
        if number:
            self.model.remove_apartment(number)

    def add_resident(self):
        number, resident = self.view.get_resident_data()
        if number and resident:
            self.model.add_resident(number, resident)

    def remove_resident(self):
        number, resident = self.view.get_resident_data()
        if number and resident:
            self.model.remove_resident(number, resident)

    def get_apartment_info(self, number):
        apt = self.model.get_apartment_info(number)
        if apt:
            self.view.display_apartment_info(apt)
        else:
            self.view.show_error("ApartmentNotFoundError")

    def update(self):
        apartments = self.model.apartments
        self.view.update(apartments)


