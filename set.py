set={1,2,3,5} #duplicate value are not alow
print(set)
print(type(set))

rollNo={234,456,789,876,786,546,65}
name={"Abhi","Aman","varun","Aman"}
print(rollNo)
print(name)
##add

s={34,45,67,67,43}
s.add(100)
print(s)

s.update([35,67,89])

##remove an elements
s.remove(100)
print(s)

x=s.pop() #remove random
print("remove random",x)


s.clear()#clear all alement
print(s)

s1={32,22,33,44,55}#deep copy
s2=s1
s2.add(300)
print(s1)
print(s2)

s2=s1.copy()#salo copy
s2.add(400)
print(s1)
print(s2)

#built in function
s3={67,78,48,76,65}
print(len(s3))
print(min(s3))
print(max(s3))
print(sum(s3))
s4={False,0,-6}
print(any(s4))
s5={0,3,5}
print(all(s5))

print(s3)

#set operation
#union s1 U s2
s1={1,4,6,5,8,6}
s2={1,4,6,8,90,67}

print(s1.union(s2))

#intersection
print(s1.intersection(s2))

#difference

print(s1.difference(s2))
print(s2.difference(s1))

##forzenset
s1={23,56,89,12,20,30}
s1=frozenset({12,20,30})
print(s1)
#s1.add(40) #Attribute error , forzenset has no attrebute add

#Remove Duplicate roll number in the set (attendence system)
"""attendance_scans = ["BCA21", "BCA05", "BCA21", "BCA33", "BCA05", "BCA47"]
print("Original attendance ", attendance_scans)

present_students = set(attendance_scans)
print("Present students ", present_students)

print(f"Total present: {len(present_students)}")"""

##Checking valid indian state name 

indian_states = {"Uttar Pradesh", "Maharashtra", "Kerala", "Punjab", "Bihar", "Gujarat"}

user_input = input("Enter state name :")

if user_input in indian_states:      # O(1) lookup — much faster than list for large data
    print("Valid state")
else:
    print("Invalid state")

##comon subject bitween two semster 
sem3_subjects = {"DBMS", "OOP", "DSA", "Maths-III", "Digital Electronics"}
sem4_subjects = {"OOP", "DBMS", "OS", "CN", "Web Technology"}

common = sem3_subjects & sem4_subjects       

# or sem3_subjects.intersection(sem4_subjects)

print(f"Repeated subjects: {common}")        # {'OOP', 'DBMS'}

#Merging pincode lists from two venders(union ,no duplicate)
zomato_serviceable = {"281001", "281004", "281006", "282001"}   # Mathura, Agra pincodes
swiggy_serviceable = {"281004", "281006", "282002", "282010"}

all_serviceable = zomato_serviceable | swiggy_serviceable

# all_serviceable = zomato_serviceable.union(swiggy_serviceable)

print("Merging pincode list=",all_serviceable)

#students who upplied for scolership but have not submited income certificate
scholarship_applicants = {"A101", "A102", "A103", "A104", "A105"}
income_cert_submitted = {"A101", "A103", "A105"}

pending = scholarship_applicants - income_cert_submitted
print(f"Pending documents: {pending}")     # {'A102', 'A104'}

#detecting addhar Pan duplicate entries during bulk data

pan_numbers = ["ABCDE1234F", "PQRSX5678K", "ABCDE1234F", "LMNOP9876Q","LMNOP9876Q"]

if len(pan_numbers) != len(set(pan_numbers)):
    print("⚠️ Duplicate PAN numbers found in upload sheet!") 
    duplicates = [pan for pan in set(pan_numbers) if pan_numbers.count(pan) > 1]
    print(duplicates)