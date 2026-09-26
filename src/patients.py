#PATIENT MANAGEMENT SYSTEM

patients_dict={}                 #Empty Dictionary
pat_count=1                             #Counter for patient ID generation
def new_patient():                                    #To input new patient info
    global patients_dict, pat_count

    print("\n** Add New Patient **")

    while True:
        try:
            name = input("Enter patient name: ")
            if name:
                break
            print("Name cannot be empty. Please enter a valid name.")
        except ValueError as e:
            print(f"Invalid input! {e}")



    while True:
        try:
            age = int(input("Enter age: "))
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
                print("Invalid input! Please enter a valid 10 digits for phone number.")
        except ValueError:
            print("Invalid input! Please enter a valid integer for phone number.")


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

from src import appointment
appointment_list = appointment.appointment_list

#To delete patient record
def delete_patient():

    global patients_dict
    global appointment_list

    print("\n** Delete Patient **")

    p_id = input("Enter patient ID to delete: ")
    if p_id in patients_dict:
        del patients_dict[p_id]
        print(f"Patient with ID {p_id} has been deleted.")

        if p_id in appointment_list:
            del appointment_list[p_id]

    else:
        print("Patient ID not found.")

