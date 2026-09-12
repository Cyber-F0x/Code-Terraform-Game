while True:
    orders = get_component("bio_exchange_1").active_order()
    self.input.flush()
    if orders != None:
        delivered = orders.delivered
        self.input.connect("inventory")
        for each_requirment in orders.requires:
            
            while delivered[each_requirment] != orders.requires[each_requirment]:
                self.input.take(each_requirment,1)
                result = self.deliver()
                if result.status == "ok":
                    delivered[each_requirment] += 1
                    continue
                if result.status == "busy":
                    sleep(0.2)
                    continue
        
