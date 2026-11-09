"""
models.py
---------
The classes (blueprints) used by the Vaccination Tracker.

Classes in this file:
    Vaccine            - describes one vaccine (name, doses needed, gap between doses)
    VaccinationRecord  - one patient's history for ONE vaccine
    Patient            - an anonymous patient who can receive vaccines

DPG note (privacy): we never store names, phone numbers or addresses.
A patient is only an anonymous code (e.g. PT-001), an age and a district.
"""

from datetime import date, datetime, timedelta

# ---------------------------------------------------------------------------
# A TUPLE: the official vaccine list. Tuples cannot be changed once created,
# which is exactly what we want for a fixed schedule.
# Each item is: (vaccine name, doses required, days between doses)
# ---------------------------------------------------------------------------
VACCINE_CATALOGUE = (
    ("BCG", 1, 0),
    ("Polio", 4, 28),
    ("Pentavalent", 3, 28),
    ("Measles", 2, 180),
    ("Yellow Fever", 1, 0),
    ("COVID-19", 2, 28),
)


class Vaccine:
    """A vaccine and its schedule rules."""

    def __init__(self, name, doses_required, interval_days):
        self.name = name
        self.doses_required = doses_required
        self.interval_days = interval_days

    # ----- instance method -----
    def describe(self):
        """Return a short sentence describing the vaccine."""
        if self.doses_required == 1:
            return f"{self.name}: 1 dose required"
        return (f"{self.name}: {self.doses_required} doses required, "
                f"{self.interval_days} days apart")

    # ----- class methods (they work on the class, not on one object) -----
    @classmethod
    def from_tuple(cls, data):
        """Build a Vaccine object from one tuple of VACCINE_CATALOGUE."""
        name, doses_required, interval_days = data
        return cls(name, doses_required, interval_days)

    @classmethod
    def find(cls, name):
        """Look up a vaccine by name (not case sensitive). Returns None if not found."""
        for item in VACCINE_CATALOGUE:
            if item[0].lower() == name.strip().lower():
                return cls.from_tuple(item)
        return None

    @classmethod
    def all_names(cls):
        """Return a tuple with every vaccine name."""
        return tuple(item[0] for item in VACCINE_CATALOGUE)


class VaccinationRecord:
    """Remembers how many doses of ONE vaccine a patient has had."""

    def __init__(self, vaccine, first_dose_date):
        self.vaccine = vaccine              # a Vaccine object
        self.doses_given = 1
        self.last_dose_date = first_dose_date

    def add_dose(self, dose_date):
        """Count one more dose given on dose_date."""
        self.doses_given += 1
        self.last_dose_date = dose_date

    def is_complete(self):
        """True when all required doses have been given."""
        return self.doses_given >= self.vaccine.doses_required

    def next_due_date(self):
        """Date the next dose is due, or None if the course is complete."""
        if self.is_complete():
            return None
        return self.last_dose_date + timedelta(days=self.vaccine.interval_days)


class Patient:
    """An anonymous patient (privacy-respecting: no name is stored)."""

    # ----- class attribute: shared by ALL patients -----
    total_patients = 0

    def __init__(self, patient_id, age, district):
        self.patient_id = patient_id
        self.age = age
        self.district = district
        # A DICTIONARY: vaccine name -> VaccinationRecord
        self.vaccinations = {}
        Patient.total_patients += 1

    # ----- instance methods -----
    def record_dose(self, vaccine, dose_date):
        """
        Record that this patient received a dose of `vaccine` (a Vaccine object).
        Returns a message telling what happened.
        """
        record = self.vaccinations.get(vaccine.name)
        if record is None:
            self.vaccinations[vaccine.name] = VaccinationRecord(vaccine, dose_date)
            return f"{vaccine.name} dose 1 recorded for {self.patient_id}."
        if record.is_complete():
            return (f"{self.patient_id} has already completed {vaccine.name}. "
                    "No extra dose recorded.")
        record.add_dose(dose_date)
        return f"{vaccine.name} dose {record.doses_given} recorded for {self.patient_id}."

    def update_record(self, age=None, district=None):
        """Change the patient's age and/or district."""
        if age is not None:
            self.age = age
        if district is not None:
            self.district = district

    def is_fully_vaccinated(self, vaccine_name):
        """True if the patient finished the course for this vaccine."""
        record = self.vaccinations.get(vaccine_name)
        return record is not None and record.is_complete()

    def display_info(self):
        """Print everything we know about this patient."""
        print(f"Patient ID : {self.patient_id}")
        print(f"Age        : {self.age}")
        print(f"District   : {self.district}")
        if not self.vaccinations:
            print("Vaccines   : none recorded yet")
            return
        print("Vaccines   :")
        for name, record in self.vaccinations.items():
            needed = record.vaccine.doses_required
            line = f"   - {name}: {record.doses_given}/{needed} doses"
            if record.is_complete():
                line += " (COMPLETE)"
            else:
                line += f" (next due {record.next_due_date().isoformat()})"
            print(line)

    # ----- class methods -----
    @classmethod
    def create_new(cls, age, district):
        """Create a patient and give it the next automatic ID (PT-001, PT-002 ...)."""
        new_id = f"PT-{cls.total_patients + 1:03d}"
        return cls(new_id, age, district)

    @classmethod
    def get_total_patients(cls):
        """How many Patient objects have been created so far."""
        return cls.total_patients

    # ----- static methods (helpers that need no object and no class) -----
    @staticmethod
    def is_valid_age(age):
        """Age must be a whole number from 0 to 120."""
        return isinstance(age, int) and 0 <= age <= 120

    @staticmethod
    def parse_date(text):
        """Turn 'YYYY-MM-DD' into a date. Returns None if the text is not a valid date."""
        try:
            return datetime.strptime(text.strip(), "%Y-%m-%d").date()
        except ValueError:
            return None
