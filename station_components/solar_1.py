sun_clock = get_component("clock")
# Example sun at 60 then tilt = 30
while True:
    self.set_tilt(90 - sun_clock.get_elevation())
    