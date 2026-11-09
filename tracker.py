"""
tracker.py
----------
Simple functions that work with the ONE data structure of this project:
a dictionary called `patients` where   key = patient ID,  value = Patient object.

Example:  {"PT-001": <Patient>, "PT-002": <Patient>}
"""

from models import Patient, Vaccine


def add_patient_record(patients, patient):
    """ADD a patient to the dictionary. Returns True if added, False if the ID already exists."""
    if patient.patient_id in patients:
        return False
    patients[patient.patient_id] = patient
    return True


def display_all_records(patients):
    """DISPLAY every patient in the dictionary."""
    if not patients:
        print("No patients registered yet.")
        return
    print(f"--- {len(patients)} registered patient(s) ---")
    for patient_id, patient in patients.items():
        patient.display_info()
        print()


def find_patient(patients, patient_id):
    """Return the Patient with this ID, or None."""
    return patients.get(patient_id.strip().upper())


def show_summary(patients):
    """Print simple statistics (counts only, no personal data)."""
    print("--- Vaccination summary ---")
    print(f"Total patients: {len(patients)}")
    for name in Vaccine.all_names():
        started = 0
        complete = 0
        for patient in patients.values():
            if name in patient.vaccinations:
                started += 1
            if patient.is_fully_vaccinated(name):
                complete += 1
        print(f"{name:<13} started: {started}   fully vaccinated: {complete}")


def load_demo_data(patients):
    """Fill the dictionary with a few anonymous example patients."""
    p1 = Patient.create_new(2, "Western Area Urban")
    p2 = Patient.create_new(1, "Bo")
    p3 = Patient.create_new(34, "Kenema")
    for p in (p1, p2, p3):
        add_patient_record(patients, p)

    polio = Vaccine.find("Polio")
    measles = Vaccine.find("Measles")
    bcg = Vaccine.find("BCG")
    covid = Vaccine.find("COVID-19")

    p1.record_dose(bcg, Patient.parse_date("2024-05-01"))
    p1.record_dose(polio, Patient.parse_date("2024-06-01"))
    p1.record_dose(polio, Patient.parse_date("2024-06-29"))
    p2.record_dose(measles, Patient.parse_date("2025-01-10"))
    p3.record_dose(covid, Patient.parse_date("2025-03-01"))
    p3.record_dose(covid, Patient.parse_date("2025-03-29"))
