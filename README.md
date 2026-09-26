# Hospital Management System

## Overview

This is a simple, menu-driven **Hospital / Clinic Management System** built in
Python. It lets a hospital or clinic keep track of patients, doctors,
appointments, walk-in patients, and billing — all from a single text-based
menu, with no external database required.

The project was built as part of a Problem Solving and Programming course
assignment, and intentionally uses only core Python concepts (no classes,
no external libraries) so that every part of the code can be explained line
by line.

## Features

- **Patient management** — add new patients and view all registered patients
- **Doctor management** — add new doctors (with specialization and fee) and view all doctors
- **Appointment booking** — book an appointment for a patient with a doctor at a fixed time slot, with automatic double-booking prevention
- **Appointment management** — view all appointments and cancel an existing one
- **Walk-in queue** — add walk-in patients to a waiting queue, serve the next patient in line, and view who's currently waiting
- **Patient search** — search for a patient by name (or part of a name)
- **Billing** — generate a bill combining consultation fee, medicine cost, test cost, and discount, and view all past bills

## Technologies / Tools Used

- **Language:** Python 3 (3.10 or newer recommended)
- **Data storage:** in-memory, using built-in Python data structures only
  - Dictionaries — patient records, doctor records, bill records
  - Lists — appointment records, walk-in queue
  - Tuples — fixed list of available time slots
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
   or simply download `hospital_system.py` into a folder of your choice.

3. **Run the program**
   No installation of extra packages is needed — the project only uses
   Python's built-in features. From inside the project folder, run:
   ```
   python hospital_system.py
   ```
   (On some systems you may need to use `python3` instead of `python`.)

4. **Use the menu**
   The program will display a numbered menu in the terminal. Type the
   number of the action you want and press Enter, then follow the prompts.

## Instructions for Testing

Since this project has no automated test suite, testing is done manually by
running the program and exercising each menu option. A suggested test
sequence:

1. **Add a patient** (option 1) — enter sample details, note the generated Patient ID (e.g. `P001`).
2. **View patients** (option 2) — confirm the patient you added appears correctly.
3. **Add a doctor** (option 3) — enter sample details, note the generated Doctor ID (e.g. `D001`).
4. **View doctors** (option 4) — confirm the doctor appears correctly.
5. **Book an appointment** (option 5) — use the Patient ID and Doctor ID from above, pick a date and a time slot from the list shown.
6. **Try booking the same doctor at the same date and time again** — the program should reject it, confirming double-booking prevention works.
7. **View appointments** (option 6) — confirm the appointment is listed with status "Booked".
8. **Cancel the appointment** (option 7) using its Appointment ID, then view appointments again to confirm its status changed to "Cancelled". Try re-booking the same slot to confirm it is now free again.
9. **Search for the patient by name** (option 10) using only part of the name, to confirm the search works with partial matches.
10. **Add a couple of walk-in patients** (option 11), then **view the queue** (option 13) to confirm they appear in the order they were added.
11. **Serve the next walk-in patient** (option 12) and view the queue again to confirm that person is removed and the rest shift up.
12. **Generate a bill** (option 8) for the patient using the doctor's fee, then **view bills** (option 9) to confirm the total is calculated correctly.
13. **Exit the program** (option 0) and confirm it closes cleanly.

Testing with intentionally invalid input (e.g. an unknown Patient ID, an
invalid menu choice, or a time slot not in the list) is also recommended to
confirm the program's error messages appear instead of the program crashing.
