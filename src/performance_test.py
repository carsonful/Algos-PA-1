#generate tests files
import time 
import random
import matplotlib.pyplot as plt
import numpy as np
from matcher import load_input, gale_shapley, run_gale_shapley
from verifier import verifyMatches


def generate_test_file(filepath, n, hospital_preferences, student_preferences):
    with open (filepath, "w") as file:
        file.write(str(n) + "\n")
        
        for prefs in hospital_preferences:
            line = " ".join(str(num) for num in prefs)
            file.write(line + "\n")
        
        for prefs in student_preferences:
            line = " ".join(str(num) for num in prefs)
            file.write(line + "\n")


def plot_graphs(n_values, time_values_k, time_values_c):
    print("Plotting graphs...")
    x_points = np.array(n_values)
    y_points_k = np.array(time_values_k)
    y_points_c = np.array(time_values_c)


    print("n values:", x_points)
    print("Algorithm Krithika times:", y_points_k)
    print("Algorithm Carson times:", y_points_c)

    plt.plot(x_points, y_points_k, marker='o', linestyle='-', color='b', label='Algorithm 1 (Krithika)')
    plt.plot(x_points, y_points_c, marker='s', linestyle='--', color='r', label='Algorithm 2 (Carson)')

    plt.xlabel("Number of hospitals/students (n)")
    plt.ylabel("Time to Run Gale Shapley (seconds)")
    plt.legend()

    plt.show()




def performance_test():
    n_values = [1,2,4,8,16,32,64,128,256,512]
    time_values_k = []
    time_values_c = []
    
    for n in n_values:
        # generate a random preference list for each hospital and student
        hospital_preferences = []
        student_preferences = []  
        for i in range(n):
            pref = list(range(1, n+1))
            random.shuffle(pref)
            hospital_preferences.append(pref)     

        for i in range(n):
            pref = list(range(1, n+1))
            random.shuffle(pref)
            student_preferences.append(pref)


        filepath = f"test_{n}.in"
        generate_test_file(filepath, n, hospital_preferences, student_preferences)
        

        load_input(filepath)

        # algorithm 1: krithika
        start_time = time.time()
        run_gale_shapley(hospital_preferences, student_preferences)
        end_time = time.time()

        total_time = end_time - start_time
        time_values_k.append(total_time)

        # algorithm 2: carson
        start_time = time.time()
        run_gale_shapley(hospital_preferences, student_preferences)
        end_time = time.time()

        total_time = end_time - start_time
        time_values_c.append(total_time)

        # need to do the same for just the verifier too
        
        # print(f"Time taken to load input for n={n}: {end_time - start_time:.6f} seconds")
    
    plot_graphs(n_values, time_values_k, time_values_c)

performance_test()
