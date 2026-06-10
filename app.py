from flask import Flask,render_template,request,redirect,send_file
import sqlite3
from datetime import date,datetime
from reportlab.platypus import SimpleDocTemplate,Table
from reportlab.platypus.tables import TableStyle
from reportlab.lib import colors

app=Flask(__name__)

# ---------------- DATABASE ----------------

conn=sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor=conn.cursor()

# ---------------- CREATE TABLE ----------------

cursor.execute("""

CREATE TABLE IF NOT EXISTS bookings(

id INTEGER PRIMARY KEY AUTOINCREMENT,

department TEXT,

event TEXT,

date TEXT,

start_time TEXT,

end_time TEXT,

participants TEXT,

status TEXT DEFAULT 'Pending'

)

""")

conn.commit()





# ---------------- HOME ----------------

@app.route("/")
def home():

    return render_template(
        "role_select.html"
    )


# ---------------- LOGIN ----------------

@app.route("/login/<role>")
def login(role):

    return render_template(
        "login.html",
        role=role
    )


# ---------------- AUTHENTICATE ----------------

@app.route(
"/authenticate",
methods=["POST"]
)

def authenticate():

    role=request.form["role"]

    if role=="admin":

        username=request.form["username"]
        password=request.form["password"]

        if username=="admin" and password=="1234":

            return redirect(
                "/admin_dashboard"
            )

        else:

            return render_template(
                "login.html",
                role="admin",
                error="Invalid Username or Password"
            )

    else:

        email=request.form["email"]
        password=request.form["password"]

        if email and password:

            return redirect(
                "/booking"
            )

        else:

            return render_template(
                "login.html",
                role="user",
                error="Enter Email and Password"
            )


# ---------------- ADMIN DASHBOARD ----------------

@app.route("/admin_dashboard")
def admin_dashboard():

    cursor.execute(
        "SELECT COUNT(*) FROM bookings"
    )
    total=cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM bookings WHERE status='Approved'"
    )
    approved=cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM bookings WHERE status='Pending'"
    )
    pending=cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM bookings WHERE status='Rejected'"
    )
    rejected=cursor.fetchone()[0]

    return render_template(

        "dashboard.html",

        total_bookings=total,
        approved_bookings=approved,
        pending_bookings=pending,
        rejected_bookings=rejected

    )


# ---------------- BOOKING PAGE ----------------

@app.route("/booking")
def booking():

    return render_template(
        "booking.html"
    )


# ---------------- SAVE BOOKING ----------------

@app.route(
"/save_booking",
methods=["POST"]
)

def save_booking():

    department=request.form["department"]
    event=request.form["event"]
    booking_date=request.form["date"]
    start=request.form["start"]
    end=request.form["end"]
    participants=request.form["participants"]

    # REQUIRED FIELD CHECK

    if not all([

        department,
        event,
        booking_date,
        start,
        end,
        participants

    ]):

        return render_template(

            "booking.html",

            error="Please fill all required fields"

        )

    selected_date=date.fromisoformat(
        booking_date
    )

    today=date.today()

    # BLOCK TODAY & PREVIOUS

    if selected_date<=today:

        return render_template(

            "booking.html",

            error="Booking available only from tomorrow"

        )

    # BLOCK WEEKENDS

    if selected_date.weekday() in [5,6]:

        return render_template(

            "booking.html",

            error="Saturday and Sunday Closed"

        )

    time_format="%I:%M %p"

    start_obj=datetime.strptime(
        start,
        time_format
    )

    end_obj=datetime.strptime(
        end,
        time_format
    )

    # END AFTER START

    if start_obj>=end_obj:

        return render_template(

            "booking.html",

            error="End time must be after start time"

        )


    # -------- SLOT CONFLICT CHECK --------

    cursor.execute(
        "SELECT start_time,end_time FROM bookings WHERE date=?",
        (booking_date,)
    )

    existing_slots=cursor.fetchall()

    for slot in existing_slots:

        booked_start=datetime.strptime(
            slot[0],
            time_format
        )

        booked_end=datetime.strptime(
            slot[1],
            time_format
        )

        # overlap check
        if start_obj < booked_end and end_obj > booked_start:

            return render_template(

                "booking.html",

                error="Time slot already booked"

            )


    # SAVE BOOKING

    cursor.execute("""

    INSERT INTO bookings(

    department,
    event,
    date,
    start_time,
    end_time,
    participants

    )

    VALUES(?,?,?,?,?,?)

    """,(

    department,
    event,
    booking_date,
    start,
    end,
    participants

    ))

    conn.commit()

    return render_template(

        "booking.html",

        success="Booking Successful"

    )


# ---------------- VIEW BOOKINGS ----------------

@app.route("/view_bookings")
def view_bookings():

    cursor.execute(
        "SELECT * FROM bookings"
    )

    data=cursor.fetchall()

    return render_template(
        "view_bookings.html",
        bookings=data
    )


# ---------------- MY BOOKINGS ----------------

@app.route("/my_bookings")
def my_bookings():

    cursor.execute(
        "SELECT * FROM bookings"
    )

    data=cursor.fetchall()

    return render_template(
        "my_bookings.html",
        bookings=data
    )


# ---------------- APPROVE ----------------

@app.route("/approve/<int:id>")
def approve_booking(id):

    cursor.execute(
    "UPDATE bookings SET status='Approved' WHERE id=?",
    (id,)
    )

    conn.commit()

    return redirect(
        "/view_bookings"
    )


# ---------------- REJECT ----------------

@app.route("/reject/<int:id>")
def reject_booking(id):

    cursor.execute(
    "UPDATE bookings SET status='Rejected' WHERE id=?",
    (id,)
    )

    conn.commit()

    return redirect(
        "/view_bookings"
    )


# ---------------- REPORTS ----------------

@app.route("/reports")
def reports():

    cursor.execute(
        "SELECT * FROM bookings"
    )

    data=cursor.fetchall()

    return render_template(
        "reports.html",
        bookings=data
    )


# ---------------- PDF REPORT ----------------

@app.route("/download_report")
def download_report():

    cursor.execute(
        "SELECT * FROM bookings"
    )

    data=cursor.fetchall()

    pdf="booking_report.pdf"

    document=SimpleDocTemplate(pdf)

    table_data=[

        ["ID",
        "Department",
        "Event",
        "Date",
        "Status"]

    ]

    for row in data:

        table_data.append([

            row[0],
            row[1],
            row[2],
            row[3],
            row[7]

        ])

    table=Table(table_data)

    style=TableStyle([

    ('BACKGROUND',(0,0),(-1,0),colors.blue),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('GRID',(0,0),(-1,-1),1,colors.black)

    ])

    table.setStyle(style)

    document.build([table])

    return send_file(
        pdf,
        as_attachment=True
    )


# ---------------- RUN ----------------

if __name__=="__main__":

    app.run(
        debug=True
    )