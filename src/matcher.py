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
    
    print("Number of hospitals/students:", n)
    # print("Hospital preferences:", hospital_preferences)
    # print("Student preferences:", student_preferences)
    gale_shapley(hospital_preferences, student_preferences)
    # check for edge cases as per instructions: empty file and 1 hospital/student, equal number of hospital and students
    # call some matching function here later

# krithika's fixed version
def run_gale_shapley(hospital_preferences, student_preferences):
    h_pref = hospital_preferences
    s_pref = student_preferences

    n = len(hospital_preferences)
    hospital_matches = [None] * n # ex: [-1, -1, 2] where hospital 3 is matched to student 2
    student_matches = [None] * n # ex: [-1, 3, -1] where student 2 is matched to hospital 3
    
    while(None in hospital_matches):
        # choose the first occurrence of None
        current_hospital = hospital_matches.index(None) + 1 # index = 0 -> hospital = 1

        # find top student from current_hospital's preference list (pretend the list is a queue)
        current_student = h_pref[current_hospital - 1][0] # if we already proposed to them and later unmatched, they wont be in this list

        # check if student is free
        if(student_matches[current_student-1] == None):
            student_matches[current_student-1] = current_hospital
            hospital_matches[current_hospital - 1] = current_student

        else:
            student_current_match = student_matches[current_student-1]
            student_pref_list = s_pref[current_student - 1]

            if(student_pref_list.index(current_hospital) < student_pref_list.index(student_current_match)):
                # set the student's old hospital to unmatched
                old_hospital = student_matches[current_student-1]
                hospital_matches[old_hospital-1] = -1
                
                # remove the student from the old hospital's preferences so it doesn't propose to it again
                h_pref[old_hospital - 1].pop(0)

                # set the student and hospital matches
                student_matches[current_student-1] = current_hospital
                hospital_matches[current_hospital - 1] = current_student
            else:
                # rejection case
                h_pref[current_hospital-1].pop(0)
                # The same hospital continues to the next person in the while loop until it matches with a student


def gale_shapley(hospital_preferences, student_preferences):
    h_pref = hospital_preferences
    s_pref = student_preferences

    hospital_match = [None for none in range(len(hospital_preferences))]
    student_match = [None for none in range(len(student_preferences))]
    n = len(hospital_preferences)
    h_stack = [i for i in range(n)]  # stack of free hospitals
    print(student_match)
    print(hospital_match)

    # -1 IS THE TRUE INDEX OF THE STUDENT/HOSPITAL 

    while h_stack: # while there is a free hospital
        h = h_stack.pop() 
        print(f"Hospital {h+1} is free and looking for a match.")

        for pref in h_pref[h]: # iterate through hospital's preference list
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
                    h_pref[h].remove(pref)  # Remove student from hospital's preference list
                    continue # continue to next preference in the list within the for loop

    print("Final Hospital Matches:", hospital_match)
    print("Final Student Matches:", student_match)


if __name__ == "__main__":
    load_input("../tests/ex.in")