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
3.	To manage appointments by allowing users to book, view, search, and cancel appointments while checking doctor availability.
4.	To automate basic billing by calculating consultation, medicine, and test charges and applying applicable discounts.
5.	To provide basic reports such as the number of registered patients, doctors, appointments, and total revenue.
6.	To reduce data-entry errors through input validation and appropriate error-handling mechanisms.
7.	To organize data efficiently using Python data structures such as lists, tuples, and dictionaries.
8.	To apply Object-Oriented Programming concepts by representing entities such as patients, doctors, appointments, and bills as Python classes and objects.
9.	To demonstrate modular programming by separating different functionalities into appropriate Python modules and packages.
10.	To develop a maintainable and structured application that follows proper program organization and can be tested and improved easily.
11.	To apply the Python concepts learned in the course—including operators, conditional statements, loops, functions, modules, packages, data structures, and OOP—to a practical problem.


**Out of scope:** the project does not include persistent storage (all data
is kept in memory and is lost when the program closes), a graphical user
interface, multi-user access, user login/authentication, or integration with
real hospital systems (e.g. insurance, pharmacy, or lab equipment). Walk-in patients, searching pateints and doctors, editing their details, etc cannot be done using this program. It is
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



## Future Improvements