# Hospital Management System

## Objective

This is a simple, menu-driven **Hospital / Clinic Management System** built in
Python. It lets a Clinic keep track of patients, doctors,
appointments, and billing — all from a single text-based
menu, with no external database required.

The project was built as part of the "Python Essentials" course in VITyathi platform, and intentionally uses only core Python concepts covered in the said course.

## Features

- **Patient management** — add new patients and view all registered patients
- **Doctor management** — add new doctors (their details like specialization and fee) and view all doctors
- **Appointment booking** — book an appointment for a patient with a doctor at a fixed time slot, with automatic double-booking prevention
- **Appointment management** — view all appointments and cancel an existing one
- **Billing** — generate a bill combining consultation fee, medicine cost, test cost, and discount, and view all past bills

## Technologies / Tools Used

- **Language:** Python 3.14 (3.10 or newer recommended)
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

Testing is done manually by running the program and exercising each menu option. A suggested test
sequence:

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
11. **Delete patient records** (option 10) use the Patient ID to delete thier records and related appointments
12. **Try accessing the patient deatils and view appointments again**- The Patient's details must have cleared and the related appointments must have been deleted.
13. **Exit the program** (option 0) and confirm it closes cleanly.

Testing with intentionally invalid input (e.g. an unknown Patient ID, an
invalid menu choice, or a time slot not in the list) is also recommended to
confirm the program's error messages appear instead of the program crashing.
