# A hospital patient tracking system is restructuring its patient records
# The current format is fragmented, each patient is represented as a list of
# namedtuple. Each element contains a different piece of information about
# the patient
# Your task is to write a function that merges all of the information into one
# namedtuple, named Patient, in the order that it's provied to the function

# For example
# PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
# personal_details = PersonalDetails(date_of_birth = '06-04-1972')
# Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
# complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')

# print(MedicalRecord.merge(personal_details, complexion))

# Should print>
# Patient(date_of_birth='06-04-1972', eye_color='Blue', hair_color='Black')

from collections import namedtuple

class MedicalRecord:
    @staticmethod
    def merge(*records):
        Patient = namedtuple('Patient', ['date_of_birth', 'eye_color', 'hair_color'])
        patient = Patient(date_of_birth = records[0][0], eye_color = records[1][0], hair_color = records[1][1])
        # print(patient)

        return patient

PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972')
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')

print(MedicalRecord.merge(personal_details, complexion))
