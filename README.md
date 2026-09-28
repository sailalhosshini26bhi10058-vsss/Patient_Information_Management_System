# Patient Information Management System

## Project Overview

This is a simple, menu-driven **Patient Information System** built in
Python. It lets a Clinic/Hospital keep track of patients, doctors,
appointments, and billing — all from a single text-based
menu, with no external database required.

The project was built as part of the "Python Essentials" course in VITyarthi platform, and intentionally uses only core Python concepts covered in the said course.

# Problem Statement

Hospitals and small clinics often rely on paper registers or scattered
spreadsheets to manage patient records, doctor schedules, appointments, and
billing. This makes it slow to look up a patient's history, easy to
accidentally double-book a doctor, and error-prone when calculating bills by
hand.

This project addresses that problem by building a simple, menu-driven
**Patient Information Management System** in Python. It gives a receptionist or admin
staff member a single program to register patients and doctors, schedule and
manage appointments, and generate accurate bills —
without needing a database server or any external software.

## Objectives

1.	To manage patient records by allowing users to add, view, search, update, and delete patient information.
2.	To manage doctor records by maintaining information such as doctor ID, name, specialization, and consultation fee.
3. To provide an appointment booking system with predefined time slots.
4.	To prevent double booking of a doctor at the same date and time.
5. To allow appointments to be cancelled and re-booked.
6. To generate bills using consultation, medicine, test and discount amounts.
7. To provide input validation and error handling.
8. To demonstrate the use of Python data structures and control statements.
9. To organize the program into separate modules for better maintainability.
10.To maintain the project using Git and GitHub.



**Out of scope:** the project does not include persistent storage (all data
is kept in memory and is lost when the program closes), a graphical user
interface, multi-user access, user login/authentication, or integration with
real hospital systems (e.g. insurance, pharmacy, or lab equipment). Walk-in patients, searching patients and doctors, editing their details, etc cannot be done using this program. It is
built as a learning project to demonstrate core programming concepts, not as
production software.


## Features

- **Patient management** — add new patients and view all registered patients
- **Doctor management** — add new doctors (their details like specialization and fee) and view all doctors
- **Appointment booking** — book an appointment for a patient with a doctor at a fixed time slot, with automatic double-booking prevention
- **Appointment management** — view all appointments and cancel an existing one
- **Billing** — generate a bill combining consultation fee, medicine cost, test cost, and discount, and view all past bills

## Functional Requirements

1.	Patient Management
The system shall allow users to add, view, search, update, and delete patient records.
2.	Doctor Management
The system shall allow users to add, view, and search doctor records, including doctor ID, name, specialization, and consultation fee.
3.	Appointment Management
The system shall allow users to book, view, search, and cancel appointments, while checking doctor availability to prevent scheduling conflicts.
4.	Billing Management
The system shall allow users to generate and view patient bills by calculating consultation fees, medicine charges, test charges, and applicable discounts.
5. Error Handling
The system sall direct, handle, and log errors arising from any of the operations and displays user friendly error meassages.

## Non Functional-Requirements

1. Usability
-Simple menu-driven interface.
-Clear prompts and error messages.
-Suitable for beginner-level clinic administration.

2. Reliability
-Prevents appointment double-booking.
-Validates patient and doctor IDs.
-Handles invalid user input without crashing.

3. Performance
-Uses dictionaries and sets for fast record lookup.
-Suitable for small clinic datasets.

4. Maintainability
-Patient, doctor, appointment, and billing functionality are separated into modules.
-Modular structure makes future modifications easier.


## Project Structure



                                                            ┌─────────────────────┐
                                                            │        USER         │
                                                            └──────────┬──────────┘
                                                                       │
                                                                       ▼
                                                            ┌─────────────────────┐
                                                            │      main.py        │
                                                            │     Main Menu       │
                                                            └──────────┬──────────┘
                                                                       │
                        ┌──────────────────────────────────────────────┼──────────────────────────────────────────┐
                        │                                              │                                          │
                        ▼                                              ▼                                          ▼
               ┌──────────────┐                                 ┌──────────────┐                          ┌────────────────┐
               │  patients.py │                                 │  doctors.py  │                          │ appointment.py │
               │    Patient   │                                 │    Doctor    │                          │ Appointments   │
               │  Management  │                                 │  Management  │                          │  Management    │
               └──────────────┘                                 └──────────────┘                          └────────────────┘
                       │                                               │                                           │
                       │                                               │                                           │
                       └───────────────────────────────────────────────┼───────────────────────────────────────────┘
                                                                       │
                                                                       ▼
                                                                ┌──────────────┐
                                                                │    bill.py   │
                                                                │    Billing   │
                                                                └──────────────┘


## Technologies / Tools Used

- **Language:** Python (3.10 or newer recommended)
- **Data storage:** in-memory, using built-in Python data structures only
  - Dictionaries — patient_dict, doctor_dict, bills_dict
  - Lists — appointment_list
  - Tuples — time_slots
  - Sets — tracking already-booked doctor/date/time combinations
- **No external libraries or database** — runs with a standard Python installation
- **Editor used:** Visual Studio Code
- **Version control:** Git and GitHub

## Steps to Install & Run the Project

1. **Install Python** (if not already installed)
   Download from [python.org](https://www.python.org/downloads/) and verify with:
   ```
   python --version
   ```

2. **Get the project files**
   Either clone the repository:
   ```
   git clone <your-repository-url>
   cd <repository-folder>
   ```
   or simply download `clinic_management_system.py` into a folder of your choice.

3. **Run the program**
   No need to install extra packages — the project only uses
   Python's built-in features. From inside the project folder, run:
   ```
   python clinic_management_system.py
   ```

4. **Use the menu**
   The program will display a numbered menu in the terminal. Type the
   number of the action you want and press Enter, then follow the prompts.

## Instructions for Testing

Testing is done manually by running the program and exercising each menu option. A  suggested testsequence:

1. **Add a patient** (option 1) — enter sample details, note the generated Patient ID (e.g. `P1`).
2. **View patients** (option 2) — confirm the patient you added appears correctly.
3. **Add a doctor** (option 3) — enter sample details, note the generated Doctor ID (e.g. `D1`).
4. **View doctors** (option 4) — confirm the doctor appears correctly.
5. **Book an appointment** (option 5) — use the Patient ID and Doctor ID from above, pick a date and a time slot from the list shown, note the generated Appointment ID (e.g. `A1`)
6. **Try booking the same doctor at the same date and time again** — the program should reject it, confirming double-booking prevention works.
7. **View appointments** (option 6) — confirm the appointment is listed with status "Booked".
8. **Cancel the appointment** (option 7) using its Appointment ID, then view appointments again to confirm its status changed to "Cancelled". Try re-booking the same slot to confirm it is now free again.
9. **Generate a bill** (option 8) — for the patient using the doctor's fee.
10. **view bills** (option 9) — confirm the total is calculated correctly.
11. **Delete patient records** (option 10) use the Patient ID to delete their records and related appointments
12. **Try accessing the patient details and view appointments again**- The Patient's details must have cleared and the related appointments must have been deleted.
13. **Exit the program** (option 0) and confirm it closes cleanly.

Testing with intentionally invalid input (e.g. an unknown Patient ID, an
invalid menu choice, or a time slot not in the list) is also recommended to
confirm the program's error messages appear instead of the program crashing.




## Limitations

1. **Command-Line Interface Only**
 The system operates through a text-based interface, which may not be as user-friendly as a graphical application.
2. **Data Is Not Permanently Stored**
 Patient, doctor, appointment, and billing records are stored in Python data structures during program execution. The data is lost when the program is closed.
3. **Limited Date Validation**
 The appointment system checks the DD-MM-YYYY format but does not verify whether the entered date is an actual calendar date.
4. **Fixed Appointment Time Slots**
 The system provides only predefined time slots. Users cannot add or customize available timings.
5. **No User Authentication**
 There is no login system or role-based access for administrators, doctors, or staff.
6. **Basic Search and Management**
 The system does not provide advanced searching, filtering, or sorting of patient, doctor, or appointment records.
7. **Basic Billing System**
 Billing is limited to consultation, medicine, test fees, and discount. It does not generate professional invoices or maintain detailed payment information.
8. **Limited Data Validation**
 Some inputs, such as phone numbers and fees, have only basic validation and could be improved further.


## Future Improvements

1. **Database Integration**
   Use MySQL or SQLite to permanently store patient, doctor, appointment, and billing records.
2. **Graphical User Interface (GUI)**
   Develop a GUI using Tkinter, PyQt, or a web interface to make the system easier to use.
3. **User Authentication**
   Add secure login with different roles such as Admin, Doctor, Receptionist, and Patient.
4. **Advanced Appointment Management**
   Allow users to:
    -Add custom time slots
    -Reschedule appointments
    -Search appointments by date or doctor
    -Maintain appointment history
5. **Improved Validation**
   Add validation for:
    -Actual calendar dates
    -Phone numbers
    -Positive fee values
    -Required fields
    -Duplicate patient information
6. **Enhanced Billing**
   Add:
    -Detailed invoices
    -Payment status
    -Payment methods
    -Tax calculation
    -Printable/downloadable bills
7. **Patient Search and Medical Records**
   Store additional information such as medical history, diagnosis, prescriptions, and previous visits.
8. **Reports and Analytics**
   Generate reports such as:
    -Number of patients
    -Daily appointments
    -Doctor-wise appointments
    -Revenue reports
9. **Data Backup and Export**
   Provide options to export records to CSV/PDF and create regular backups.
10.**Web/Cloud Deployment**
   Convert the project into a web-based application so authorized users can access it from different devices.