from src import bill
from src import patients
from src import doctors
from src import appointment

# ********** MAIN MENU **********

patients_dict = {}
doctors_dict = {}


def main_menu():         # WHILE LOOP: Runs continuously until an option is chosen
    global patients_dict
    global doctors_dict
    global appointment_list
    global bills_dict

    while True:
        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. View Appointments")
        print("7. Cancel Appointment")
        print("8. Generate Bill")
        print("9. View Bills")
        print("10. Delete Patient")
        print("0. Exit")

        choice = input("Enter your choice (0-9): ")

        # IF/ELIF/ELSE: Directing flow based on input
        if choice == "1":
            patients.new_patient()
        elif choice == "2":
            patients.view_patients()
        elif choice == "3":
            doctors.add_doc()
        elif choice == "4":
            doctors.view_docs()
        elif choice == "5":
            appointment.book_appointment()
        elif choice == "6":
            appointment.view_appointments()
        elif choice == "7":
            appointment.cancel_appointment()
        elif choice == "8":
            bill.generate_bill()
        elif choice == "9":
            bill.view_bills()
        elif choice== "10":
            patients.delete_patient()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break # break-> Exits the loop and ends the program
        else:
            print("Invalid selection! Please enter a number between 0 and 9.")


# ********** PROGRAM START **********
if __name__ == "__main__":
    main_menu()
