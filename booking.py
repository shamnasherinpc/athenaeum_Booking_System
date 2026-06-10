import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

# ---------- SETTINGS ----------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ---------- FUNCTIONS ----------

def is_weekend(date_obj):

    return date_obj.weekday() in (5,6)


def book_auditorium():

    dept=department.get()

    event=event_name.get()

    selected_date=cal.get_date()

    start=start_time.get()

    end=end_time.get()


    if dept=="Select Department" or event=="" or start=="" or end=="":

        messagebox.showwarning(
            "Error",
            "Please fill all fields"
        )

        return


    if is_weekend(selected_date):

        messagebox.showerror(
            "Error",
            "Weekend booking not allowed"
        )

        return


    try:

        s=datetime.strptime(
            start,
            "%I:%M %p"
        )

        e=datetime.strptime(
            end,
            "%I:%M %p"
        )

        if e<=s:

            messagebox.showerror(
                "Error",
                "End time must be after start time"
            )

            return


    except:

        messagebox.showerror(
            "Error",
            "Time format: 09:30 AM"
        )

        return


    with open(
            "bookings.txt",
            "a"
    ) as f:

        f.write(
            f"{selected_date},{start},{end},{dept},{event}\n"
        )


    messagebox.showinfo(
        "Success",
        "Booking Successful"
    )


def view_bookings():

    win=ctk.CTkToplevel()

    win.geometry(
        "700x400"
    )

    win.title(
        "Bookings"
    )

    textbox=ctk.CTkTextbox(
        win,
        width=600,
        height=300
    )

    textbox.pack(
        pady=20,
        padx=20
    )

    try:

        with open(
                "bookings.txt",
                "r"
        ) as f:

            data=f.read()

            textbox.insert(
                "0.0",
                data
            )

    except:

        textbox.insert(
            "0.0",
            "No bookings found"
        )


# ---------- MAIN WINDOW ----------

root=ctk.CTk()

root.geometry(
    "1000x600"
)

root.title(
    "Athenaeum Booking System"
)


# ---------- SIDEBAR ----------

sidebar=ctk.CTkFrame(
    root,
    width=220
)

sidebar.pack(
    side="left",
    fill="y"
)


title=ctk.CTkLabel(
    sidebar,
    text="Athenaeum",
    font=("Arial",30,"bold")
)

title.pack(
    pady=30
)


view=ctk.CTkButton(
    sidebar,
    text="View Bookings",
    command=view_bookings
)

view.pack(
    pady=10
)


# ---------- MAIN FRAME ----------

mainframe=ctk.CTkFrame(
    root,
    corner_radius=20
)

mainframe.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=30
)


department=ctk.StringVar(
    value="Select Department"
)

event_name=ctk.StringVar()

start_time=ctk.StringVar()

end_time=ctk.StringVar()


heading=ctk.CTkLabel(
    mainframe,
    text="Book Auditorium",
    font=("Arial",30,"bold")
)

heading.pack(
    pady=20
)


# Department

ctk.CTkLabel(
    mainframe,
    text="Department"
).pack()

dept=ctk.CTkOptionMenu(
    mainframe,
    variable=department,
    values=[
        "BCA",
        "BBA",
        "Engineering",
        "Nursing",
        "B Pharm",
        "Physiotherapy"
    ]
)

dept.pack(
    pady=10
)


# Event

ctk.CTkLabel(
    mainframe,
    text="Event Name"
).pack()

event=ctk.CTkEntry(
    mainframe,
    width=300,
    textvariable=event_name,
    placeholder_text="Enter Event Name"
)

event.pack(
    pady=10
)


# Date

ctk.CTkLabel(
    mainframe,
    text="Select Date"
).pack()

cal=DateEntry(
    mainframe,
    width=18
)

cal.pack(
    pady=10
)


# Start time

ctk.CTkLabel(
    mainframe,
    text="Start Time"
).pack()

start=ctk.CTkEntry(
    mainframe,
    width=300,
    textvariable=start_time,
    placeholder_text="09:30 AM"
)

start.pack(
    pady=10
)


# End time

ctk.CTkLabel(
    mainframe,
    text="End Time"
).pack()

end=ctk.CTkEntry(
    mainframe,
    width=300,
    textvariable=end_time,
    placeholder_text="11:30 AM"
)

end.pack(
    pady=10
)


book=ctk.CTkButton(
    mainframe,
    text="Book Auditorium",
    width=250,
    height=40,
    command=book_auditorium
)

book.pack(
    pady=20
)

root.mainloop()