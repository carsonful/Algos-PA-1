#generate tests files
import time 
from matcher import load_input


def generate_test_file(filepath, n, hospital_preferences, student_preferences):
    with open (filepath, "w") as file:
        file.write(str(n) + "\n")
        
        for prefs in hospital_preferences:
            line = " ".join(str(num) for num in prefs)
            file.write(line + "\n")
        
        for prefs in student_preferences:
            line = " ".join(str(num) for num in prefs)
            file.write(line + "\n")

def performance_test():
    n_values = [1,2,4,8,16,32,64,128,256,512,10000]
    
    for n in n_values:
        #  dummy preferences for testing
        hospital_preferences = [list(range(1, n+1)) for _ in range(n)]
        student_preferences = [list(range(1, n+1)) for _ in range(n)]
        
        filepath = f"test_{n}.in"
        generate_test_file(filepath, n, hospital_preferences, student_preferences)
        

        # we aren't measuring the time to generate the file, this is just a placeholder for now
        start_time = time.time()
        load_input(filepath)
        end_time = time.time()
        
        print(f"Time taken to load input for n={n}: {end_time - start_time:.6f} seconds")

performance_test()
