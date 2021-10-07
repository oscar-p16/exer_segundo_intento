
def is_criticality_balanced(temperature, neutrons_emitted):
    
 
    return (temperature < 800) and (neutrons_emitted > 500) and (temperature * neutrons_emitted < 500000)
def reactor_efficiency(voltage, current, theoretical_max_power):
 
    efficiency = ((voltage * current) / theoretical_max_power) * 100
    if efficiency >= 80:
        return "green"
    if efficiency >= 60:
        return "orange"
    if efficiency >= 30:
        return "red"
    return "black"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
  
    criticality = temperature * neutrons_produced_per_second
    if criticality < (threshold * 0.4):
        return "LOW"
    if (threshold * 0.9) <= criticality <= (threshold * 1.1):
        return "NORMAL"
    return "DANGER"