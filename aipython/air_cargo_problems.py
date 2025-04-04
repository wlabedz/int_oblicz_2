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

    subgoal1 = {at('c3', 'GDN'): True, at('c4', 'KRK'): True}
    subgoal2 = {at('c2', 'KTW'): True, at('c1', 'WAW'): True}
    goal_state = {at('c1', 'GDN'): True, at('c2', 'KRK'): True, at('c3', 'KTW'): True, at('c4', 'WAW'): True, at('c5', 'GDN'): True}

    return Planning_problem(air_cargo_domain, initial_state, [subgoal1, subgoal2, goal_state])

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

    subgoal1 = {at('c1', 'KRK'): True, at('c2', 'WAW'): True}
    subgoal2 = {at('c3', 'GDN'): True}
    goal_state = {at('c1', 'GDN'): True, at('c2', 'KRK'): True, at('c3', 'WAW'): True}

    return Planning_problem(air_cargo_domain, initial_state, [subgoal1, subgoal2, goal_state])


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

    subgoal1 = {at('c1', 'BER'): True, at('c2', 'NYC'): True}
    subgoal2 = {at('c3', 'LON'): True, at('c4', 'BER'): True}
    goal_state = {at('c1', 'LON'): True, at('c2', 'BER'): True, at('c3', 'NYC'): True, at('c4', 'LON'): True}

    return Planning_problem(air_cargo_domain, initial_state, [subgoal1, subgoal2, goal_state])

def create_air_cargo_problem4():
    air_cargo_domain = create_air_cargo_domain({'c1', 'c2', 'c3'}, 
                                               {'p1', 'p2'}, 
                                               {'WAW', 'KRK'})

    initial_state = {at(c, a): False for c in {'c1', 'c2', 'c3'} 
                     for a in {'WAW', 'KRK'}}
    initial_state.update({at(p, a): False for p in {'p1', 'p2'} 
                          for a in {'WAW', 'KRK'}})
    initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2', 'c3'} 
                          for p in {'p1', 'p2'}})

    initial_state[at('c1', 'WAW')] = True
    initial_state[at('c2', 'KRK')] = True
    initial_state[at('c3', 'KRK')] = True

    initial_state[at('p1', 'KRK')] = True
    initial_state[at('p2', 'WAW')] = True

    subgoal1 = {at('c1', 'WAW'): True, at('c2', 'WAW'): True}
    subgoal2 = {at('c3', 'WAW'): True}
    goal_state = {at('c1', 'KRK'): True, at('c2', 'WAW'): True, at('c3', 'WAW'): True}

    return Planning_problem(air_cargo_domain, initial_state, [subgoal1, subgoal2, goal_state])
   

def create_air_cargo_problem5():
    air_cargo_domain = create_air_cargo_domain({'c1', 'c2', 'c3', 'c4', 'c5'}, 
                                               {'p1', 'p2', 'p3'}, 
                                               {'NYC', 'LON', 'BER', 'PAR'})

    initial_state = {at(c, a): False for c in {'c1', 'c2', 'c3', 'c4', 'c5'} 
                     for a in {'NYC', 'LON', 'BER', 'PAR'}}
    initial_state.update({at(p, a): False for p in {'p1', 'p2', 'p3'} 
                          for a in {'NYC', 'LON', 'BER', 'PAR'}})
    initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2', 'c3', 'c4', 'c5'} 
                          for p in {'p1', 'p2', 'p3'}})

    initial_state[at('c1', 'NYC')] = True
    initial_state[at('c2', 'LON')] = True
    initial_state[at('c3', 'BER')] = True
    initial_state[at('c4', 'PAR')] = True
    initial_state[at('c5', 'NYC')] = True

    initial_state[at('p1', 'NYC')] = True
    initial_state[at('p2', 'LON')] = True
    initial_state[at('p3', 'BER')] = True

    subgoal1 = {at('c1', 'LON'): True, at('c2', 'BER'): True}
    subgoal2 = {at('c3', 'PAR'): True, at('c4', 'NYC'): True}
    goal_state = {at('c5', 'LON'): True, at('c1', 'PAR'): True, at('c2', 'NYC'): True, at('c3', 'LON'): True, at('c4', 'BER'): True}

    return Planning_problem(air_cargo_domain, initial_state, [subgoal1, subgoal2, goal_state])


def create_air_cargo_problem6():
    air_cargo_domain = create_air_cargo_domain({'c1', 'c2', 'c3', 'c4', 'c5', 'c6'}, 
                                               {'p1', 'p2', 'p3', 'p4'}, 
                                               {'WAW', 'GDN', 'KRK', 'KTW', 'POZ'})

    initial_state = {at(c, a): False for c in {'c1', 'c2', 'c3', 'c4', 'c5', 'c6'} 
                     for a in {'WAW', 'GDN', 'KRK', 'KTW', 'POZ'}}
    initial_state.update({at(p, a): False for p in {'p1', 'p2', 'p3', 'p4'} 
                          for a in {'WAW', 'GDN', 'KRK', 'KTW', 'POZ'}})
    initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2', 'c3', 'c4', 'c5', 'c6'} 
                          for p in {'p1', 'p2', 'p3', 'p4'}})

    initial_state[at('c1', 'WAW')] = True
    initial_state[at('c2', 'GDN')] = True
    initial_state[at('c3', 'KRK')] = True
    initial_state[at('c4', 'KTW')] = True
    initial_state[at('c5', 'POZ')] = True
    initial_state[at('c6', 'WAW')] = True

    initial_state[at('p1', 'WAW')] = True
    initial_state[at('p2', 'GDN')] = True
    initial_state[at('p3', 'KRK')] = True
    initial_state[at('p4', 'KTW')] = True

    subgoal1 = {at('c1', 'GDN'): True, at('c2', 'KRK'): True}
    subgoal2 = {at('c3', 'KTW'): True, at('c4', 'POZ'): True}
    goal_state = {at('c5', 'WAW'): True, at('c6', 'GDN'): True, at('c1', 'KRK'): True, at('c2', 'KTW'): True, at('c3', 'POZ'): True, at('c4', 'WAW'): True}

    return Planning_problem(air_cargo_domain, initial_state, [subgoal1, subgoal2, goal_state])


def create_air_cargo_problem7():
    air_cargo_domain = create_air_cargo_domain({'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'}, 
                                               {'p1', 'p2', 'p3', 'p4', 'p5'}, 
                                               {'NYC', 'LON', 'BER', 'PAR', 'WAW', 'GDN'})

    initial_state = {at(c, a): False for c in {'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'} 
                     for a in {'NYC', 'LON', 'BER', 'PAR', 'WAW', 'GDN'}}
    initial_state.update({at(p, a): False for p in {'p1', 'p2', 'p3', 'p4', 'p5'} 
                          for a in {'NYC', 'LON', 'BER', 'PAR', 'WAW', 'GDN'}})
    initial_state.update({in_cargo(c, p): False for c in {'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'} 
                          for p in {'p1', 'p2', 'p3', 'p4', 'p5'}})

    initial_state[at('c1', 'NYC')] = True
    initial_state[at('c2', 'LON')] = True
    initial_state[at('c3', 'BER')] = True
    initial_state[at('c4', 'PAR')] = True
    initial_state[at('c5', 'WAW')] = True
    initial_state[at('c6', 'GDN')] = True
    initial_state[at('c7', 'NYC')] = True

    initial_state[at('p1', 'NYC')] = True
    initial_state[at('p2', 'LON')] = True
    initial_state[at('p3', 'BER')] = True
    initial_state[at('p4', 'PAR')] = True
    initial_state[at('p5', 'WAW')] = True

    subgoal1 = {at('c1', 'LON'): True, at('c2', 'BER'): True}
    subgoal2 = {at('c3', 'PAR'): True, at('c4', 'WAW'): True}
    goal_state = {at('c5', 'GDN'): True, at('c6', 'NYC'): True, at('c7', 'LON'): True, at('c1', 'BER'): True, at('c2', 'PAR'): True, at('c3', 'WAW'): True, at('c4', 'GDN'): True}

    return Planning_problem(air_cargo_domain, initial_state, [subgoal1, subgoal2, goal_state])
