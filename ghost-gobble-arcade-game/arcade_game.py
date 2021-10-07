def eat_ghost(power_pellet_active, touching_ghost):
   
    if power_pellet_active and touching_ghost:
        return True
    else:
        return False
def score(touching_power_pellet, touching_dot):
    
    if touching_power_pellet or touching_dot:
        return True
    else:
        return False
def lose(power_pellet_active, touching_ghost):
  
    if touching_ghost and not power_pellet_active:
        return True
    else:
        return False
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
   
    haslost = lose(power_pellet_active, touching_ghost)
    if not haslost and has_eaten_all_dots:
        return True
    else:
        return False