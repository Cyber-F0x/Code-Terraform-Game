# todo save this in the data bank for later.
dict_states = {}

def find_heater_efficency(state) -> int:
    for i in range(1000):
        self.set_power(i)
        if self.efficiency() == 100:
            watts = i
            dict_states[state] = watts
            print(f"{state} requires {watts}W")
            return watts
    
while True:
    state = self.thermal_state()
    watts = find_heater_efficency(state)
    while self.thermal_state() == state:
        self.set_power(watts)
    