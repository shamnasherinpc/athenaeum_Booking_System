from tkinter import *

from tkinter import messagebox

from tkinter import ttk

from datetime import datetime

from supabase import create_client

# ---------- SUPABASE CONNECTION ----------

url = "https://fbpdqgyetuzalsnixmfr.supabase.co"


key = "your key here"

supabase = create_client(url, key)

# ---------- CHECK TIME CONFLICT ----------

def is_slot_conflict(date, new_start, new_end):

    try:

        response = supabase.table("bookings").select("*").eq("date", date).execute()

        data = response.data

        for row in data:

            existing_start = datetime.strptime(row["start_time"], "%I:%M %p")

            existing_end = datetime.strptime(row["end_time"], "%I:%M %p")

            if (new_start < existing_end and new_end > existing_start):

                return True

    except Exception as e:

        print("Conflict check error:", e)

        return False

    return False

# ---------- BOOK FUNCTION ----------

def book_auditorium():

    dept = department.get()

    event = event_name.get()

    date = event_date.get()

    start = start_time.get()

    end = end_time.get()

    # Empty validation

    if dept == "Select Department" or event == "" or date == "" or start == "" or end == "":

        messagebox.showwarning("Error", "All fields are required!")

        return

    # Date validation

    try:

        entered_date = datetime.strptime(date, "%d-%m-%Y")

        today = datetime.today()

        today = datetime(today.year, today.month, today.day)

        if entered_date < today:

            messagebox.showerror("Error", "Cannot book past dates!")

            return

    except:

        messagebox.showerror("Error", "Enter date in DD-MM-YYYY format")

        return

    # Time validation (AM/PM)

    try:

        start_obj = datetime.strptime(start.strip(), "%I:%M %p")

        end_obj = datetime.strptime(end.strip(), "%I:%M %p")

        if end_obj <= start_obj:

            messagebox.showerror("Error", "End time must be after start time!")

            return

    except:

        messagebox.showerror("Error", "Enter time like 09:30 AM")

        return

    # Conflict check

    if is_slot_conflict(date, start_obj, end_obj):

        messagebox.showerror("Error", "Time slot already booked!")

        return

    # Insert into Supabase

    try:

        response = supabase.table("bookings").insert({

            "date": date,

            "start_time": start,

            "end_time": end,

            "department": dept,

            "event": event

        }).execute()

        print("Insert response:", response)

        messagebox.showinfo("Success", "Booking Saved Successfully!")

    except Exception as e:

        messagebox.showerror("Error", str(e))

        print("Insert error:", e)

    # Clear fields

    department.set("Select Department")

    event_name.set("")

    event_date.set("")

    start_time.set("")

    end_time.set("")

# ---------- VIEW BOOKINGS ----------

def view_bookings():

    window = Toplevel(root)

    window.title("Booking Table")

    window.geometry("700x300")

    tree = ttk.Treeview(window, columns=("Date","Start","End","Department","Event"), show="headings")

    for col in ("Date","Start","End","Department","Event"):

        tree.heading(col, text=col)

        tree.column(col, width=120)

    tree.pack(fill=BOTH, expand=True)

    try:

        response = supabase.table("bookings").select("*").execute()

        data = response.data

        for row in data:

            tree.insert("", END, values=(

                row["date"],

                row["start_time"],

                row["end_time"],

                row["department"],

                row["event"]

            ))

    except Exception as e:

        messagebox.showerror("Error", str(e))

        print("Fetch error:", e)

# ---------- UI ----------

root = Tk()

root.title("Athenaeum Booking System")

root.geometry("400x450")

department = StringVar()

event_name = StringVar()

event_date = StringVar()

start_time = StringVar()

end_time = StringVar()

department.set("Select Department")

Label(root, text="Athenaeum Booking System", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Department").pack()

OptionMenu(root, department, "BCA","BBA","B Pharm","Physiotherapy","Nursing","Engineering").pack()

Label(root, text="Event Name").pack()

Entry(root, textvariable=event_name).pack()

Label(root, text="Date (DD-MM-YYYY)").pack()

Entry(root, textvariable=event_date).pack()

Label(root, text="Start Time (e.g., 09:30 AM)").pack()

Entry(root, textvariable=start_time).pack()

Label(root, text="End Time (e.g., 11:30 AM)").pack()

Entry(root, textvariable=end_time).pack()

Button(root, text="Book Auditorium", command=book_auditorium).pack(pady=10)

Button(root, text="View Bookings", command=view_bookings).pack()

root.mainloop()