import tkinter as tk
from tkinter import messagebox


class HouseWindowedView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root

    def create_gui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        apt_frame = tk.LabelFrame(self.frame, text="Apartments", padx=5, pady=5)
        apt_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(apt_frame, text="Number:").grid(row=0, column=0)
        self.number_entry = tk.Entry(apt_frame)
        self.number_entry.grid(row=0, column=1)

        tk.Label(apt_frame, text="Floor:").grid(row=1, column=0)
        self.floor_entry = tk.Entry(apt_frame)
        self.floor_entry.grid(row=1, column=1)

        tk.Label(apt_frame, text="Rooms:").grid(row=2, column=0)
        self.rooms_entry = tk.Entry(apt_frame)
        self.rooms_entry.grid(row=2, column=1)

        tk.Button(apt_frame, text="Add Apartment", command=self.controller.add_apartment).grid(row=3, columnspan=2, pady=5)
        tk.Button(apt_frame, text="Remove Apartment", command=self.controller.remove_apartment).grid(row=4, columnspan=2, pady=5)

        res_frame = tk.LabelFrame(self.frame, text="Residents", padx=5, pady=5)
        res_frame.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(res_frame, text="Apartment Number:").grid(row=0, column=0)
        self.apt_number_entry = tk.Entry(res_frame)
        self.apt_number_entry.grid(row=0, column=1)

        tk.Label(res_frame, text="Resident Name:").grid(row=1, column=0)
        self.resident_entry = tk.Entry(res_frame)
        self.resident_entry.grid(row=1, column=1)

        tk.Button(res_frame, text="Add Resident", command=self.controller.add_resident).grid(row=2, columnspan=2, pady=5)
        tk.Button(res_frame, text="Remove Resident", command=self.controller.remove_resident).grid(row=3, columnspan=2, pady=5)

        self.listbox = tk.Listbox(self.root, width=70)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def update(self, apartments):
        self.listbox.delete(0, tk.END)
        for num, apt in apartments.items():
            self.listbox.insert(tk.END, f"{num} - Floor: {apt.floor}, Rooms: {apt.rooms}, Residents: {', '.join(apt.residents)}")

    def get_apartment_data(self):
        return self.number_entry.get(), self.floor_entry.get(), self.rooms_entry.get()

    def get_resident_data(self):
        return self.apt_number_entry.get(), self.resident_entry.get()

    def on_select(self, event):
        number = self.get_selected_apartment()
        if number:
            self.controller.get_apartment_info(number)

    def get_selected_apartment(self):
        selected = self.listbox.curselection()
        return self.listbox.get(selected[0]).split(' ')[0] if selected else None

    def display_apartment_info(self, apartment):
        if apartment:
            info = f"Apartment {apartment.number} - Floor: {apartment.floor}, Rooms: {apartment.rooms}, Residents: {', '.join(apartment.residents)}"
            messagebox.showinfo("Apartment Info", info)
        else:
            messagebox.showerror("Error", "No apartment selected")

    def show_error(self, message):
        messagebox.showerror("Error", message)
