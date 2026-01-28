#generate tests files
import time 
import random
import matplotlib.pyplot as plt
import numpy as np
from matcher import gale_shapley
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


def plot_graphs(n_values, time_values_gs, time_values_verifier):
    print("Plotting graphs...Close graphs tab to end program.")
    x_points = np.array(n_values)
    y_points_gs = np.array(time_values_gs)
    y_points_verifier = np.array(time_values_verifier)

    fig, ax = plt.subplots(2, 1, figsize=(8, 10), layout='constrained')

    gs_graph = ax[0]
    verifier_graph = ax[1]

    # Gale-shapley runtime graph
    gs_graph.plot(x_points, y_points_gs, marker='o', color='blue')
    gs_graph.set_title("Gale-Shapley Runtime")
    gs_graph.set_xlabel("Number of hospitals/students (n)")
    gs_graph.set_ylabel("Runtime (seconds)")
    gs_graph.grid(True)

    # Verifier runtime graph
    verifier_graph.plot(x_points, y_points_verifier, marker='x', color='red')
    verifier_graph.set_title("Verifier Runtime")
    verifier_graph.set_xlabel("Number of hospitals/students (n)")
    verifier_graph.set_ylabel("Runtime (seconds)")
    verifier_graph.grid(True)

    plt.show()

def performance_test():
    n_values = [1,2,4,8,16,32,64,128,256,512]
    time_values_gs = []
    time_values_verifier = []
    
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


        input_filepath = f"../tests/test_{n}.in"
        output_filepath = f"../tests/test_{n}.out"
        generate_test_file(input_filepath, n, hospital_preferences, student_preferences)

        # time the algorithm - no need to load the preferences as they've been pre-created above
        start_time = time.time()
        hospital_matches, student_matches = gale_shapley(hospital_preferences, student_preferences, output_filepath)
        end_time = time.time()

        total_time = end_time - start_time
        time_values_gs.append(total_time)

        # time the verifier 
        start_time = time.time()
        verifyMatches(hospital_matches, student_matches, hospital_preferences, student_preferences)
        end_time = time.time()
        total_time = end_time - start_time
        time_values_verifier.append(total_time)
        
    
    plot_graphs(n_values, time_values_gs, time_values_verifier)

performance_test()
