from stripsProblem import STRIPS_domain, Strips, Planning_problem
from stripsForwardPlanner import Forward_STRIPS

from air_cargo_heuristics import h_movement_cost
from air_cargo_problems import create_air_cargo_problem1, create_air_cargo_problem2, create_air_cargo_problem3, create_air_cargo_problem4

from searchMPP import SearcherMPP

import time
import threading


air_cargo_problem1 = create_air_cargo_problem1()
air_cargo_problem2 = create_air_cargo_problem2()
air_cargo_problem3 = create_air_cargo_problem3()
air_cargo_problem4 = create_air_cargo_problem4()

def run_searcher(s2):
    s2.search()

def run_problem(problem):
    start_time = time.time()
    
    try:
        s2 = SearcherMPP(Forward_STRIPS(problem))

        search_thread = threading.Thread(target=run_searcher, args=(s2,))
        
        search_thread.daemon = True 
        search_thread.start()

        search_thread.join(timeout=100) 
        
        if search_thread.is_alive():
            raise TimeoutError("Timeout")

        no_heuristic_time = time.time() - start_time

    except TimeoutError:
        no_heuristic_time = "Timeout reached"

    start_time = time.time()
    s2 = SearcherMPP(Forward_STRIPS(problem, h_movement_cost))
    s2.search()
    heuristic_time = time.time() - start_time

    print(f"No heuristic: {no_heuristic_time}")
    print(f"With heuristic: {heuristic_time}")


# print("For problem 1")
# run_problem(air_cargo_problem1)

# print("For problem 2")
# run_problem(air_cargo_problem2)

# print("For problem 3")
# run_problem(air_cargo_problem3)

print("For problem 4")
run_problem(air_cargo_problem4)