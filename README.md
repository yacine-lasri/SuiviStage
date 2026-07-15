# Suivi de Stage — Internship Tracking Web Application

A full-stack web application built using **Python** and **Django** designed to streamline and monitor the internship lifecycle for engineering students. This project was developed as a core curriculum project at EMSI Casablanca.

While my primary engineering focus is on low-level systems programming and networking, building this application allowed me to master Application Layer (Layer 7) concepts, secure web workflows, and relational database design.

---

## Key Features & Architecture

The platform manages the complete workflow of student internships by segregating permissions and views across three distinct roles: **Students**, **Academic Tutors**, and **Administrators**.

*   **Role-Based Access Control (RBAC):** Built secure, middleware-protected views ensuring students can only submit and view their own internship progress, while tutors and admins hold specific grading and management privileges.
*   **Relational Database Schema:** Designed a robust database model handling relationships between users, internship listings, weekly logs (suivi), and final evaluations.
*   **Document Uploads:** Implemented file handling for students to securely upload mandatory internship documents and final reports.
*   **Dynamic Dashboard:** Created a real-time tracking interface for tutors to monitor student milestones, weekly submissions, and advisor assignments.

---

## Tech Stack

*   **Backend Framework:** Django (Python)
*   **Database:** SQLite (Development) / PostgreSQL compatible
*   **Frontend:** HTML5, CSS3 (Bootstrap), JavaScript
*   **Authentication:** Django Built-in Auth System (customized for multi-user roles)

---

## System Architecture

             [ User / Browser ]
                     │  (HTTP Requests)
                     ▼
           [ Django Middleware ]  <─── (RBAC / Auth Check)
                     │
                     ▼
            [ URL Dispatcher ]
                     │
                     ▼
                [ Views ] 
               /         \
(Read/Write)    /           \   (Render)▼             ▼[ Models ]     [ Templates ]│             (HTML/Bootstrap)▼[ Relational DB ]
---

## Installation and Setup

### Prerequisites
*   Python 3.8+
*   `pip` (Python package manager)

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yacine-lasri/suivi-stage-django.git](https://github.com/yacine-lasri/suivi-stage-django.git)
   cd suivi-stage-django
Create and activate a virtual environment:Bash# On Windows
python -m venv venv
.\venv\Scripts\activate

# On Linux/macOS
python3 -m venv venv
source venv/bin/activate
Install dependencies:Bashpip install -r requirements.txt
Apply database migrations:Bashpython manage.py migrate
Create an administrator (superuser) account:Bashpython manage.py createsuperuser
Run the development server:Bashpython manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/.Engineering TakeawaysApplication Security: Gained practical understanding of Web Security basics, including mitigating Cross-Site Request Forgery (CSRF) using Django tokens, handling secure session cookies, and implementing strict backend password hashing.Data Modeling: Learned how to translate real-world academic workflows into normalized SQL tables using Django's Object-Relational Mapping (ORM), avoiding redundant data.State & Lifecycle Management: Built logic to handle state transitions (e.g., Submitted $\rightarrow$ Under Review $\rightarrow$ Approved), which is a fundamental concept in systems and application design.
