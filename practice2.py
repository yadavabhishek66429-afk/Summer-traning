#operator and operends
"""a=45
b=55
sum=a+b
print(sum)
#flor Division
print(34//4)

#comperision operator
print(3>2) #return true or false
print(3<2)
print(2==4)
print(2!=4)
print(3>=5)
print(3<=5)

#Logicale operator
print(4>3 and 8>5)
print(3>5 or 9>5)
print(not(3>5 or 9>5))

#assignment operator
a=35
a+=5
print(a)
a-=6
print(a)
a*=2
print(a)
a/=3
print(a)"""

#Identity Operator(is or is not)
a="Abhi"
b="abhi"

print(a is b)
print(a is not b)

#Bitwise Operator
print(bin(8))#print Binary number
a=10
b=8
#and (&) operator 
print(a & b)
#or (|) Operator
print(a | b)
#XOR (^) operator
print(a ^ b)

#left shift and right shift binary operation
print(10>>1) #left shift
print(10<<2)#Right shift

#Membership Operator (in or not in)
name="Abhishek Yadav"

print("Yadav" not in name)

#conditional statment 
marks=87
if marks>=90:
    print("you will get mobile phone")
else:
    print("you will not get phone")

print("Thank you")

#if-elif-else
marks=97

if marks>=90:
    print("Grade : A")
elif marks>=80 & marks<90:
    print("grade: B")
elif marks>=50 & marks<80:
    print("Grade: C") 
else:
    print("Fale")

#nested if condition
marks=79

if marks>=80:
    print("You will get a new phone ")
    if marks>95:
        print("you can go for trip")
else:
    print("not phone for one month")

age=20
if age>=18:
    print("eligible for vote :")

print("hello")

marks=70
res="pass" if marks >=40 else "fail"
print(f"Result:{res}")

age=25
if age <=12:
    print("Child ")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Young adult")
else:
    print("Adult.")