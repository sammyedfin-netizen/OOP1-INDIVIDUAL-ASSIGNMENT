"""
main.py
-------
Vaccination Tracker - menu program.

Run it with:    python main.py
Quick demo:     python main.py demo
"""

import sys

from models import Patient, Vaccine
from tracker import (add_patient_record, display_all_records, find_patient,
                     show_summary, load_demo_data)


def ask_age():
    """Keep asking until the user types a valid age."""
    while True:
        text = input("Age (0-120): ").strip()
        if text.isdigit() and Patient.is_valid_age(int(text)):
            return int(text)
        print("Please type a whole number between 0 and 120.")


def register_patient(patients):
    age = ask_age()
    district = input("District (e.g. Bo): ").strip() or "Unknown"
    patient = Patient.create_new(age, district)
    add_patient_record(patients, patient)
    print(f"Registered. The patient's anonymous ID is {patient.patient_id}")


def record_vaccination(patients):
    patient = find_patient(patients, input("Patient ID (e.g. PT-001): "))
    if patient is None:
        print("Patient not found.")
        return
    print("Available vaccines:", ", ".join(Vaccine.all_names()))
    vaccine = Vaccine.find(input("Vaccine name: "))
    if vaccine is None:
        print("Unknown vaccine.")
        return
    dose_date = Patient.parse_date(input("Date given (YYYY-MM-DD): "))
    if dose_date is None:
        print("Invalid date. Use the format YYYY-MM-DD, for example 2026-11-08.")
        return
    print(patient.record_dose(vaccine, dose_date))


def view_patient(patients):
    patient = find_patient(patients, input("Patient ID: "))
    if patient is None:
        print("Patient not found.")
    else:
        patient.display_info()


def update_patient(patients):
    patient = find_patient(patients, input("Patient ID: "))
    if patient is None:
        print("Patient not found.")
        return
    print("Press Enter to keep the old value.")
    age_text = input(f"New age (now {patient.age}): ").strip()
    district = input(f"New district (now {patient.district}): ").strip()
    new_age = None
    if age_text:
        if age_text.isdigit() and Patient.is_valid_age(int(age_text)):
            new_age = int(age_text)
        else:
            print("Invalid age ignored.")
    patient.update_record(age=new_age, district=district or None)
    print("Record updated.")


def show_menu():
    print()
    print("===== VACCINATION TRACKER =====")
    print("1. Register a new patient")
    print("2. Record a vaccine dose")
    print("3. View one patient")
    print("4. View all patients")
    print("5. Update a patient")
    print("6. Show summary")
    print("7. Load demo data")
    print("8. List vaccines")
    print("0. Exit")


def run_menu():
    patients = {}                      # the ONE data structure: a dictionary
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        print()
        if choice == "1":
            register_patient(patients)
        elif choice == "2":
            record_vaccination(patients)
        elif choice == "3":
            view_patient(patients)
        elif choice == "4":
            display_all_records(patients)
        elif choice == "5":
            update_patient(patients)
        elif choice == "6":
            show_summary(patients)
        elif choice == "7":
            load_demo_data(patients)
            print("Demo data loaded.")
        elif choice == "8":
            for item in Vaccine.all_names():
                print(Vaccine.find(item).describe())
        elif choice == "0":
            print(f"Goodbye! Patients created in this session: {Patient.get_total_patients()}")
            break
        else:
            print("Invalid option. Please choose a number from the menu.")


def run_demo():
    """Non-interactive demonstration (good for screenshots)."""
    patients = {}
    print("Loading demo data...\n")
    load_demo_data(patients)
    display_all_records(patients)
    show_summary(patients)
    print()
    print("Is PT-001 fully vaccinated against BCG?",
          patients["PT-001"].is_fully_vaccinated("BCG"))
    print("Is PT-001 fully vaccinated against Polio?",
          patients["PT-001"].is_fully_vaccinated("Polio"))
    print("Total Patient objects created:", Patient.get_total_patients())
    print("Is 150 a valid age?", Patient.is_valid_age(150))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        run_demo()
    else:
        run_menu()
