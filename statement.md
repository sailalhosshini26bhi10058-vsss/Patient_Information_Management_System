# Problem Statement

Many small clinics and hospitals still use paper registers or separate spreadsheets to manage patient records, doctor information, appointments, and billing. This can make it difficult to find patient information quickly and increases the chances of mistakes, such as accidentally booking a doctor for two patients at the same time or making errors while calculating bills manually.

This project addresses these issues by developing a simple, menu-driven **Patient Information Management System** using Python. The system provides a single program through which receptionists or administrative staff can register patients and doctors, schedule and manage appointments, and generate patient bills.

The system doesn't require a database server or any external software, making it simple to set up and suitable for a small clinic environment.

# Scope of the Project

The project focuses on the basic day-to-day activities that may be handled at the front desk of a small clinic or hospital.

The system covers:

* Storing and viewing patient and doctor information.
* Scheduling appointments using a fixed set of available time slots.
* Automatically preventing a doctor from being booked for two patients at the same date and time.
* Cancelling appointments and making the cancelled time slot available for booking again.
* Generating and viewing bills based on consultation fees, medicine costs, test charges, and discounts.
* Removing patient records along with their related appointment information.

## Out of Scope

The project has been kept simple so that it focuses on demonstrating core Python programming concepts. It doesn't include permanent data storage, so all information is stored in memory and is lost when the program is closed.

The system also doesn't include a graphical user interface, multi-user access, login or authentication, or integration with external hospital services such as insurance systems, pharmacies, or laboratory equipment.

Advanced features such as walk-in patient registration, advanced patient and doctor searching, detailed record editing, and other hospital-level management functions aren't included.

Therefore, this project is intended as a **learning and academic project**, rather than a production-ready hospital management system.

# Target Users

The system is mainly designed for small healthcare setups and the staff responsible for basic administrative tasks.

### Receptionists / Front-Desk Staff

Receptionists are the primary users of the system. They can register patients, add doctor information, schedule appointments, and manage cancellations.

### Billing Staff

Billing staff can use the system to generate patient bills and review previously generated bills.

### Small Clinics or Single-Doctor Practices

The system is suitable for small clinics or individual doctor practices that need basic record and appointment management without the complexity of a complete hospital information system.

# High-Level Features

## 1. Patient Management

The system allows users to register new patients, view the registered patient list, and remove patient records along with their related information.

## 2. Doctor Management

Users can register doctors and store details such as their name, specialization, and consultation fee. The system also allows users to view the registered doctor list.

## 3. Appointment Scheduling

Users can book appointments using the available predefined time slots. The system automatically checks whether the selected doctor is already booked for the chosen date and time.

## 4. Appointment Handling

Users can view scheduled appointments and cancel existing appointments. When an appointment is cancelled, the time slot becomes available for another booking.

## 5. Billing

The system can generate an itemized bill containing the consultation fee, medicine charges, test charges, and applicable discount. Previously generated bills can also be viewed.

# Non-Functional Requirements

## 1. Usability

* The system should have a simple menu-driven interface.
* Prompts and error messages should be clear and easy to understand.
* The system should be simple enough for basic clinic administration.

## 2. Reliability

* The system should prevent appointment double-booking.
* Patient and doctor IDs should be checked before performing related operations.
* Invalid user input should be handled without causing the program to crash.

## 3. Performance

* Dictionaries and sets are used for efficient record lookup and appointment availability checks.
* The system is designed to handle small clinic datasets efficiently.

## 4. Maintainability

* Patient, doctor, appointment, and billing functionality are organized into separate modules.
* The modular structure makes the program easier to understand, test, modify, and extend in the future.
