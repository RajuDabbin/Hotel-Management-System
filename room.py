from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector
from datetime import datetime


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Room Booking")
        self.root.geometry("1295x550+230+220")

        # ================= VARIABLES =================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_totalpaid = StringVar()

        # ================= TITLE =================
        lbl_title = Label(
            self.root,
            text="ROOM BOOKING DETAILS",
            font=("times new roman", 18, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ================= LEFT FRAME =================
        labelframeleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Room Booking Details",
            font=("times new roman", 12, "bold"),
            padx=2
        )
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ================= CONTACT =================
        lbl_contact = Label(
            labelframeleft,
            text="Contact",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_contact.grid(row=0, column=0, sticky=W)

        entry_contact = Entry(
            labelframeleft,
            textvariable=self.var_contact,
            font=("arial", 13, "bold"),
            width=20
        )
        entry_contact.grid(row=0, column=1)

        # ================= CHECK-IN =================
        lbl_checkin = Label(
            labelframeleft,
            text="Check-in Date",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_checkin.grid(row=1, column=0, sticky=W)

        txt_checkin = DateEntry(
            labelframeleft,
            textvariable=self.var_checkin,
            font=("arial", 12, "bold"),
            width=18,
            date_pattern="dd/mm/yyyy"
        )
        txt_checkin.grid(row=1, column=1)

        # ================= CHECK-OUT =================
        lbl_checkout = Label(
            labelframeleft,
            text="Check-out Date",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_checkout.grid(row=2, column=0, sticky=W)

        txt_checkout = DateEntry(
            labelframeleft,
            textvariable=self.var_checkout,
            font=("arial", 12, "bold"),
            width=18,
            date_pattern="dd/mm/yyyy"
        )
        txt_checkout.grid(row=2, column=1)

        # ================= ROOM TYPE =================
        lbl_room_type = Label(
            labelframeleft,
            text="Room Type",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_room_type.grid(row=3, column=0, sticky=W)

        combo_room_type = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_roomtype,
            font=("arial", 12, "bold"),
            width=18,
            state="readonly"
        )

        combo_room_type["values"] = (
            "Single",
            "Double",
            "Luxury"
        )

        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)

        # ================= ROOM NUMBER =================
        lbl_room = Label(
            labelframeleft,
            text="Available Room",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_room.grid(row=4, column=0, sticky=W)

        txt_room = Entry(
            labelframeleft,
            textvariable=self.var_roomavailable,
            font=("arial", 13, "bold"),
            width=20
        )
        txt_room.grid(row=4, column=1)

        # ================= MEAL =================
        lbl_meal = Label(
            labelframeleft,
            text="Meal",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_meal.grid(row=5, column=0, sticky=W)

        combo_meal = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_meal,
            font=("arial", 12, "bold"),
            width=18,
            state="readonly"
        )

        combo_meal["values"] = (
            "Breakfast",
            "Lunch",
            "Dinner",
            "All"
        )

        combo_meal.current(0)
        combo_meal.grid(row=5, column=1)

        # ================= DAYS =================
        lbl_days = Label(
            labelframeleft,
            text="No Of Days",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_days.grid(row=6, column=0, sticky=W)

        txt_days = Entry(
            labelframeleft,
            textvariable=self.var_noofdays,
            font=("arial", 13, "bold"),
            width=20,
            state="readonly"
        )
        txt_days.grid(row=6, column=1)

        # ================= TAX =================
        lbl_tax = Label(
            labelframeleft,
            text="Paid Tax",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_tax.grid(row=7, column=0, sticky=W)

        txt_tax = Entry(
            labelframeleft,
            textvariable=self.var_paidtax,
            font=("arial", 13, "bold"),
            width=20,
            state="readonly"
        )
        txt_tax.grid(row=7, column=1)

        # ================= SUBTOTAL =================
        lbl_total = Label(
            labelframeleft,
            text="Sub Total",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_total.grid(row=8, column=0, sticky=W)

        txt_total = Entry(
            labelframeleft,
            textvariable=self.var_actualtotal,
            font=("arial", 13, "bold"),
            width=20,
            state="readonly"
        )
        txt_total.grid(row=8, column=1)

        # ================= TOTAL =================
        lbl_paid = Label(
            labelframeleft,
            text="Total Cost",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_paid.grid(row=9, column=0, sticky=W)

        txt_paid = Entry(
            labelframeleft,
            textvariable=self.var_totalpaid,
            font=("arial", 13, "bold"),
            width=20,
            state="readonly"
        )
        txt_paid.grid(row=9, column=1)

        # ================= BILL BUTTON =================
        btnBill = Button(
            labelframeleft,
            text="Bill",
            command=self.total_cost,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=10
        )
        btnBill.grid(row=10, column=0, padx=1, pady=10)

        # ================= BUTTON FRAME =================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=430, width=412, height=40)

        Button(
            btn_frame,
            text="Add",
            command=self.add_data,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=9
        ).grid(row=0, column=0)

        Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=9
        ).grid(row=0, column=1)

        Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=9
        ).grid(row=0, column=2)

        Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=9
        ).grid(row=0, column=3)

        # ================= TABLE FRAME =================
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=435, y=50, width=850, height=490)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(
            table_frame,
            columns=(
                "contact",
                "checkin",
                "checkout",
                "roomtype",
                "room",
                "meal",
                "days"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        headings = {
            "contact": "Contact",
            "checkin": "Check-In",
            "checkout": "Check-Out",
            "roomtype": "Room Type",
            "room": "Room",
            "meal": "Meal",
            "days": "Days"
        }

        for col, txt in headings.items():
            self.room_table.heading(col, text=txt)
            self.room_table.column(col, width=110)

        self.room_table["show"] = "headings"

        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # ================= DATABASE =================
    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="raju01",
            database="hotel_system"
        )

    # ================= TOTAL COST =================
    def total_cost(self):
        try:
            in_date = datetime.strptime(
                self.var_checkin.get(),
                "%d/%m/%Y"
            )

            out_date = datetime.strptime(
                self.var_checkout.get(),
                "%d/%m/%Y"
            )

            days = abs((out_date - in_date).days)

            self.var_noofdays.set(str(days))

            if self.var_roomtype.get() == "Single":
                price = 1000

            elif self.var_roomtype.get() == "Double":
                price = 2000

            else:
                price = 3000

            subtotal = days * price

            tax = subtotal * 0.18

            total = subtotal + tax

            self.var_actualtotal.set(f"Rs. {subtotal}")
            self.var_paidtax.set(f"Rs. {tax}")
            self.var_totalpaid.set(f"Rs. {total}")

        except Exception as es:
            messagebox.showerror(
                "Error",
                f"{str(es)}"
            )

    # ================= ADD =================
    def add_data(self):

        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error",
                "Contact is required"
            )
            return

        try:
            conn = self.connect_db()

            my_cursor = conn.cursor()

            query = """
            INSERT INTO room(
                contact,
                checkin,
                checkout,
                roomtype,
                roomavailable,
                meal,
                noofdays
            )
            VALUES(%s,%s,%s,%s,%s,%s,%s)
            """

            values = (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get()
            )

            my_cursor.execute(query, values)

            conn.commit()

            self.fetch_data()

            conn.close()

            messagebox.showinfo(
                "Success",
                "Room Booked Successfully"
            )

        except Exception as es:
            messagebox.showerror(
                "Error",
                f"{str(es)}"
            )

    # ================= FETCH =================
    def fetch_data(self):

        try:
            conn = self.connect_db()

            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM room")

            rows = my_cursor.fetchall()

            self.room_table.delete(
                *self.room_table.get_children()
            )

            for row in rows:
                self.room_table.insert("", END, values=row)

            conn.close()

        except Exception as es:
            print(es)

    # ================= GET CURSOR =================
    def get_cursor(self, event=""):

        cursor_row = self.room_table.focus()

        content = self.room_table.item(cursor_row)

        row = content["values"]

        if row:
            self.var_contact.set(row[0])
            self.var_checkin.set(row[1])
            self.var_checkout.set(row[2])
            self.var_roomtype.set(row[3])
            self.var_roomavailable.set(row[4])
            self.var_meal.set(row[5])
            self.var_noofdays.set(row[6])

    # ================= UPDATE =================
    def update_data(self):

        try:
            conn = self.connect_db()

            my_cursor = conn.cursor()

            query = """
            UPDATE room SET
            checkin=%s,
            checkout=%s,
            roomtype=%s,
            roomavailable=%s,
            meal=%s,
            noofdays=%s
            WHERE contact=%s
            """

            values = (
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()
            )

            my_cursor.execute(query, values)

            conn.commit()

            self.fetch_data()

            conn.close()

            messagebox.showinfo(
                "Success",
                "Updated Successfully"
            )

        except Exception as es:
            messagebox.showerror(
                "Error",
                f"{str(es)}"
            )

    # ================= DELETE =================
    def delete_data(self):

        delete = messagebox.askyesno(
            "Delete",
            "Do you want to delete this booking?"
        )

        if delete:

            try:
                conn = self.connect_db()

                my_cursor = conn.cursor()

                sql = "DELETE FROM room WHERE contact=%s"

                val = (self.var_contact.get(),)

                my_cursor.execute(sql, val)

                conn.commit()

                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "Delete",
                    "Booking Deleted"
                )

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"{str(es)}"
                )

    # ================= RESET =================
    def reset_data(self):

        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("Single")
        self.var_roomavailable.set("")
        self.var_meal.set("Breakfast")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_totalpaid.set("")


# ================= MAIN =================
if __name__ == "__main__":

    root = Tk()

    obj = RoomBooking(root)

    root.mainloop()