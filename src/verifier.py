# Task B: Verifier
"""
(a)  Checks validity: each hospital and each student is matched to exactly one partner, with no duplicates. 
And (b) checks stability: confirms there is no blocking pair.

"""

def verifyMatches(hospital_matches, student_matches, hospital_preferences, student_preferences):
    print("Verifying matches...")
    # Hospital matches in the format of [2, 3, 1] where it is H1-S2, H2-S3, H3-S1

    # Verify validity (unique matches)
    if(len(set(hospital_matches)) != len(hospital_matches)):
        print("INVALID validity due to lack of unique matches.")
        return
    
    # Verify stability
    for hospital_index, student in enumerate(hospital_matches):
        h_pref = hospital_preferences[hospital_index]
        student_matched_rank = h_pref.index(student) # where the matched student ranks

        if(student_matched_rank == 0):
            continue # if the student is the hospital's #1 choice, we go to next iteration, bc it needs to be a mutual thing
        
        # Find students that are ranked higher than current match
        higher_ranked_students = [hospital_preferences[hospital_index][i] for i in range(0, student_matched_rank)]
        # print("Hospital", hospital_index+1, "has higher ranked students ", higher_ranked_students)

        # Check if the higher ranked students prefer this hospital more over their matching
        for higher_student in higher_ranked_students:
            higher_student_index = higher_student - 1
            matched_hospital = student_matches[higher_student_index]

            s_pref = student_preferences[higher_student_index]

            if(s_pref.index(matched_hospital) > s_pref.index(hospital_index+1)):
                print("UNSTABLE due to hospital", (hospital_index + 1), "and student", higher_student)
                return
            
    print("VALID STABLE")

