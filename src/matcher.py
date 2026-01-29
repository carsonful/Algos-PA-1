# Task A: Matching Engine
import os
import copy

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

from verifier import verifyMatches

def load_preferences(filepath):
    hospital_preferences = []
    student_preferences = []

    # check for empty file
    if(os.path.getsize(filepath) == 0):
        print("Input file is empty.")
        return

    with open(filepath, "r") as file:
        contents = [line.rstrip() for line in file]

    n = int(contents[0])
    
    # check for valid n
    if(n < 1):
        print("Invalid number of hospitals/students:", n)

    # check for valid number of lines
    if len(contents) != (2*n + 1):
        print("Invalid number of lines in input file.")
        return

    # hospital preferences
    for i in range (1, n+1):
        string_hospital_preferences = contents[i].split()
        if(len(string_hospital_preferences) != n):
            print("A hospital preference list does not contain n values.")
            return
        hospital_preferences.append([int(num) for num in string_hospital_preferences])

    # student preferences
    for i in range (n+1, 2*n+1):
        string_student_preferences = contents[i].split()
        if(len(string_student_preferences) != n):
            print("A student preference list does not contain n values.")
            return
        student_preferences.append([int(num) for num in string_student_preferences])


    # print("Number of hospitals/students:", n)
    # print("Hospital preferences:", hospital_preferences)
    # print("Student preferences:", student_preferences)

    return hospital_preferences, student_preferences


def gale_shapley(hospital_preferences, student_preferences, output_file):
    h_pref = copy.deepcopy(hospital_preferences)
    s_pref = copy.deepcopy(student_preferences)

    hospital_match = [None for none in range(len(hospital_preferences))]
    student_match = [None for none in range(len(student_preferences))]
    n = len(hospital_preferences)
    h_stack = [i for i in range(n)]  # stack of free hospitals

    # -1 IS THE TRUE INDEX OF THE STUDENT/HOSPITAL 

    while h_stack: # while there is a free hospital
        h = h_stack.pop() 
        print(f"Hospital {h+1} is free and looking for a match.")

        while h_pref[h]: # iterate through hospital's preference list
            pref = h_pref[h][0]  # get the top preference
            if (student_match[pref - 1] is None): 
                # Student is free
                hospital_match[h] = pref # set hospital match to its applicant 
                student_match[pref - 1] = h + 1 # set student's match to hospital
               # print(f"Hospital {h+1} matched with Student {pref}.")
                break # exit for loop since hospital is no longer free



            elif(student_match[pref-1] is not None):
                # check if student prefers this hospital over current match
                current_hospital = student_match[pref - 1] # get current hospital matched to student
                student_pref_list = s_pref[pref - 1] # get student's preference list


                if student_pref_list.index(h + 1) < student_pref_list.index(current_hospital):
                    # Student prefers new hospital
                    # print(f"Student {pref} prefers Hospital {h+1} over Hospital {current_hospital}.")
                    hospital_match[h] = pref # set new hospital match to student
                    student_match[pref - 1] = h + 1 # set student match to new hospital
                    # Previous hospital becomes free
                    h_stack.append(current_hospital - 1) # add previous hospital back to free stack
                    hospital_match[current_hospital - 1] = None # unset previous hospital's match
                    # print(f"Hospital {current_hospital} is now free.")
                    break # exit for loop since hospital is no longer free


                else:
                    # print(f"Student {pref} rejects Hospital {h+1}.")
                    h_pref[h].pop(0)  # remove student from hospital's preference list

    # print to console
    print("Final Matches: ")
    for hospital, student in enumerate(hospital_match):
            print((f"{hospital + 1} {student}"))

    # create output file
    with open(output_file, "w") as file:
        for hospital, student in enumerate(hospital_match):
            file.write(f"{hospital + 1} {student}\n")
    
    # return matches for later use
    return hospital_match, student_match


if __name__ == "__main__":
    hospital_preferences, student_preferences = load_preferences("../tests/ex2.in") # change input file here
    hospital_matches, student_matches = gale_shapley(hospital_preferences, student_preferences, "../tests/ex2.out") # change output file here
    verifyMatches(hospital_matches, student_matches, hospital_preferences, student_preferences)