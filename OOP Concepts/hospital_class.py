class Hospital:
    def __init__(self, hospital_name, location, total_beds, contact_number, specialization):
        self.hospital_name = hospital_name
        self.location = location
        self.total_beds = total_beds
        self.contact_number = contact_number
        self.specialization = specialization

    def details(self):
        print(f"Hospital Name  : {self.hospital_name}")
        print(f"Location       : {self.location}")
        print(f"Total Beds     : {self.total_beds}")
        print(f"Contact Number : {self.contact_number}")
        print(f"Specialization : {self.specialization}")
        print("-" * 30)


hospital1 = Hospital("Sterling Hospital", "Rajkot", 250, "+91-281-2480000", "Multi-Specialty")
hospital2 = Hospital("Zydus Hospitals", "Ahmedabad", 550, "+91-79-66190201", "Cardiology & Oncology")
hospital3 = Hospital("Kiran Multi Super Speciality", "Surat", 750, "+91-261-7161111", "Multi-Specialty")
hospital4 = Hospital("Bhailal Amin General Hospital", "Vadodara", 320, "+91-265-2280601", "Orthopedics & Trauma")
hospital5 = Hospital("GG Government Hospital", "Jamnagar", 1500, "+91-288-2550211", "General & Emergency")

all_hospitals = [hospital1, hospital2, hospital3, hospital4, hospital5]

for h in all_hospitals:
    h.details()