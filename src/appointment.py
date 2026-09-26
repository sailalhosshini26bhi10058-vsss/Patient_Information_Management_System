#PATIENT MANAGEMENT SYSTEM

time_slots = ("09:00 AM", "11:00 AM", "02:00 PM", "04:00 PM", "06:00 PM")
def show_time_slots():
    print("\nTime slots available:")
    
    for slot in time_slots:
        print("Timing- ", slot)

from src import patients
from src import doctors

patients_dict = patients.patients_dict
doctors_dict = doctors.doctors_dict


appointment_list = []
booked_slots = set()
appointment_counter = 1  # Counter for appointment ID generation

def book_appointment():
    global appointment_counter, appointment_list, booked_slots
    print("\n** Book Appointment **")

    # Checks if data exists or not
    if len(patients_dict) == 0 or len(doctors_dict) == 0:
        print("Error: You need at least one patient and one doctor registered first.")
        return

    p_id = input("Enter patient ID: ")
    if p_id not in patients_dict:
        print("Error!: Patient ID not found.")
        return

    doc_id = input("Enter doctor ID: ")
    if doc_id not in doctors_dict:
        print("Error!: Doctor ID not found.")
        return

    def check_date(date):
        if len(date) != 10 or date[2] != '-' or date[5] != '-':
            print("Error!: Invalid date format. Please enter date in DD-MM-YYYY format.")
            return False
        return True

    date = input("Enter date (DD-MM-YYYY): ")
    if not check_date(date):
        return

    time = input(f"Enter chosen time slot exactly as shown-{time_slots}: ")

    if time not in time_slots:
        print("Error!: Invalid time slot selected.")
        return

    # Accumulating details into a single tuple
    slot_key = (doc_id, date, time)
    
    # SET LOOKUP: Incredibly fast check to prevent double booking
    if slot_key in booked_slots:
        print("Error!: This doctor is already booked at that date and time.")
        return

    appointment_id = "A" + str(appointment_counter)
    appointment_counter += 1

    # To add an appointment record :

    appointment_list.append({"appointment_id": appointment_id, "patient_id": p_id,"doctor_id": doc_id,"date": date,"time": time,"status": "Booked"})

    # To save the slot 
    booked_slots.add(slot_key)
    print(f"Appointment booked successfully. Appointment ID: {appointment_id}")


def view_appointments():
     global appointment_list

     print("\n** All Appointments **")

     if len(appointment_list) == 0:
        print("No appointments found.")
        return
    
     for appt in appointment_list:
        print(f"{appt['appointment_id']} | Patient: {appt['patient_id']} | "
              f"Doctor: {appt['doctor_id']} | {appt['date']} {appt['time']} | "
              f"Status: {appt['status']}")

def cancel_appointment():
    print("\n** Cancel Appointment **")
    appointment_id = input("Enter appointment ID to cancel: ")

    for appt in appointment_list:
        if appt["appointment_id"] == appointment_id:
            appt["status"] = "Cancelled"
            slot_key = (appt["doctor_id"], appt["date"], appt["time"])
            booked_slots.discard(slot_key)   # empty the slot
            print("Appointment cancelled.")
            return

    print("Appointment ID not found.")