from stripsProblem import Planning_problem
from air_cargo_domain import create_air_cargo_domain, in_cargo, at

def create_air_cargo_problem1():
    air_cargo_domain = create_air_cargo_domain({'c1', 'c2', 'c3', 'c4', 'c5'}, 
                                               {'p1', 'p2', 'p3'}, 
                                               {'WAW', 'GDN', 'KRK', 'KTW'})

    initial_state = {at(c, a): False for c in {'c1', 'c2', 'c3', 'c4', 'c5'} 
                     for a in {'WAW', 'GDN', 'KRK', 'KTW'}}
    initial_state.update({at(p, a): False for p in {'p1', 'p2', 'p3'} 
                          for a in {'WAW', 'GDN', 'KRK', 'KTW'}})
    initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2', 'c3', 'c4', 'c5'} 
                          for p in {'p1', 'p2', 'p3'}})

    initial_state[at('c1', 'WAW')] = True
    initial_state[at('c2', 'GDN')] = True
    initial_state[at('c3', 'KRK')] = True
    initial_state[at('c4', 'KTW')] = True
    initial_state[at('c5', 'WAW')] = True

    initial_state[at('p1', 'WAW')] = True
    initial_state[at('p2', 'GDN')] = True
    initial_state[at('p3', 'KRK')] = True

    goal_state = {
        at('c1', 'GDN'): True,
        at('c2', 'KRK'): True,
        at('c3', 'KTW'): True,
        at('c4', 'WAW'): True,
        at('c5', 'GDN'): True
    }

    return Planning_problem(air_cargo_domain, initial_state, goal_state)


def create_air_cargo_problem2():
    air_cargo_domain = create_air_cargo_domain({'c1', 'c2', 'c3'}, 
                                               {'p1', 'p2', 'p3', 'p4'}, 
                                               {'WAW', 'GDN', 'KRK'})

    initial_state = {at(c, a): False for c in {'c1', 'c2', 'c3'} 
                     for a in {'WAW', 'GDN', 'KRK'}}
    initial_state.update({at(p, a): False for p in {'p1', 'p2', 'p3', 'p4'} 
                          for a in {'WAW', 'GDN', 'KRK'}})
    initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2', 'c3'} 
                          for p in {'p1', 'p2', 'p3', 'p4'}})

    initial_state[at('c1', 'WAW')] = True
    initial_state[at('c2', 'GDN')] = True
    initial_state[at('c3', 'KRK')] = True

    initial_state[at('p1', 'WAW')] = True
    initial_state[at('p2', 'GDN')] = True
    initial_state[at('p3', 'KRK')] = True
    initial_state[at('p4', 'WAW')] = True

    goal_state = {
        at('c1', 'GDN'): True,
        at('c2', 'KRK'): True,
        at('c3', 'WAW'): True
    }

    return Planning_problem(air_cargo_domain, initial_state, goal_state)


def create_air_cargo_problem3():
    air_cargo_domain = create_air_cargo_domain({'c1', 'c2', 'c3', 'c4'}, 
                                               {'p1', 'p2', 'p3'}, 
                                               {'NYC', 'LON', 'BER'})

    initial_state = {at(c, a): False for c in {'c1', 'c2', 'c3', 'c4'} 
                     for a in {'NYC', 'LON', 'BER'}}
    initial_state.update({at(p, a): False for p in {'p1', 'p2', 'p3'} 
                          for a in {'NYC', 'LON', 'BER'}})
    initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2', 'c3', 'c4'} 
                          for p in {'p1', 'p2', 'p3'}})

    initial_state[at('c1', 'NYC')] = True
    initial_state[at('c2', 'LON')] = True
    initial_state[at('c3', 'BER')] = True
    initial_state[at('c4', 'NYC')] = True

    initial_state[at('p1', 'NYC')] = True
    initial_state[at('p2', 'LON')] = True
    initial_state[at('p3', 'BER')] = True

    goal_state = {
        at('c1', 'LON'): True,
        at('c2', 'BER'): True,
        at('c3', 'NYC'): True,
        at('c4', 'LON'): True
    }

    return Planning_problem(air_cargo_domain, initial_state, goal_state)

def create_air_cargo_problem4():
    air_cargo_domain = create_air_cargo_domain({'c1', 'c2', 'c3'}, 
                                               {'p1', 'p2'}, 
                                               {'WAW', 'KRK'})

    initial_state = {at(c, a): False for c in {'c1', 'c2', 'c3'} 
                     for a in {'WAW','KRK'}}
    initial_state.update({at(p, a): False for p in {'p1', 'p2'} 
                          for a in {'WAW','KRK'}})
    initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2', 'c3'} 
                          for p in {'p1', 'p2'}})

    initial_state[at('c1', 'WAW')] = True
    initial_state[at('c2', 'KRK')] = True
    initial_state[at('c3', 'KRK')] = True
    

    initial_state[at('p1', 'KRK')] = True
    initial_state[at('p2', 'WAW')] = True

    goal_state = {
        at('c1', 'KRK'): True,
        at('c2', 'WAW'): True,
        at('c3', 'WAW'): True
    }

    return Planning_problem(air_cargo_domain, initial_state, goal_state)