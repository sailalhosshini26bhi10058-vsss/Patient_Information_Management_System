# Patient Information Management System

## Project Overview

The Patient Information System is a simple, menu-driven Python program designed to help a small clinic or hospital manage basic patient-related information. The system can be used to maintain records of patients and doctors, book appointments, manage cancellations, and generate bills, all through a text-based menu.

The project was developed as part of the Python Essentials course on the VITyarthi platform. It uses only the core Python concepts taught in the course, without depending on an external database or other software.

## Problem Statement

Small clinics and hospitals may still use paper registers or separate spreadsheets to manage patient records, doctor information, appointments, and billing. Managing information this way can make it difficult to find records quickly and can also lead to mistakes, such as booking a doctor for two patients at the same time or calculating a bill incorrectly.

To address these problems, this project provides a simple Patient Information Management System using Python. A receptionist or administrator can use the program to manage patient and doctor records, schedule appointments, handle cancellations, and generate bills from one place.

The system is designed mainly for learning and demonstration purposes. It shows how basic Python concepts can be combined to create a useful real-world application.

## Objectives
To manage patient records by allowing users to add, view, search, update, and delete patient information.
To maintain doctor information such as doctor ID, name, specialization, and consultation fee.
To provide an appointment booking system with predefined time slots.
To prevent a doctor from being booked for two patients at the same date and time.
To allow users to cancel appointments and book another appointment when required.
To generate bills based on consultation fees, medicine costs, test charges, and discounts.
To validate user input and handle common errors without crashing the program.
To demonstrate the use of Python data structures, functions, and control statements.
To divide the program into separate modules so that it is easier to understand and maintain.
To use Git and GitHub for managing and maintaining the project.
Out of Scope

This project is intended as a learning project rather than a complete hospital management system. It does not provide permanent data storage, so all information is stored in memory and is lost when the program is closed.

The project also does not include a graphical user interface, multiple-user access, login or authentication, or integration with real hospital services such as insurance companies, pharmacies, or laboratory equipment.

Features such as walk-in patient management and some advanced record-management operations may also be limited depending on the implemented modules. The main purpose of the project is to demonstrate core Python programming concepts in a practical application, rather than provide production-ready hospital software.

## Features
Patient Management
Add new patient records.
View registered patients.
Search, update, and delete patient information.
Doctor Management
Add new doctors along with details such as specialization and consultation fee.
View and search doctor records.
Appointment Booking
Book appointments for patients with available doctors.
Use predefined appointment time slots.
Automatically check doctor availability to prevent double booking.
Appointment Management
View scheduled appointments.
Search for appointments.
Cancel existing appointments.
Billing
Generate patient bills using consultation fees, medicine costs, test charges, and discounts.
View previously generated bills.

## Functional Requirements

1. Patient Management

The system should allow users to add, view, search, update, and delete patient records.

2. Doctor Management

The system should allow users to add, view, and search doctor records. Each doctor record can contain details such as doctor ID, name, specialization, and consultation fee.

3. Appointment Management

The system should allow users to book, view, search, and cancel appointments. Before booking an appointment, the system checks whether the selected doctor is already booked for the chosen date and time.

4. Billing Management

The system should allow users to generate and view patient bills. The total bill is calculated using the consultation fee, medicine charges, test charges, and any applicable discount.

5. Error Handling

The system should handle errors that may occur during different operations and display clear, user-friendly messages. Invalid inputs, such as incorrect IDs or unavailable appointment slots, should be handled without causing the program to crash.

## Non-Functional Requirements
1. Usability
The system should have a simple menu-driven interface.
Prompts and error messages should be easy to understand.
The system should be suitable for basic clinic administration and beginner-level use.
2. Reliability
The system should prevent appointment double booking.
Patient and doctor IDs should be validated before performing related operations.
Invalid user input should be handled without terminating the program unexpectedly.
3. Performance
Dictionaries and sets are used where appropriate to make record searching and checking faster.
The system is designed for small clinic datasets rather than large hospital databases.
4. Maintainability
Patient, doctor, appointment, and billing functions are organized into separate modules.
The modular structure makes the code easier to understand, test, modify, and extend in the future.

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

The project was developed using basic Python and does not require any external libraries or database software.

* **Programming Language:** Python 3.10 or newer is recommended.
* **Data Storage:** The program stores data temporarily in memory using built-in Python data structures.

  * **Dictionaries:** Used for storing patient, doctor, and billing records.
  * **Lists:** Used for maintaining appointment records.
  * **Tuples:** Used to store the available appointment time slots.
  * **Sets:** Used to keep track of already-booked doctor, date, and time combinations.
* **External Libraries:** None. The program uses only Python's built-in features.
* **Database:** No external database is required.
* **Code Editor:** Visual Studio Code.
* **Version Control:** Git and GitHub.

## Steps to Install and Run the Project

### 1. Install Python

If Python isn't already installed, download and install it from the official Python website.

After installation, open the terminal and check whether Python is installed correctly:

```bash
python --version
```

The project is recommended to be run using Python 3.10 or newer.

### 2. Get the Project Files

There are two ways to get the project.

You can clone the GitHub repository using:

```bash
git clone <your-repository-url>
cd <repository-folder>
```

Alternatively, you can download the `clinic_management_system.py` file and place it in a folder of your choice.

### 3. Run the Program

No additional packages need to be installed because the project uses only Python's built-in features.

Open the terminal inside the project folder and run:

```bash
python clinic_management_system.py
```

### 4. Use the Menu

After starting the program, a numbered menu will appear in the terminal.

Enter the number corresponding to the operation you want to perform and press **Enter**. The program will then display the required prompts and guide you through the selected operation.

## Instructions for Testing

The system can be tested manually by running the program and checking each menu option. The following sequence can be used as a basic test procedure.

### 1. Add a Patient

Select **option 1** and enter sample patient details. Note the generated Patient ID, such as `P1`.

### 2. View Patients

Select **option 2** and check whether the patient you added is displayed correctly.

### 3. Add a Doctor

Select **option 3**, enter the doctor's details, and note the generated Doctor ID, such as `D1`.

### 4. View Doctors

Select **option 4** and confirm that the doctor appears with the correct information.

### 5. Book an Appointment

Select **option 5** and use the Patient ID and Doctor ID created earlier. Choose a date and one of the available time slots.

Note the generated Appointment ID, such as `A1`.

### 6. Test Double-Booking Prevention

Try booking the **same doctor at the same date and time** again.

The program should reject the booking. This confirms that the double-booking prevention feature is working correctly.

### 7. View Appointments

Select **option 6** and check whether the appointment appears with the status **"Booked"**.

### 8. Cancel an Appointment

Select **option 7** and enter the Appointment ID.

After cancellation, view the appointments again and confirm that its status has changed to **"Cancelled"**.

Try booking the same doctor at the same time again. The slot should now be available.

### 9. Generate a Bill

Select **option 8** and generate a bill for the patient using the doctor's consultation fee along with any required medicine, test, or discount amounts.

### 10. View Bills

Select **option 9** and confirm that the generated bill is displayed and the total amount has been calculated correctly.

### 11. Delete a Patient

Select **option 10** and enter the Patient ID.

The patient's record and related appointment records should be removed.

### 12. Verify Patient Deletion

Try accessing the deleted patient's details and view the appointments again.

The patient's information should no longer be available, and their related appointments should also have been removed.

### 13. Exit the Program

Select **option 0** and confirm that the program closes normally.

## Testing Invalid Input

Invalid inputs should also be tested to make sure the program handles errors properly. Examples include:

* Entering an unknown Patient ID.
* Entering an unknown Doctor ID.
* Choosing an invalid menu option.
* Entering a time slot that isn't available.
* Trying to book an already occupied appointment slot.
* Entering incorrect or incomplete information.

The program should display a clear error message instead of crashing.

## Limitations

### 1. Command-Line Interface Only

The system currently works through a text-based terminal interface. It doesn't have a graphical interface, so it may be less convenient for users who aren't familiar with command-line programs.

### 2. Data Isn't Permanently Stored

Patient, doctor, appointment, and billing information is stored only while the program is running. Once the program is closed, all the data is lost.

### 3. Limited Date Validation

The system checks whether the date follows the required **DD-MM-YYYY** format, but it doesn't fully verify whether the entered date is a valid calendar date.

### 4. Fixed Appointment Time Slots

The program provides a predefined list of appointment times. Users can't create or customize their own time slots.

### 5. No User Authentication

There is currently no login system. The program doesn't have separate access levels for administrators, doctors, receptionists, or patients.

### 6. Basic Search and Record Management

The system provides basic record management but doesn't include advanced search, filtering, or sorting options.

### 7. Basic Billing

The billing system currently handles consultation fees, medicine charges, test charges, and discounts. It doesn't provide detailed professional invoices or maintain complete payment information.

### 8. Limited Input Validation

Some inputs, such as phone numbers and consultation fees, have basic validation. More detailed validation could be added to improve the reliability of the system.

## Future Improvements

The current project provides the basic functionality required for a small clinic management system, but several improvements could make it more useful in the future.

### 1. Database Integration

A database such as **MySQL or SQLite** could be added to permanently store patient, doctor, appointment, and billing information.

### 2. Graphical User Interface

The command-line interface could be replaced or extended with a graphical interface using **Tkinter, PyQt**, or a web-based interface. This would make the system easier to use.

### 3. User Authentication

A secure login system could be introduced with different roles, such as:

* Admin
* Doctor
* Receptionist
* Patient

Each role could have access to only the features relevant to them.

### 4. Advanced Appointment Management

The appointment system could be improved by adding features such as:

* Creating custom time slots.
* Rescheduling appointments.
* Searching appointments by date or doctor.
* Maintaining a complete appointment history.

### 5. Improved Data Validation

More detailed validation could be added for:

* Valid calendar dates.
* Phone numbers.
* Positive fee values.
* Required fields.
* Duplicate patient information.

### 6. Enhanced Billing

The billing system could be expanded to include:

* Detailed invoices.
* Payment status.
* Different payment methods.
* Tax calculation.
* Printable or downloadable bills.

### 7. Patient Search and Medical Records

The system could store additional patient information, such as medical history, diagnosis, prescriptions, and previous visits. This would make the system more useful for maintaining a patient's overall record.

### 8. Reports and Analytics

The system could generate useful reports, including:

* Total number of patients.
* Daily appointments.
* Doctor-wise appointments.
* Revenue reports.

### 9. Data Backup and Export

Users could be given options to export records to formats such as **CSV or PDF**. A backup feature could also be added to reduce the risk of losing important records.

### 10. Web or Cloud Deployment

In the future, the project could be converted into a web-based application. Authorized users would then be able to access the system from different devices instead of running it only on a local computer.
