import customtkinter as ctk
from tkinter import messagebox

# ---------------- SETTINGS ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- FUNCTIONS ----------------

def clear():

    for widget in login_frame.winfo_children():
        widget.destroy()


# ---------- FIRST SCREEN ----------

def show_selection():

    clear()

    title=ctk.CTkLabel(
        login_frame,
        text="Athenaeum Login",
        font=("Arial",30,"bold")
    )

    title.pack(pady=(30,20))

    icon=ctk.CTkLabel(
        login_frame,
        text="👤",
        font=("Arial",60)
    )

    icon.pack(pady=10)

    subtitle=ctk.CTkLabel(
        login_frame,
        text="Choose Login Type",
        font=("Arial",18)
    )

    subtitle.pack(pady=15)

    admin_btn=ctk.CTkButton(
        login_frame,
        text="Admin Login",
        width=250,
        height=40,
        corner_radius=20,
        command=show_admin
    )

    admin_btn.pack(pady=10)

    user_btn=ctk.CTkButton(
        login_frame,
        text="User Login",
        width=250,
        height=40,
        corner_radius=20,
        command=show_user
    )

    user_btn.pack(pady=10)


# ---------- ADMIN SCREEN ----------

def show_admin():

    clear()

    title=ctk.CTkLabel(
        login_frame,
        text="Admin Login",
        font=("Arial",28,"bold")
    )

    title.pack(pady=20)

    icon=ctk.CTkLabel(
        login_frame,
        text="👤",
        font=("Arial",60)
    )

    icon.pack()

    global admin_user
    global admin_pass

    admin_user=ctk.CTkEntry(
        login_frame,
        width=280,
        placeholder_text="Username"
    )

    admin_user.pack(pady=15)

    admin_pass=ctk.CTkEntry(
        login_frame,
        width=280,
        placeholder_text="Password",
        show="*"
    )

    admin_pass.pack(pady=15)

    login_btn=ctk.CTkButton(
        login_frame,
        text="LOGIN",
        width=280,
        height=40,
        command=admin_login
    )

    login_btn.pack(pady=20)

    back=ctk.CTkButton(
        login_frame,
        text="Back",
        width=120,
        fg_color="gray",
        command=show_selection
    )

    back.pack()


# ---------- USER SCREEN ----------

def show_user():

    clear()

    title=ctk.CTkLabel(
        login_frame,
        text="User Login",
        font=("Arial",28,"bold")
    )

    title.pack(pady=20)

    icon=ctk.CTkLabel(
        login_frame,
        text="👤",
        font=("Arial",60)
    )

    icon.pack()

    global user_email
    global user_pass

    user_email=ctk.CTkEntry(
        login_frame,
        width=280,
        placeholder_text="Email ID"
    )

    user_email.pack(pady=15)

    user_pass=ctk.CTkEntry(
        login_frame,
        width=280,
        placeholder_text="Password",
        show="*"
    )

    user_pass.pack(pady=15)

    login_btn=ctk.CTkButton(
        login_frame,
        text="LOGIN",
        width=280,
        height=40,
        command=user_login
    )

    login_btn.pack(pady=20)

    back=ctk.CTkButton(
        login_frame,
        text="Back",
        width=120,
        fg_color="gray",
        command=show_selection
    )

    back.pack()


# ---------- LOGIN FUNCTIONS ----------

def admin_login():

    username=admin_user.get()
    password=admin_pass.get()

    if username=="admin" and password=="1234":

        messagebox.showinfo(
            "Success",
            "Admin Login Successful"
        )

        root.destroy()

        import dashboard

    else:

        messagebox.showerror(
            "Error",
            "Wrong Username or Password"
        )


def user_login():

    email=user_email.get()
    password=user_pass.get()

    if email and password:

        messagebox.showinfo(
            "Success",
            "User Login Successful"
        )

        root.destroy()

        import booking

    else:

        messagebox.showerror(
            "Error",
            "Enter Email and Password"
        )


# ---------------- WINDOW ----------------

root=ctk.CTk()

root.geometry("900x600")

root.title(
    "Athenaeum Login"
)

# Main background frame

bg=ctk.CTkFrame(
    root
)

bg.pack(
    fill="both",
    expand=True
)

# Center login card

login_frame=ctk.CTkFrame(
    bg,
    width=400,
    height=450,
    corner_radius=25
)

login_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

show_selection()

root.mainloop()