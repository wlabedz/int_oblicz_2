from stripsProblem import STRIPS_domain, Strips, Planning_problem
from stripsForwardPlanner import Forward_STRIPS

boolean = {False, True}

def load(c, p, a):
    return f'load_{c}_onto_{p}_at_{a}'

def unload(c, p, a):
    return f'unload_{c}_from_{p}_at_{a}'

def fly(p, fr, to):
    return f'fly_{p}_from_{fr}_to_{to}'

def in_cargo(c, p):
    return f'{c}_in_{p}'

def at(obj, place):
    return f'{obj}_at_{place}'

def create_air_cargo_domain(cargos={'c1', 'c2'}, planes={'p1'}, airports={'a1', 'a2'}):
    actions = set()
    
    for c in cargos:
        for p in planes:
            for a in airports:
                actions.add(Strips(load(c, p, a),
                                   {at(c, a): True, at(p, a): True},
                                   {in_cargo(c, p): True, at(c, a): False}))
    
    for c in cargos:
        for p in planes:
            for a in airports:
                actions.add(Strips(unload(c, p, a),
                                   {in_cargo(c, p): True, at(p, a): True},
                                   {at(c, a): True, in_cargo(c, p): False}))
    
    for p in planes:
        for fr in airports:
            for to in airports:
                if fr != to:
                    actions.add(Strips(fly(p, fr, to),
                                       {at(p, fr): True},
                                       {at(p, to): True, at(p, fr): False}))
    
    feature_domain_dict = {at(obj, place): boolean for obj in cargos | planes for place in airports}
    feature_domain_dict.update({in_cargo(c, p): boolean for c in cargos for p in planes})
    
    return STRIPS_domain(feature_domain_dict, actions)


from searchMPP import SearcherMPP


air_cargo_domain = create_air_cargo_domain({'c1', 'c2'}, {'p1', 'p2'}, {'a1', 'a2', 'a3'})

initial_state = {at(c, a): False for c in {'c1', 'c2'} for a in {'a1', 'a2', 'a3'}}
initial_state.update({at(p, a): False for p in {'p1', 'p2'} for a in {'a1', 'a2', 'a3'}})
initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2'} for p in {'p1', 'p2'}})

initial_state[at('c1', 'a1')] = True
initial_state[at('c2', 'a2')] = True
initial_state[at('p1', 'a1')] = True
initial_state[at('p2', 'a2')] = True
goal_state = {at('c1', 'a3'): True, at('c2', 'a3'): True}

air_cargo_problem = Planning_problem(air_cargo_domain, initial_state, goal_state)

s2 = SearcherMPP(Forward_STRIPS(air_cargo_problem))
s2.search()
