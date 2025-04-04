from stripsProblem import STRIPS_domain, Strips, Planning_problem
from stripsForwardPlanner import Forward_STRIPS

from air_cargo_heuristics import h_movement_cost
from air_cargo_problems import create_air_cargo_problem1, create_air_cargo_problem2, create_air_cargo_problem3, create_air_cargo_problem4, create_air_cargo_problem5, create_air_cargo_problem6, create_air_cargo_problem7

from searchMPP import SearcherMPP

import time
import threading


air_cargo_problem1 = create_air_cargo_problem1()
air_cargo_problem2 = create_air_cargo_problem2()
air_cargo_problem3 = create_air_cargo_problem3()
air_cargo_problem4 = create_air_cargo_problem4()
air_cargo_problem5 = create_air_cargo_problem5()
air_cargo_problem6 = create_air_cargo_problem6()
air_cargo_problem7 = create_air_cargo_problem7()

def run_searcher(s2):
    s2.search()

def run_problem(problem):
    current_state = problem.initial_state  # Rozpoczynamy od stanu początkowego

    for i, subgoal in enumerate(problem.goal[:-1]):  # Pomijamy ostatni cel
        print(f"Solving subgoal {i + 1}: {subgoal}")
        start_time = time.time()
        
        try:
            # Tworzymy nowy problem dla podcelu
            subproblem = Planning_problem(problem.prob_domain, current_state, subgoal)
            s2 = SearcherMPP(Forward_STRIPS(subproblem))
            search_thread = threading.Thread(target=run_searcher, args=(s2,))
            
            search_thread.daemon = True
            search_thread.start()
            search_thread.join(timeout=300)
            
            if search_thread.is_alive():
                raise TimeoutError("Timeout")
            
            no_heuristic_time = time.time() - start_time
        except TimeoutError:
            no_heuristic_time = "Timeout reached"
        
        start_time = time.time()
        s2 = SearcherMPP(Forward_STRIPS(subproblem, h_movement_cost))
        s2.search()
        heuristic_time = time.time() - start_time
        
        print(f"No heuristic: {no_heuristic_time}")
        print(f"With heuristic: {heuristic_time}")
        
        # Aktualizujemy stan początkowy na podstawie osiągniętego podcelu
        current_state = {**current_state, **subgoal}
    
    print("All subgoals achieved. Solving final goal...")
    # Rozwiązujemy główny cel na podstawie zaktualizowanego stanu
    final_goal = problem.goal[-1]
    final_problem = Planning_problem(problem.prob_domain, current_state, final_goal)
    
    start_time = time.time()
    try:
        s2 = SearcherMPP(Forward_STRIPS(final_problem))
        search_thread = threading.Thread(target=run_searcher, args=(s2,))
        
        search_thread.daemon = True
        search_thread.start()
        search_thread.join(timeout=300)
        
        if search_thread.is_alive():
            raise TimeoutError("Timeout")
        
        no_heuristic_time = time.time() - start_time
    except TimeoutError:
        no_heuristic_time = "Timeout reached"
    
    start_time = time.time()
    s2 = SearcherMPP(Forward_STRIPS(final_problem, h_movement_cost))
    s2.search()
    heuristic_time = time.time() - start_time
    
    print(f"Final goal - No heuristic: {no_heuristic_time}")
    print(f"Final goal - With heuristic: {heuristic_time}")


print("For problem 1")
run_problem(air_cargo_problem1)

print("For problem 2")
run_problem(air_cargo_problem2)

print("For problem 3")
run_problem(air_cargo_problem3)

print("For problem 4")
run_problem(air_cargo_problem4)

print("For problem 5")
run_problem(air_cargo_problem5)

print("For problem 6")
run_problem(air_cargo_problem6)

print("For problem 7")
run_problem(air_cargo_problem7)
