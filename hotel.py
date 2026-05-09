from tkinter import *
from customer import Customer
from room import RoomBooking
from details import DetailsRoom

class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#000000")

        # Header
        lbltitle = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), 
                         bg="#000000", fg="#D4AF37", bd=0)
        lbltitle.place(x=0, y=0, relwidth=1, height=80)
        Frame(self.root, bg="#D4AF37").place(x=0, y=80, relwidth=1, height=3)

        # Main Workspace Frame
        self.main_frame = Frame(self.root, bd=0, bg="#000000")
        self.main_frame.place(x=250, y=83, width=1300, height=717)

        # Sidebar Menu
        side_menu = Frame(self.root, bd=0, bg="#1C1C1C")
        side_menu.place(x=0, y=83, width=250, height=717)

        Label(side_menu, text="NAVIGATION", font=("arial", 12, "bold"), bg="#1C1C1C", fg="gray").pack(pady=20)

        # Modern Sidebar Buttons
        def create_menu_btn(text, cmd):
            btn = Button(side_menu, text=text, command=cmd, font=("arial", 13, "bold"), 
                         bg="#1C1C1C", fg="#D4AF37", bd=0, cursor="hand2", activebackground="#D4AF37", 
                         activeforeground="black", anchor="w", padx=30)
            btn.pack(fill=X, pady=5, ipady=10)
            return btn

        create_menu_btn("  CUSTOMER", self.cust_details)
        create_menu_btn("  ROOM BOOKING", self.room_booking)
        create_menu_btn("  ROOM DETAILS", self.details_room)
        create_menu_btn("  LOGOUT", self.logout)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer(self.new_window)

    def room_booking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagement(root)
    root.mainloop()