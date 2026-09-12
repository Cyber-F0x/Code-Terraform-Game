while True:
    if self.waste() >55:
        self.dump_waste()
    CO2_level = get_component("atmosphere").get_co2()
    intake_level = CO2_level/10
    self.set_intake(intake_level)
    
    #print(self.dump_penalty())