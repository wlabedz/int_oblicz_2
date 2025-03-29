def h_movement_cost(state, goal):
    """ Based on number of actions """
    movement_cost = 0
    
    for fact in goal:
        #if cargo (object) which should be at the particular airport is not there
        if goal[fact] is True and state.get(fact, False) is False and '_at_' in fact:
            cargo, dest = fact.split("_at_")
            if cargo.startswith("c"): 
                current_loc = next((key.split('_at_')[1] for key, loc in state.items() if cargo in key and loc and '_at_' in key), None)
                
                #cargo is at the correct airport 
                if current_loc == dest:
                    continue
                
                #cargo is at the wrong airport
                if current_loc:
                    #is there any airport at the airport where parcel is located
                    planes_on_wrong_airport = [key.split("_at_")[0] for key, loc in state.items() if "p" in key and state[key] and loc == current_loc]
                    
                    if planes_on_wrong_airport:
                        #if the cargo is already placed in the airport we add two moves (flight and unload)
                        if state.get(f"{cargo}_in_{planes_on_wrong_airport[0]}", False):
                            movement_cost += 2
                        #if it is not loaded then 3 moves
                        else:
                            movement_cost += 3
                    
                    # there is no plane at the airport where parcel is placed
                    else:
                        movement_cost += 4
                else:
                    movement_cost += 4
                
    return movement_cost