from searchMPP import SearcherMPP
from air_cargo_problems import create_air_cargo_problem4, create_air_cargo_problem2, create_air_cargo_problem3
from air_cargo_domain import in_cargo, at
from stripsRegressionPlanner import Regression_STRIPS, Subgoal
from air_cargo_heuristics import h_movement_cost

from searchMPP import SearcherMPP
import time, threading

def solve_problem_with_subgoals(problem, subgoals):
    current_state = problem.initial_state
    
    for i, subgoal in enumerate(subgoals, start=1):
        print(f"Subgoal {i}")
        
        planner = Regression_STRIPS(problem)
        
        planner.top_goal = subgoal
        
        sol = SearcherMPP(planner).search()
        
        for action in planner.top_goal.assignment:
            current_state[action] = planner.top_goal.assignment[action]
        

    planner = Regression_STRIPS(problem)
    planner.top_goal = Subgoal(problem.goal)
    SearcherMPP(planner).search()

    for action in planner.top_goal.assignment:
        current_state[action] = planner.top_goal.assignment[action]
    return current_state


def solve_problem_with_subgoals_heur(problem, subgoals,heur):
    current_state = problem.initial_state
    
    for i, subgoal in enumerate(subgoals, start=1):
        print(f"Subgoal {i}")
        
        planner = Regression_STRIPS(problem,heur=heur)
        
        planner.top_goal = subgoal
        
        SearcherMPP(planner).search()
        
        for action in planner.top_goal.assignment:
            current_state[action] = planner.top_goal.assignment[action]
        

    planner = Regression_STRIPS(problem,heur=heur)
    planner.top_goal = Subgoal(problem.goal)
    SearcherMPP(planner).search()

    for action in planner.top_goal.assignment:
        current_state[action] = planner.top_goal.assignment[action]

    return current_state



#Problem 2

start_time = time.time()
    
try:
    problem2 = create_air_cargo_problem2()
    subgoals = [ 
        Subgoal({in_cargo('c1', 'p1'): True, in_cargo('c2','p2') : True, in_cargo('c3','p3') : True}) ,
        Subgoal({at('p1', 'GDN'): True, at('p2', 'KRK'): True, at('p3','WAW') : True})
    ]

    print("p2 No heuristic")
    search_thread = threading.Thread(target=solve_problem_with_subgoals, args=(problem2,subgoals))
        
    search_thread.daemon = True 
    search_thread.start()

    search_thread.join(timeout=100) 
        
    if search_thread.is_alive():
        raise TimeoutError("Timeout")

    no_heuristic_time = time.time() - start_time

except TimeoutError:
    no_heuristic_time = "Timeout reached"


problem2 = create_air_cargo_problem2()
subgoals = [ 
        Subgoal({in_cargo('c1', 'p1'): True, in_cargo('c2','p2') : True, in_cargo('c3','p3') : True}) ,
        Subgoal({at('p1', 'GDN'): True, at('p2', 'KRK'): True, at('p3','WAW') : True})
    ]
start_time = time.time()
print("p2 Heuristic")
solve_problem_with_subgoals_heur(problem=problem2, subgoals=subgoals,heur=h_movement_cost)
heuristic_time = time.time() - start_time

print(f"p2 No heuristic: {no_heuristic_time}")
print(f"p2 With heuristic: {heuristic_time}")

#Problem 3

start_time = time.time()
    
try:
    problem3 = create_air_cargo_problem3()
    subgoals = [ 
        Subgoal({in_cargo('c1', 'p1'): True, in_cargo('c2','p2') : True, in_cargo('c3','p3') : True}) ,
        Subgoal({at('p1', 'LON'): True, at('p2', 'BER'): True, at('p3','NYC') : True}),
        Subgoal({in_cargo('c4', 'p3'): True}),
        Subgoal({at('c4','LON'): True})
    ]

    print("p3 No heuristic")
    search_thread = threading.Thread(target=solve_problem_with_subgoals, args=(problem3,subgoals))
        
    search_thread.daemon = True 
    search_thread.start()

    search_thread.join(timeout=100) 
        
    if search_thread.is_alive():
        raise TimeoutError("Timeout")

    no_heuristic_time = time.time() - start_time

except TimeoutError:
    no_heuristic_time = "Timeout reached"


problem3 = create_air_cargo_problem3()
subgoals = [ 
        Subgoal({in_cargo('c1', 'p1'): True, in_cargo('c2','p2') : True, in_cargo('c3','p3') : True}) ,
        Subgoal({at('p1', 'LON'): True, at('p2', 'BER'): True, at('p3','NYC') : True}),
        Subgoal({in_cargo('c4', 'p3'): True}),
        Subgoal({at('c4','LON') : True})
    ]
start_time = time.time()
print("p3 Heuristic")
solve_problem_with_subgoals_heur(problem=problem3, subgoals=subgoals,heur=h_movement_cost)
heuristic_time = time.time() - start_time

print(f"p3 No heuristic: {no_heuristic_time}")
print(f"p3 With heuristic: {heuristic_time}")


#Problem 4

start_time = time.time()
    
try:
    problem4 = create_air_cargo_problem4()
    subgoals = [ 
        Subgoal({in_cargo('c1', 'p2'): True, in_cargo('c2','p1') : True}) ,
        Subgoal({at('p2', 'KRK'): True, at('p1', 'WAW'): True})
    ]

    print("p4 No heuristic")
    search_thread = threading.Thread(target=solve_problem_with_subgoals, args=(problem4,subgoals))
        
    search_thread.daemon = True 
    search_thread.start()

    search_thread.join(timeout=100) 
        
    if search_thread.is_alive():
        raise TimeoutError("Timeout")

    no_heuristic_time = time.time() - start_time

except TimeoutError:
    no_heuristic_time = "Timeout reached"


problem4 = create_air_cargo_problem4()
subgoals = [ 
    Subgoal({in_cargo('c1', 'p2'): True, in_cargo('c2','p1') : True}) ,
    Subgoal({at('c1', 'KRK'): True, at('c2', 'WAW'): True})
]
start_time = time.time()
print("p4 Heuristic")
solve_problem_with_subgoals_heur(problem=problem4, subgoals=subgoals,heur=h_movement_cost)
heuristic_time = time.time() - start_time

print(f"p4 No heuristic: {no_heuristic_time}")
print(f"p4 With heuristic: {heuristic_time}")
