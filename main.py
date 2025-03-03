import tkinter as tk

from model1_exam import House
from controller_exam import HouseController
from view_exam import HouseWindowedView

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Exam task 6")
    house = House()
    view = HouseWindowedView(root, None)
    controller = HouseController(house, view)
    view.controller = controller
    view.create_gui()
    view.update(house.apartments)
    root.mainloop()
