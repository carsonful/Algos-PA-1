# Task A: Matching Engine

"""
Pseudocode for Algorithm (Source: Chapter-1-2026 PowerPoint)

Initialize each person and hospital to be free.
while (some hospital is free and hasn't been matched/assigned to every applicant) {
    Choose such a hospital h
    a = 1st applicant on h's list to whom h has not been matched
    
    if (a is free)
        assign h and a
    else if (a prefers h to her/his current assignment h')
        assign a and h, and h' has a slot free
    else
        a rejects h
}

"""

def load_input(filepath):
    hospital_preferences = []
    student_preferences = []

    with open(filepath, "r") as file:
        contents = [line.rstrip() for line in file]

    n = int(contents[0])

    # hospital preferences
    for i in range (1, n+1):
        string_hospital_preferences = contents[i].split()
        hospital_preferences.append([int(num) for num in string_hospital_preferences])

    # student preferences
    for i in range (n+1, 2*n+1):
        string_student_preferences = contents[i].split()
        student_preferences.append([int(num) for num in string_student_preferences])
    
   # print("Number of hospitals/students:", n)
   # print("Hospital preferences:", hospital_preferences)
   # print("Student preferences:", student_preferences)


    
   
   
load_input("../tests/ex.in")
