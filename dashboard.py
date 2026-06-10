<!DOCTYPE html>
<html>

<head>

    <title>Admin Dashboard</title>

    <link rel="stylesheet"
          href="{{ url_for('static', filename='css/style.css') }}">

</head>

<body>

<div class="dashboard">

    <!-- SIDEBAR -->

    <div class="sidebar">

        <h2>Athenaeum</h2>

        <a href="/view_bookings">
            <button class="menu-btn">
                View Bookings
            </button>
        </a>

        <a href="/reports">
            <button class="menu-btn">
                Reports
            </button>
        </a>

        <a href="/">
            <button class="logout">
                Logout
            </button>
        </a>

    </div>

    <!-- MAIN -->

    <div class="main-content">

        <h1>Welcome Admin</h1>

        <div class="cards">

            <!-- TOTAL BOOKINGS -->

            <div class="card">

                <h2>
                    {{ total_bookings }}
                </h2>

                <p>Total Bookings</p>

            </div>

            <!-- TODAY EVENTS -->

            <div class="card">

                <h2>
                    {{ today_events }}
                </h2>

                <p>Today's Events</p>

            </div>

            <!-- DEPARTMENTS -->

            <div class="card">

                <h2>
                    {{ departments }}
                </h2>

                <p>Departments</p>

            </div>

        </div>

    </div>

</div>

</body>

</html>