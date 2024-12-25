from sat.solver_sat import solve_sat
from sat.verifier_sat import verify_sat_solution
from threesat.solver_3sat import solve_3sat
from reduction.sat_to_3sat import reduce_sat_to_3sat
from core.argparser import parse_args
from analysis.generator import generate_random_sat_instance, generate_random_3sat_instance
from analysis.profiler import measure_execution_time, measure_memory_usage
import matplotlib.pyplot as plt  
import core.globals
import csv
try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    print("[WARNING] 'tqdm' library not found. Progress bar will not be displayed.")
    print("You can install it using 'pip install tqdm' for enhanced CLI feedback.\n")

def main():
    parse_args()
    print("===== Program Configuration =====")
    print(f"Algorithm:         {core.globals.algorithm}")
    print(f"Analyser:          {core.globals.analyser}")
    print(f"Clauster file:     {core.globals.clauster_file}")
    print(f"Number of test:    {core.globals.test_number}")
    print(f"Graph enabled:     {core.globals.graph}")
    print(f"nb_vars:           {core.globals.nb_vars}")
    print(f"nb_clauses:        {core.globals.nb_clauses}")
    print("=================================\n")
    looping = core.globals.test_number > 0
    verifying = core.globals.algorithm != "SAT-2-3SAT"
    if looping:
        core.globals.logs = "off"
    if core.globals.clauster_file and not False:
        if core.globals.logs == "info": print("[INFO] Reading instance from file (not implemented in this example).")
        clauses = []
        nb_vars = 0
    else:
        nb_vars = core.globals.nb_vars
        nb_clauses = core.globals.nb_clauses
        if core.globals.algorithm == "3SAT" and not looping:
            clauses = generate_random_3sat_instance(nb_vars, nb_clauses)
        else:
            clauses = generate_random_sat_instance(nb_vars, nb_clauses, clause_size_min=core.globals.clause_size_min, clause_size_max=core.globals.clause_size_max)

        if core.globals.logs == "info": print("[INFO] Generated random clauses:")
        for idx, clause in enumerate(clauses, 1):
            if core.globals.logs == "info": print(f"  Clause {idx}: {clause}")

    if core.globals.algorithm == "SAT":
        if core.globals.logs == "info": print("\n[INFO] Running SAT solver...")
        algorithm = [solve_sat,(clauses, nb_vars)]
        generator = [generate_random_sat_instance,(core.globals.clause_size_min,core.globals.clause_size_max)]

    elif core.globals.algorithm == "3SAT":
        if core.globals.logs == "info": print("\n[INFO] Running 3-SAT solver... (placeholder: using solve_sat for demonstration)")
        algorithm = [solve_3sat,(clauses, nb_vars)]
        generator = [generate_random_sat_instance,()]

    elif core.globals.algorithm == "SAT-2-3SAT":
        if core.globals.logs == "info": 
            print("\n[INFO] Performing SAT → 3-SAT reduction...")
        algorithm = [reduce_sat_to_3sat,(clauses,nb_vars)]
        generator = [generate_random_sat_instance,(core.globals.clause_size_min,core.globals.clause_size_max)]
    else:
        raise Exception("algorithm can either be SAT,3SAT or SAT-2-3SAT")
        
    if core.globals.analyser == "TIME" and not looping:
        if core.globals.logs == "info": print("[INFO] Time analysis is selected.")
        result,total_time = measure_execution_time(algorithm[0],*algorithm[1])
        if core.globals.logs == "info": 
            print(f"[INFO] Execution Time [Total = {total_time}]")
            print(f"[INFO] Result: {result}")
    elif core.globals.analyser == "MEMORY" and not looping:
        if core.globals.logs == "info": print("[INFO] Memory analysis is selected.")
        result,current,peak = measure_memory_usage(algorithm[0],*algorithm[1])
        if core.globals.logs == "info": 
            print(f"[INFO] Memory Usage [peak = {peak}, current = {current}, consumation = {peak - current}]")
            print(f"[INFO] Result: {result}")
    if verifying and not looping: 
        verifying_result = verify_sat_solution(clauses,result)
        print("[INFO] Result Satisfied !" if verifying_result else "[INFO] Result NOT Satisfied !")

    if core.globals.graph:
        if core.globals.test_number < 10:
            raise Exception("you have to change test number if you wanna use the graph option; at least 10\nyou can do : python main.py -t 10 -g")
        if core.globals.logs == "info": 
            print("[INFO] Graph generation is enabled.")
    if not looping: return
    
    x,y = [],[] # nb_clauser,execution time / memory usage
    total_iterations = len(range(3, core.globals.test_number, core.globals.step))
    if TQDM_AVAILABLE:
        iterator = tqdm(range(3, core.globals.test_number, core.globals.step), desc="Running Tests", unit="test")
    else:
        iterator = range(3, core.globals.test_number, core.globals.step)
        
    for idx, nb_clauses in enumerate(iterator, 1):
        if core.globals.analyser == "TIME":
            clauses = generator[0](nb_vars, nb_clauses,*generator[1])
            result, total_time = measure_execution_time(algorithm[0], clauses, nb_clauses)
            x.append(nb_clauses)
            y.append(total_time)
            metric = f"Time: {total_time:.4f}s"
        else:
            clauses = generator[0](nb_vars, nb_clauses,*generator[1])
            result, current, peak = measure_memory_usage(algorithm[0], clauses, nb_clauses)
            memory_consumption = peak - current
            x.append(nb_clauses)
            y.append(memory_consumption) 
            metric = f"Memory: {memory_consumption:.4f}MB"

        if TQDM_AVAILABLE:
            tqdm.write(f"Test {idx}/{total_iterations} - Clauses: {nb_clauses}, {metric}")
        else:
            print(f"Test {idx}/{total_iterations} - Clauses: {nb_clauses}, {metric}")
    
    csv_filename = f"{core.globals.algorithm}_{core.globals.analyser}_analysis.csv"
    try:
        with open(f'output/{csv_filename}', mode='w+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Number of Clauses', core.globals.analyser])
            for clause, metric in zip(x, y):
                writer.writerow([clause, metric])
        if core.globals.logs == "info":
            print(f"[INFO] Analysis data saved to {csv_filename}")
    except Exception as e:
        print(f"[ERROR] Failed to write to CSV file: {e}")
    
    if core.globals.graph:
        plt.figure(figsize=(10, 6))
        if core.globals.analyser == "TIME":
            plt.plot(x, y, marker='o', linestyle='-', color='b', label='Execution Time (s)')
        elif core.globals.analyser == "MEMORY":
            plt.plot(x, y, marker='s', linestyle='--', color='r', label='Memory Consumption (MB)')
        
        plt.xlabel('Number of Clauses')
        plt.ylabel('Execution Time (s)' if core.globals.analyser == "TIME" else 'Memory Consumption (MB)')
        plt.title(f"{core.globals.analyser} Analysis for {core.globals.algorithm}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        
        plt.show()
        plt.savefig('analysis_plot.png')
        plt.close()

if __name__ == "__main__":
    main()
