from stripsProblem import STRIPS_domain, Strips

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


