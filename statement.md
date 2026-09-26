# Problem Statement

Hospitals and small clinics often rely on paper registers or scattered
spreadsheets to manage patient records, doctor schedules, appointments, and
billing. This makes it slow to look up a patient's history, easy to
accidentally double-book a doctor, and error-prone when calculating bills by
hand.

This project addresses that problem by building a simple, menu-driven
**Hospital Management System** in Python. It gives a receptionist or admin
staff member a single program to register patients and doctors, schedule and
manage appointments, handle walk-in patients, and generate accurate bills —
without needing a database server or any external software.

## Scope of the Project

The project covers the core day-to-day operations of a small clinic or
hospital front desk:

- Storing and viewing patient and doctor information
- Scheduling appointments against a fixed set of time slots, with automatic
  prevention of double-booking a doctor for the same date and time
- Cancelling appointments and freeing up the slot for re-booking
- Managing a walk-in queue for patients without appointments
- Searching for a patient by name
- Generating and viewing bills based on consultation fee, medicine cost,
  test cost, and discount

**Out of scope:** the project does not include persistent storage (all data
is kept in memory and is lost when the program closes), a graphical user
interface, multi-user access, user login/authentication, or integration with
real hospital systems (e.g. insurance, pharmacy, or lab equipment). It is
built as a learning project to demonstrate core programming concepts, not as
production software.

## Target Users

- **Receptionists / front-desk staff** — the primary users, who register
  patients, book appointments, and manage the walk-in queue
- **Billing staff** — who generate and review patient bills
- **Small clinics or single-doctor practices** — as an organization, this
  tool is aimed at smaller setups that don't need (or can't afford) a full
  hospital information system

## High-Level Features

1. **Patient Management** — register new patients and view the full patient list
2. **Doctor Management** — register new doctors with their specialization and consultation fee, and view the full doctor list
3. **Appointment Scheduling** — book appointments against a fixed set of time slots, with built-in double-booking prevention
4. **Appointment Handling** — view all appointments and cancel existing ones
5. **Walk-in Queue Management** — add walk-in patients to a first-come-first-served queue, serve the next patient, and view who is waiting
6. **Patient Search** — find a patient quickly by full or partial name
7. **Billing** — generate an itemized bill (consultation, medicine, tests, discount) and review past bills
