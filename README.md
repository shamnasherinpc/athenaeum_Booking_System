Athenaeum Booking System

Overview

The Athenaeum Booking System is a web-based auditorium reservation and event management application developed to simplify the process of booking and managing the Athenaeum auditorium. The system provides a centralized platform where users can submit booking requests, monitor reservation status, and manage event schedules, while administrators can review, approve, or reject bookings efficiently.

The project was developed as part of an academic software development project to demonstrate the practical implementation of web application development, database management, user authentication, and booking management functionalities using modern technologies.

⸻

Key Features

User Module
	•	User Registration and Login
	•	Secure Authentication System
	•	Auditorium Booking Request Submission
	•	Event Scheduling Management
	•	Booking Status Tracking
	•	Booking History Management

Admin Module
	•	Admin Login Authentication
	•	View All Booking Requests
	•	Approve or Reject Reservations
	•	Manage Event Schedules
	•	Generate Booking Reports
	•	Monitor System Activities

Reporting Module
	•	Reservation Reports
	•	Booking Statistics
	•	Event Scheduling Records
	•	Administrative Monitoring Reports

⸻

System Architecture

The application follows a modular architecture consisting of:
	•	Frontend Interface
	•	Backend Processing Layer
	•	Database Management Layer
	•	Authentication and Authorization Module
	•	Booking Management Module
	•	Reporting Module

This structure improves maintainability, scalability, and future enhancement capabilities.

⸻

Technologies Used

Programming Language
	•	Python

Backend Framework
	•	Flask

Frontend Technologies
	•	HTML
	•	CSS
	•	JavaScript

Database
	•	SQLite

Development Tools
	•	Visual Studio Code
	•	Git
	•	GitHub

Browser Support
	•	Google Chrome
	•	Microsoft Edge
	•	Mozilla Firefox

⸻

Project Structure

Athenaeum_Booking_System/
│
├── app.py
├── login.py
├── dashboard.py
├── booking.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── booking.html
│   └── admin_dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md


⸻

Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/your-username/athenaeum_Booking_System.git

Step 2: Navigate to Project Directory

cd athenaeum_Booking_System

Step 3: Install Required Dependencies

pip install flask

Step 4: Run the Application

python app.py

Step 5: Open in Browser

http://127.0.0.1:5000


⸻

Database

The system uses SQLite for storing:
	•	User Information
	•	Department Details
	•	Auditorium Information
	•	Reservation Records
	•	Booking Status Updates
	•	Administrative Data

⸻

Future Enhancements
	•	Mobile Application Support
	•	Cloud Deployment
	•	Email Notification System
	•	Real-Time Booking Updates
	•	AI-Based Schedule Recommendations
	•	Online Payment Integration
	•	Advanced Analytics Dashboard
	•	Multi-Language Support
	•	Enhanced Security Features

⸻


Conclusion

The Athenaeum Booking System successfully provides a reliable and user-friendly platform for managing auditorium reservations and event scheduling. The system improves booking efficiency, reduces manual management efforts, and provides administrators with better control over reservation activities through a centralized and secure web application.
