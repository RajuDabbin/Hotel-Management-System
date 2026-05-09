from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1280x790+230+220")

        # ================= VARIABLES =================
        self.var_floor = StringVar()
        self.var_roomNo = StringVar()
        self.var_roomType = StringVar()

        # ================= TITLE =================
        lbl_title = Label(
            self.root,
            text="ROOM ADDING DEPARTMENT",
            font=("times new roman", 40, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE
        )

        lbl_title.place(x=0, y=0, width=1280, height=50)

        # ================= LABEL FRAME =================
        labelframeleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="New Room Add",
            font=("times new roman", 12, "bold"),
            padx=2
        )

        labelframeleft.place(x=5, y=50, width=540, height=350)

        # ================= FLOOR =================
        lbl_floor = Label(
            labelframeleft,
            text="Floor",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )

        lbl_floor.grid(row=0, column=0, sticky=W)

        entry_floor = ttk.Entry(
            labelframeleft,
            textvariable=self.var_floor,
            width=20,
            font=("arial", 13, "bold")
        )

        entry_floor.grid(row=0, column=1, sticky=W)

        # ================= ROOM NO =================
        lbl_RoomNo = Label(
            labelframeleft,
            text="Room No",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )

        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        entry_RoomNo = ttk.Entry(
            labelframeleft,
            textvariable=self.var_roomNo,
            width=20,
            font=("arial", 13, "bold")
        )

        entry_RoomNo.grid(row=1, column=1, sticky=W)

        # ================= ROOM TYPE =================
        lbl_RoomType = Label(
            labelframeleft,
            text="Room Type",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )

        lbl_RoomType.grid(row=2, column=0, sticky=W)

        combo_room = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_roomType,
            width=18,
            font=("arial", 12, "bold"),
            state="readonly"
        )

        combo_room["values"] = (
            "Single",
            "Double",
            "Luxury"
        )

        combo_room.current(0)

        combo_room.grid(row=2, column=1, sticky=W)

        # ================= BUTTON FRAME =================
        btn_frame = Frame(
            labelframeleft,
            bd=2,
            relief=RIDGE
        )

        btn_frame.place(x=0, y=200, width=412, height=40)

        Button(
            btn_frame,
            text="Add",
            command=self.add_data,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=10
        ).grid(row=0, column=0, padx=1)

        Button(
            btn_frame,
            text="Update",
            command=self.update,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=10
        ).grid(row=0, column=1, padx=1)

        Button(
            btn_frame,
            text="Delete",
            command=self.mDelete,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=10
        ).grid(row=0, column=2, padx=1)

        Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            font=("arial", 11, "bold"),
            bg="black",
            fg="gold",
            width=10
        ).grid(row=0, column=3, padx=1)

        # ================= TABLE FRAME =================
        Table_Frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Show Room Details",
            font=("times new roman", 12, "bold"),
            padx=2
        )

        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(
            Table_Frame,
            orient=HORIZONTAL
        )

        scroll_y = ttk.Scrollbar(
            Table_Frame,
            orient=VERTICAL
        )

        self.room_table = ttk.Treeview(
            Table_Frame,
            columns=("floor", "roomno", "type"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # ================= HEADINGS =================
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("type", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("type", width=150)

        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind(
            "<ButtonRelease-1>",
            self.get_cursor
        )

        self.fetch_data()

    # ================= DATABASE CONNECTION =================
    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="raju01",
            database="management"
        )

    # ================= ADD DATA =================
    def add_data(self):
        if (
            self.var_floor.get() == "" or
            self.var_roomNo.get() == "" or
            self.var_roomType.get() == ""
        ):

            messagebox.showerror(
                "Error",
                "All fields are required"
            )

        else:
            try:
                conn = self.connect_db()

                my_cursor = conn.cursor()

                query = """
                INSERT INTO details
                VALUES(%s,%s,%s)
                """

                values = (
                    self.var_floor.get(),
                    self.var_roomNo.get(),
                    self.var_roomType.get()
                )

                my_cursor.execute(query, values)

                conn.commit()

                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "Success",
                    "Room added successfully"
                )

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Error due to : {str(es)}"
                )

    # ================= FETCH DATA =================
    def fetch_data(self):
        try:
            conn = self.connect_db()

            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM details")

            rows = my_cursor.fetchall()

            self.room_table.delete(
                *self.room_table.get_children()
            )

            for i in rows:
                self.room_table.insert(
                    "",
                    END,
                    values=i
                )

            conn.close()

        except Exception as es:
            messagebox.showerror(
                "Error",
                f"Error due to : {str(es)}"
            )

    # ================= GET CURSOR =================
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()

        content = self.room_table.item(cursor_row)

        row = content["values"]

        if row:
            self.var_floor.set(row[0])
            self.var_roomNo.set(row[1])
            self.var_roomType.set(row[2])

    # ================= UPDATE =================
    def update(self):
        if self.var_roomNo.get() == "":
            messagebox.showerror(
                "Error",
                "Please select a room"
            )

        else:
            try:
                conn = self.connect_db()

                my_cursor = conn.cursor()

                query = """
                UPDATE details
                SET Floor=%s,
                    RoomType=%s
                WHERE RoomNo=%s
                """

                values = (
                    self.var_floor.get(),
                    self.var_roomType.get(),
                    self.var_roomNo.get()
                )

                my_cursor.execute(query, values)

                conn.commit()

                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "Update",
                    "Room details updated"
                )

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Error due to : {str(es)}"
                )

    # ================= DELETE =================
    def mDelete(self):
        delete = messagebox.askyesno(
            "Delete",
            "Do you want to delete this room?"
        )

        if delete:
            try:
                conn = self.connect_db()

                my_cursor = conn.cursor()

                query = """
                DELETE FROM details
                WHERE RoomNo=%s
                """

                value = (
                    self.var_roomNo.get(),
                )

                my_cursor.execute(query, value)

                conn.commit()

                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "Delete",
                    "Room deleted successfully"
                )

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Error due to : {str(es)}"
                )

    # ================= RESET =================
    def reset_data(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_roomType.set("Single")


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()