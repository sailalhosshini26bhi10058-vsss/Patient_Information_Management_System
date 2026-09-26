#PATIENT MANAGEMENT SYSTEM

doctors_dict={}
doc_counter=1

def add_doc():
    global doctors_dict, doc_counter
    print("\n** Add New Doctor **")
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    
    # For invalid fee value
    try:
        fees = float(input("Enter consultation fees: "))
    except ValueError:
        print("Invalid amount! Setting default fees to 500.0")
        fees = 500.0

    doc_id = "D" + str(doc_counter)
    doc_counter += 1

    doctors_dict[doc_id] = {"name": name,"specialization": specialization,"consultation_fee": fees}
    print("Doctor added successfully. Doctor ID: ",doc_id)
    
     

def view_docs():
    print("\n** All Doctors **")
    if len(doctors_dict) == 0:
        print("No doctors found.")
        return

    print("\n** DOCTORS RECORD **")
    for doc_id in doctors_dict:
        d = doctors_dict[doc_id]
        print(f"ID: {doc_id} | Name: {d['name']} | Speciality: {d['specialization']} | Fee: Rs.{d['consultation_fee']}")