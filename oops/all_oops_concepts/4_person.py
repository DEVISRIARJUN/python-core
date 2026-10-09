# 4. Create classes:
# • Person → base
# • MedicalStaff(Person)
# • Doctor(MedicalStaff)
# • Surgeon(Doctor)
# Requirements:
# • Hide sensitive data (e.g., salary, patient notes)
# • Abstract method perform_duty()
# • Each level overrides the method with more specific behavior
# • Use super() to chain constructor calls

class Person:
    