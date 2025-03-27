from stripsProblem import STRIPS_domain, Strips, Planning_problem
from stripsForwardPlanner import Forward_STRIPS
def load(cargo, plane, airport):
    """string for the 'load' action"""
    return f'load_{cargo}_into_{plane}_at_{airport}'

def unload(cargo, plane, airport):
    """string for the 'unload' action"""
    return f'unload_{cargo}_from_{plane}_at_{airport}'

def fly(plane, from_airport, to_airport):
    """string for the 'fly' action"""
    return f'fly_{plane}_from_{from_airport}_to_{to_airport}'

def at(obj):
    """string for the 'at' feature"""
    return f'at_{obj}'

def in_plane(cargo, plane):
    """string for the 'in' feature"""
    return f'in_{cargo}_on_{plane}'


def create_air_cargo_world(airports={'airport1', 'airport2'}, planes={'plane1', 'plane2'}, cargos={'cargo1', 'cargo2'}):
    airports_and_planes = airports | planes
    stmap = {
        Strips(load(c, p, a), {at(c): a, at(p): a, in_plane(c, p): False, at(a): True}, 
               {in_plane(c, p): True, at(c): False}) 
        for c in cargos for p in planes for a in airports if c != p and p != a}
    
    stmap.update({Strips(unload(c, p, a), {in_plane(c, p): True, at(p): a, at(c): False}, 
                         {at(c): a, in_plane(c, p): False}) 
                  for c in cargos for p in planes for a in airports if c != p and p != a})

    stmap.update({Strips(fly(p, from_airport, to_airport), {at(p): from_airport, at(from_airport): True, at(to_airport): True}, 
                         {at(p): to_airport, at(from_airport): False}) 
                  for p in planes for from_airport in airports for to_airport in airports if from_airport != to_airport})
    
    # First dictionary comprehension for the 'at' features
    feature_domain_dict = {
        at(obj): airports_and_planes for obj in airports_and_planes
    }

    # Second dictionary comprehension for the 'in_plane' features
    feature_domain_dict.update({
        in_plane(c, p): False for c in cargos for p in planes
    })

    # Adding the 'at' feature for the 'table'
    feature_domain_dict.update({at('table'): True})

    return STRIPS_domain(feature_domain_dict, stmap)



initial_state = {
    at('cargo1'):'airport1', in_plane('cargo1', 'plane1'): False, at('plane1'):'airport1', at('airport1'):True, 
    at('cargo2'):'airport1', in_plane('cargo2', 'plane2'): False, at('plane2'):'airport1', at('airport1'):True,
    at('airport2'):False
}

goal_state = {
    at('cargo1'):'airport2', in_plane('cargo1', 'plane1'): False, at('plane1'):'airport2', at('airport2'):True,
    at('cargo2'):'airport1', in_plane('cargo2', 'plane2'): False, at('plane2'):'airport1', at('airport1'):True
}

# Define the problem
air_cargo_domain = create_air_cargo_world()
problem_1 = Planning_problem(air_cargo_domain, initial_state, goal_state)


from searchMPP import SearcherMPP
SearcherMPP(Forward_STRIPS(problem_1)).search()  #A* with MPP
# DF_branch_and_bound(Forward_STRIPS(stripsProblem.problem1),10).search() #B&B
# To find more than one plan:
s1 = SearcherMPP(Forward_STRIPS(problem_1))  #A*
s1.search()  #find another plan