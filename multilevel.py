class Hospital():
    def __init__(self):
        self.hospital_name = input("Enter the Hospital Name: ")
        self.location = input("Enter the Location: ")
        self.hospital_phone = int(input("Enter the Hospital Phone Number: "))
    def display(self):
        print("Hospital Name is", self.hospital_name)
        print("Location is", self.location)
        print("Hospital Phone Number is", self.hospital_phone)
class Department():
    def __init__(self):
        self.department_name = input("Enter the Department Name: ")
        self.doctor_name = input("Enter the Doctor Name: ")
    def details(self):
        print("Department Name is", self.department_name)
        print("Doctor Name is", self.doctor_name)
class Patient(Hospital, Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name = input("Enter the Patient Name: ")
        self.age = int(input("Enter the Age: "))
        self.gender = input("Enter the Gender: ")
        self.phone = int(input("Enter the Patient Phone Number: "))
        self.admission_date = input("Enter the Admission Date: ")
        self.bed_no = int(input("Enter the Bed Number: "))
        self.discharge_date = ""
    def set_discharge(self):
        self.discharge_date = input("Enter the Discharge Date: ")
    def full_summary(self):
        Hospital.display(self)
        Department.details(self)
        print("Patient Name:", self.patient_name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Patient Phone:", self.phone)
        print("Admission Date:", self.admission_date)
        print("Bed Number:", self.bed_no)
        if(self.discharge_date==""):
            print("Not Discharged")
        else:
            print("Discharge Date:", self.discharge_date)
p1 = Patient()
# p1.full_summary()
p1.set_discharge()
p1.full_summary()
# class A:
#     def f(self):
#         print("In First Function F")
#     def f(self,a):
#         print("In Second Function F")
#     def f(self,a,b):
#         print("In Third Function F")
# a=A()
# # a.f()
# a.f(10)
# # a.f(10,20)