#PATIENT MANAGEMENT SYSTEM

patients_dict={}                 #Empty Dictionary (to store patient information)
pat_count=1                             #Counter for patient ID generation
def new_patient():                                    #To input new patient info
    global patients_dict, pat_count                      # declaring global- can be used outside of function

    print("\n** Add New Patient **")

    while True:
        try:
            name = input("Enter patient name: ")                          #User inputs name
            if name:
                break
            print("Name cannot be empty. Please enter a valid name.")           #Name cannot be empty
        except ValueError as e:
            print(f"Invalid input! {e}")



    while True:
        try:
            age = int(input("Enter age: "))                               #Age has to be a number
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for age.")


    while True:
        try:
            gender = input("Enter gender: ")
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for age.")
       
    while True:
        try:
            number = int(input("Enter phone number: "))
            if len(str(number)) == 10:                                        
                break
            else:
                print("Invalid input! Please enter a valid 10 digits for phone number.")   #Phone number MUST have 10 digits
        except ValueError:
            print("Invalid input! Please enter a valid integer for phone number.")  #must be numerical values


    history = input("Enter medical history (or 'None'): ")

     # ID generation
    p_id = "P" + str(pat_count)
    pat_count += 1


    # Storing patient info 
    patients_dict[p_id] = {"name": name,"age": age,"gender": gender,"phone no.": number,"medical_history": history}


    print("Patient added successfully. Patient ID: ",p_id)



#To display patients' record
def view_patients():
    global patients_dict
    print("\n** Patients records **")

    # For empty records
    if len(patients_dict) == 0:
        print("\nNo patients found.")
        return
    
    # Retrieval and Printing of Patients details 
    print("\n** PATIENTS RECORD **")
    for p_id, p in patients_dict.items():
        print(f"ID: {p_id} | Name: {p['name']} | Age: {p['age']} | Gender: {p['gender']} | Phone: {p['phone no.']} | History: {p['medical_history']}")
        print("Patient added successfully. Patient ID: ",p_id)

from src import appointment                            #importing another .py file
appointment_list = appointment.appointment_list          # using modules from that file into this

#To delete patient record
def delete_patient():

    global patients_dict
    global appointment_list

    print("\n** Delete Patient **")

    p_id = input("Enter patient ID to delete: ")
    if p_id in patients_dict:
        del patients_dict[p_id]

        # Remove all appointments belonging to the deleted patient
        for appt in appointment_list[:]:
            if appt["patient_id"] == p_id:
              slot_key = (appt["doctor_id"], appt["date"], appt["time"])
              appointment.booked_slots.discard(slot_key)
              appointment_list.remove(appt)

        print(f"Patient with ID {p_id} and related records have been deleted.")

    else:
        print("Patient ID not found.")

