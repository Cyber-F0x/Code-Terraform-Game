lock = self.contract.lock
transmitter = get_component("transmitter")
transmitter.connect("earth")
tumblr = [0,0,0,0,0,0]

def brute_force_pin(i):
    for x in range(99):
        tumblr[i] = x
        if lock.intercept(tumblr)[i] == True:
            return

for i,each_pin in enumerate(tumblr):
    brute_force_pin(i)
    print(tumblr)
    
transmitter.transmit(self.contract.id,tumblr)
    
    