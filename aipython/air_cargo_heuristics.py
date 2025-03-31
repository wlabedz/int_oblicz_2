def h_movement_cost(state, goal):
    """ Based on number of actions """
    movement_cost = 0
    
    for fact in goal.keys():
        if goal[fact] is True and state.get(fact, False) is False and '_at_' in fact:
            cargo, dest = fact.split("_at_")
            if cargo.startswith("c"): 
                current_loc = next((key.split('_at_')[1] for key, loc in state.items() if cargo in key and loc and '_at_' in key), None)
                
                if current_loc == dest:
                    continue
                
                if current_loc:
                    planes_on_wrong_airport = [key.split("_at_")[0] for key, loc in state.items() if "p" in key and loc and "_at_" in key and key.split("_at_")[1] == current_loc]
                    
                    if planes_on_wrong_airport:
                        movement_cost += 3
                    else:
                        movement_cost += 4
                else:
                    current_plane = next((key.split('_in_')[1] for key, loc in state.items() if cargo in key and loc and '_in_' in key), None)
                    
                    if current_plane:
                        plane_location = next((key.split('_at_')[1] for key, loc in state.items() if current_plane in key and loc and '_at_' in key), None)
                        
                        if plane_location == dest:
                            movement_cost += 1 
                        else:
                            movement_cost += 2
                
    return movement_cost