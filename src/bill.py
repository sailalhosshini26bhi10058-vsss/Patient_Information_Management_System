import src.patients as patients
import src.doctors as doctors

patients_dict = patients.patients_dict
doctors_dict = doctors.doctors_dict

bill_counter = 1  # Counter for bill ID generation
bills_dict={} # Empty dictionary to store bills

def generate_bill():
    global bill_counter, bills_dict         
    print("\n** Generate Bill **")

    patient_id = input("Enter patient ID: ")
    if patient_id not in patients_dict:
        print("Patient ID not found.")
        return

    doc_id = input("Enter doctor ID : ") #For generating bill

    if doc_id not in doctors_dict:
        print("Doctor ID not found.")
        return

    consultation_fee =float(doctors_dict[doc_id]["consultation_fee"])
    medicine_fee = float(input("Enter medicine fee: "))
    discount = float(input("Enter discount (0 if none): "))
    test_fee = float(input("Enter test fee (0 if none): "))

    total = consultation_fee + medicine_fee + test_fee - discount

    bill_id = "B" + str(bill_counter).zfill(3)
    bill_counter += 1

    bills_dict[bill_id] = {"patient_id": patient_id, "consultation_fee": consultation_fee, "medicine_fee": medicine_fee,"discount": discount,"test_fee":test_fee,total": total}

    print(f"\nBill generated. Bill ID: {bill_id}")


    labels = ["Consultation Fees", "Medicine Fees", "Test Fees", "Discount"]
    values = [consultation_fee, medicine_fee, test_fee, discount]

    for i in range(len(labels)): 
        print(f"{labels[i]}: {values[i]}")

    print(f"Total Amount: {total}")


def view_bills():
    print("\n** All Bills **")
    if len(bills_dict) == 0:
        print("No bills found.")
        return
    for bill_id in bills_dict:
        b = bills_dict[bill_id]
        print(f"{bill_id } | Patient: {b['patient_id']} | Total: {b['total']}")
        