
import time

print("Welcome to Report Card Generator\n")
time.sleep(2)

name = input("Enter your name: ")
time.sleep(1)
roll_no = input("Enter your roll number: ")
time.sleep(1)
math_marks = int(input("Enter your math marks: "))
time.sleep(1)
science_marks = int(input("Enter your science marks: "))
time.sleep(1)
english_marks = int(input("Enter your english marks: "))
time.sleep(1)
sst_marks = int(input("Enter your SST Marks: "))
time.sleep(2)
print("\n")
print("Analyzing...\n")
time.sleep(3)
print("Generating...\n")
time.sleep(3)
print("Almost Done...\n\n")
time.sleep(2)
# # math_grade = None
# science_grade = None
# english_grade = None
# sst_grade = None
# def check_math_grade():
if (math_marks>=90):
    math_grade = "A"
elif(math_marks>=70 and math_marks<90):
    math_grade = "B"
elif(math_marks>=50 and math_marks<70):
    math_grade = "C"
else:
    math_grade = "F"

# check_math_grade()

# def check_science_grade():
if (science_marks>=90):
    science_grade = "A"
elif(science_marks>=70 and science_marks<90):
    science_grade = "B"
elif(science_marks>=50 and science_marks<70):
    science_grade = "C"
else:
    science_grade = "F"

# check_science_grade()

# def check_english_grade():
if (english_marks>=90):
    english_grade = "A"
elif(english_marks>=70 and english_marks<90):
    english_grade = "B"
elif(english_marks>=50 and english_marks<70):
    english_grade = "C"
else:
    english_grade = "F"

# check_english_grade()

# def check_sst_grade():
if (sst_marks>=90):
    sst_grade = "A"
elif(sst_marks>=70 and sst_marks<90):
    sst_grade = "B"
elif(sst_marks>=50 and sst_marks<70):
    sst_grade = "C"
else:
    sst_grade = "F"

# check_sst_grade()




print("R E P O R T  C A R D")
time.sleep(0.2)
print("---------------------")
time.sleep(1)
print(f"{name.title()}  -  {roll_no}","\n")
time.sleep(1)
print("SUBJECT | MARKS | PERCENTAGE | GRADE ")
time.sleep(0.2)
print(f"MATHS   |  {math_marks}   |   {math_marks} %     | {math_grade}    ")
time.sleep(0.5)
print(f"SCIENCE |  {science_marks}   |   {science_marks} %     | {science_grade}    ")
time.sleep(0.5)
print(f"ENGLISH |  {english_marks}   |   {english_marks} %     | {english_grade}    ")
time.sleep(0.5)
print(f" SST    |  {sst_marks}   |   {sst_marks} %     | {sst_grade}    ")