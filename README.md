# Vaccination Tracker (PROG211 – Object-Oriented Programming 1)

**Student name:** Samuel Sesay
**Student ID:** 905006247
**Module:** PROG211 Object-Oriented Programming 1 – Limkokwing University of Creative Technology, Sierra Leone
**Assignment:** Real-World Solutions under DPG Standards (Individual Assignment, 10%)
**Domain chosen:** Health – **Vaccination Tracker**

---

## 1. What is this project?

The Vaccination Tracker is a small Python program that helps a health worker keep track of which vaccines a patient has received, how many doses are still needed, and when the next dose is due. It solves a real problem: paper vaccination cards get lost, and missed doses leave children and adults unprotected.

The program is written with **Object-Oriented Programming (OOP)** and follows **Digital Public Goods (DPG)** principles.

## 2. Project files

| File | Purpose |
|------|---------|
| `models.py` | The classes: `Vaccine`, `VaccinationRecord`, `Patient`, and the vaccine tuple |
| `tracker.py` | Functions that add, display, find and summarise records in the dictionary |
| `main.py` | The menu program (what the user runs) |
| `sample_output_demo.txt` | Example output of `python main.py demo` |
| `README.md` | This file |

## 3. How the assignment requirements are met

| Requirement | Where in the code |
|-------------|-------------------|
| **Task 1 – at least two classes with attributes and methods** | Three classes: `Vaccine`, `VaccinationRecord`, `Patient` (in `models.py`) |
| **Object creation and interaction** | A `Patient` creates `VaccinationRecord` objects, which hold `Vaccine` objects |
| **Task 2 – only one data structure** | A **dictionary** `patients` (key = patient ID, value = `Patient` object) |
| **Function to add and display records** | `add_patient_record()` and `display_all_records()` in `tracker.py` |
| **Tuples (optional, extra marks)** | `VACCINE_CATALOGUE` is a tuple of tuples (a fixed vaccine schedule) |
| **Task 3 – instance method** | `record_dose()`, `update_record()`, `display_info()` in `Patient` |
| **Task 3 – class method (`@classmethod`)** | `Patient.create_new()`, `Patient.get_total_patients()`, `Vaccine.find()` |
| **Static method (bonus)** | `Patient.is_valid_age()`, `Patient.parse_date()` |

## 4. How the project follows Digital Public Goods (DPG) standards

| DPG principle | How this project follows it |
|---------------|-----------------------------|
| **Open-source** | The full source code is published on GitHub and uses only the Python standard library, so anyone can read, copy, improve and reuse it. |
| **Inclusive and accessible design** | Plain-text menu with numbered options and clear messages; no mouse, internet or expensive hardware needed; works on any computer that has Python; input errors give friendly help instead of crashing. |
| **Privacy-respecting** | No names, phone numbers, addresses or ID card numbers are stored. A patient is only an anonymous code (e.g. `PT-001`), an age and a district. Data is kept in memory only and is erased when the program closes. |
| **Modular and reusable** | The code is split into three files with one job each. The classes in `models.py` can be reused in another program (for example a web or mobile app) without changes. |

## 5. How to run

1. Install **Python 3.8 or newer** from <https://www.python.org/downloads/> (tick **"Add Python to PATH"** during installation).
2. Download or clone this repository and open a terminal in the project folder.
3. Start the program:

```
python main.py
```

(On some computers the command is `python3 main.py` or `py main.py`.)

For a quick automatic demonstration, run:

```
python main.py demo
```

No extra libraries need to be installed.

## 6. Example usage (sample input / output)

**Command:** `python main.py demo`

```
Loading demo data...

--- 3 registered patient(s) ---
Patient ID : PT-001
Age        : 2
District   : Western Area Urban
Vaccines   :
   - BCG: 1/1 doses (COMPLETE)
   - Polio: 2/4 doses (next due 2024-07-27)

Patient ID : PT-002
Age        : 1
District   : Bo
Vaccines   :
   - Measles: 1/2 doses (next due 2025-07-09)

Patient ID : PT-003
Age        : 34
District   : Kenema
Vaccines   :
   - COVID-19: 2/2 doses (COMPLETE)

--- Vaccination summary ---
Total patients: 3
BCG           started: 1   fully vaccinated: 1
Polio         started: 1   fully vaccinated: 0
...
```

**Interactive example (`python main.py`):**

```
Choose an option: 1
Age (0-120): 5
District (e.g. Bo): Bo
Registered. The patient's anonymous ID is PT-001

Choose an option: 2
Patient ID (e.g. PT-001): PT-001
Vaccine name: Polio
Date given (YYYY-MM-DD): 2026-11-08
Polio dose 1 recorded for PT-001.

Choose an option: 3
Patient ID: PT-001
Patient ID : PT-001
Age        : 5
District   : Bo
Vaccines   :
   - Polio: 1/4 doses (next due 2026-12-06)
```

## 7. Limitations and future work

- Data is not saved when the program closes (this protects privacy but limits real use). A future version could save encrypted data to a file or database.
- Text menu only; a future version could add a simple web or mobile interface in local languages.
- The vaccine schedule is a simplified teaching example and is **not** official medical guidance.

## 8. Licence

Released under the MIT Licence – free to use, study, change and share. (Add a `LICENSE` file on GitHub: *Add file → Create new file → name it `LICENSE` → choose "MIT" template.*)
