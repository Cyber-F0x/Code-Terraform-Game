#Might be worth adding in an edge case to account for lower == higher
while True:
    lower = self.next_window_low()
    high = self.next_window_high()
    while self.gauge() > lower and self.gauge() < high:
        self.sync()
    